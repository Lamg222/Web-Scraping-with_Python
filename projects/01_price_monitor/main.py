#!/usr/bin/env python3
"""
🛒 Price Monitor - Sistema de Monitoreo de Precios E-commerce
=============================================================

Autor: Curso de Web Scraping con Python
Versión: 1.0
Descripción: Sistema completo para monitorear precios de productos en múltiples tiendas online

Uso:
    python main.py --scrape                    # Ejecutar scraping una vez
    python main.py --dashboard                 # Iniciar dashboard web
    python main.py --schedule --interval=3600  # Ejecutar cada hora
    python main.py --report --email=user@example.com  # Enviar reporte
"""

import argparse
import sys
import os
import time
import logging
from datetime import datetime
from typing import List, Dict
import asyncio
from pathlib import Path

# Agregar el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Imports de módulos propios
from scraper import PriceScraper, ScrapingConfig
from database import PriceDB, Product, PriceHistory
from dashboard import create_app
from alerts import AlertSystem
from analyzer import PriceAnalyzer
from utils import setup_logging, load_config, validate_config

# Configuración de logging
logger = logging.getLogger(__name__)

class PriceMonitor:
    """
    Clase principal que orquesta todas las funcionalidades del monitor de precios.
    """
    
    def __init__(self, config_path: str = "config/settings.json"):
        """
        Inicializa el monitor de precios.
        
        Args:
            config_path: Ruta al archivo de configuración
        """
        self.config = load_config(config_path)
        validate_config(self.config)
        
        # Inicializar componentes
        self.db = PriceDB(self.config['database']['url'])
        self.scraper = PriceScraper(ScrapingConfig(
            delay=self.config['scraping']['delay'],
            timeout=self.config['scraping']['timeout'],
            user_agent=self.config['scraping']['user_agent']
        ))
        self.alert_system = AlertSystem(self.config['alerts'])
        self.analyzer = PriceAnalyzer(self.db)
        
        # Configurar logging
        setup_logging(
            level=self.config.get('logging', {}).get('level', 'INFO'),
            log_file=self.config.get('logging', {}).get('file', 'data/logs/price_monitor.log')
        )
        
        logger.info("PriceMonitor inicializado correctamente")

    def scrape_once(self, products: List[Dict] = None) -> Dict:
        """
        Ejecuta un ciclo completo de scraping para todos los productos configurados.
        
        Args:
            products: Lista de productos a scrapear (opcional, usa config si no se especifica)
            
        Returns:
            Diccionario con estadísticas del scraping
        """
        if products is None:
            products = self.config['products']
        
        logger.info(f"Iniciando scraping de {len(products)} productos")
        
        stats = {
            'success': 0,
            'errors': 0,
            'total': len(products),
            'start_time': datetime.now(),
            'results': []
        }
        
        for product_config in products:
            try:
                logger.info(f"Scrapeando: {product_config['name']}")
                
                # Obtener o crear producto en DB
                product = self.db.get_or_create_product(
                    name=product_config['name'],
                    urls=product_config['urls'],
                    target_price=product_config.get('target_price')
                )
                
                # Scrapear cada URL del producto
                for url in product_config['urls']:
                    try:
                        price_data = self.scraper.scrape_price(url)
                        
                        if price_data and price_data['price'] > 0:
                            # Guardar en base de datos
                            self.db.save_price_history(
                                product_id=product.id,
                                store=price_data['store'],
                                price=price_data['price'],
                                url=url,
                                availability=price_data.get('availability', True),
                                title=price_data.get('title', product.name)
                            )
                            
                            stats['results'].append({
                                'product': product.name,
                                'store': price_data['store'],
                                'price': price_data['price'],
                                'url': url,
                                'status': 'success'
                            })
                            
                            logger.info(f"✅ {product.name} - {price_data['store']}: ${price_data['price']:.2f}")
                            stats['success'] += 1
                            
                        else:
                            logger.warning(f"⚠️ No se pudo obtener precio para {url}")
                            stats['errors'] += 1
                            
                    except Exception as e:
                        logger.error(f"❌ Error scrapeando {url}: {str(e)}")
                        stats['errors'] += 1
                        
                # Pausa entre productos
                time.sleep(self.config['scraping']['delay'])
                
            except Exception as e:
                logger.error(f"❌ Error procesando producto {product_config['name']}: {str(e)}")
                stats['errors'] += 1
        
        stats['end_time'] = datetime.now()
        stats['duration'] = (stats['end_time'] - stats['start_time']).total_seconds()
        
        logger.info(f"Scraping completado: {stats['success']} éxitos, {stats['errors']} errores")
        
        # Verificar alertas después del scraping
        self.check_alerts()
        
        return stats

    def check_alerts(self) -> List[Dict]:
        """
        Verifica y envía alertas basadas en los precios actuales.
        
        Returns:
            Lista de alertas enviadas
        """
        logger.info("Verificando alertas...")
        
        alerts_sent = []
        products = self.db.get_all_products()
        
        for product in products:
            # Obtener precio más reciente
            latest_prices = self.db.get_latest_prices(product.id)
            
            if not latest_prices:
                continue
            
            # Obtener configuración del producto
            product_config = next(
                (p for p in self.config['products'] if p['name'] == product.name), 
                None
            )
            
            if not product_config:
                continue
                
            target_price = product_config.get('target_price')
            alert_threshold = product_config.get('alert_threshold', 0.1)  # 10% por defecto
            
            for price_record in latest_prices:
                # Verificar si el precio está por debajo del objetivo
                if target_price and price_record.price <= target_price:
                    alert_data = {
                        'type': 'price_target',
                        'product': product.name,
                        'current_price': price_record.price,
                        'target_price': target_price,
                        'store': price_record.store,
                        'url': price_record.url,
                        'savings': target_price - price_record.price
                    }
                    
                    if self.alert_system.send_price_alert(alert_data):
                        alerts_sent.append(alert_data)
                        logger.info(f"🚨 Alerta enviada: {product.name} - ${price_record.price:.2f}")
                
                # Verificar caídas significativas de precio
                price_drop = self.analyzer.detect_price_drop(product.id, threshold=alert_threshold)
                if price_drop:
                    alert_data = {
                        'type': 'price_drop',
                        'product': product.name,
                        'current_price': price_record.price,
                        'previous_price': price_drop['previous_price'],
                        'drop_percentage': price_drop['drop_percentage'],
                        'store': price_record.store,
                        'url': price_record.url
                    }
                    
                    if self.alert_system.send_price_drop_alert(alert_data):
                        alerts_sent.append(alert_data)
                        logger.info(f"📉 Alerta de caída: {product.name} - {price_drop['drop_percentage']:.1f}%")
        
        logger.info(f"Se enviaron {len(alerts_sent)} alertas")
        return alerts_sent

    def generate_report(self, days: int = 7) -> Dict:
        """
        Genera un reporte de precios de los últimos N días.
        
        Args:
            days: Número de días a incluir en el reporte
            
        Returns:
            Diccionario con datos del reporte
        """
        logger.info(f"Generando reporte de últimos {days} días")
        
        report = {
            'period': f"Últimos {days} días",
            'generated_at': datetime.now(),
            'summary': {},
            'products': [],
            'statistics': {}
        }
        
        products = self.db.get_all_products()
        
        for product in products:
            # Obtener histórico de precios
            price_history = self.db.get_price_history(product.id, days=days)
            
            if not price_history:
                continue
            
            # Calcular estadísticas
            prices = [p.price for p in price_history]
            current_price = min(prices)  # Precio más bajo actual
            max_price = max(prices)
            min_price = min(prices)
            avg_price = sum(prices) / len(prices)
            
            # Analizar tendencias
            trend = self.analyzer.calculate_price_trend(product.id, days=days)
            
            product_report = {
                'name': product.name,
                'current_price': current_price,
                'max_price': max_price,
                'min_price': min_price,
                'avg_price': avg_price,
                'price_change': max_price - min_price,
                'trend': trend,
                'data_points': len(price_history),
                'stores': list(set(p.store for p in price_history)),
                'target_price': product.target_price,
                'target_met': product.target_price and current_price <= product.target_price
            }
            
            report['products'].append(product_report)
        
        # Estadísticas generales
        if report['products']:
            report['statistics'] = {
                'total_products': len(report['products']),
                'targets_met': sum(1 for p in report['products'] if p['target_met']),
                'avg_savings': sum(p['price_change'] for p in report['products']) / len(report['products']),
                'total_data_points': sum(p['data_points'] for p in report['products'])
            }
        
        logger.info(f"Reporte generado para {len(report['products'])} productos")
        return report

    def run_dashboard(self, host: str = None, port: int = None, debug: bool = False):
        """
        Inicia el dashboard web.
        
        Args:
            host: Host del servidor (por defecto desde config)
            port: Puerto del servidor (por defecto desde config)
            debug: Modo debug de Flask
        """
        host = host or self.config['dashboard']['host']
        port = port or self.config['dashboard']['port']
        
        logger.info(f"Iniciando dashboard en http://{host}:{port}")
        
        # Crear app Flask
        app = create_app(self.db, self.analyzer, self.config)
        
        # Ejecutar servidor
        app.run(host=host, port=port, debug=debug)

    def run_scheduler(self, interval: int = 3600):
        """
        Ejecuta el scraping de forma programada.
        
        Args:
            interval: Intervalo en segundos entre ejecuciones
        """
        logger.info(f"Iniciando scheduler con intervalo de {interval} segundos ({interval/3600:.1f} horas)")
        
        try:
            while True:
                logger.info("⏰ Ejecutando scraping programado...")
                
                try:
                    stats = self.scrape_once()
                    logger.info(f"✅ Scraping completado: {stats['success']} éxitos, {stats['errors']} errores")
                    
                    # Generar reporte si hay errores significativos
                    if stats['errors'] > stats['success']:
                        logger.warning("⚠️ Más errores que éxitos, generando reporte...")
                        report = self.generate_report(days=1)
                        # Aquí podrías enviar el reporte por email si es crítico
                        
                except Exception as e:
                    logger.error(f"❌ Error en scraping programado: {str(e)}")
                
                logger.info(f"😴 Esperando {interval} segundos hasta el próximo scraping...")
                time.sleep(interval)
                
        except KeyboardInterrupt:
            logger.info("👋 Scheduler detenido por el usuario")
        except Exception as e:
            logger.error(f"❌ Error fatal en scheduler: {str(e)}")
            raise

    def send_report_email(self, email: str, days: int = 7):
        """
        Envía un reporte por email.
        
        Args:
            email: Dirección de email destino
            days: Días a incluir en el reporte
        """
        logger.info(f"Enviando reporte por email a {email}")
        
        # Generar reporte
        report = self.generate_report(days=days)
        
        # Enviar por email
        success = self.alert_system.send_report_email(report, email)
        
        if success:
            logger.info(f"✅ Reporte enviado exitosamente a {email}")
        else:
            logger.error(f"❌ Error enviando reporte a {email}")
        
        return success


def main():
    """
    Función principal que maneja los argumentos de línea de comandos.
    """
    parser = argparse.ArgumentParser(
        description="🛒 Price Monitor - Sistema de Monitoreo de Precios E-commerce",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python main.py --scrape                     # Ejecutar scraping una vez
  python main.py --dashboard                  # Iniciar dashboard web
  python main.py --schedule --interval=3600   # Ejecutar cada hora
  python main.py --report --email=user@example.com  # Enviar reporte

Para más información: https://github.com/tu-usuario/price-monitor
        """
    )
    
    # Argumentos principales
    parser.add_argument('--scrape', action='store_true', 
                       help='Ejecutar scraping una vez')
    parser.add_argument('--dashboard', action='store_true', 
                       help='Iniciar dashboard web')
    parser.add_argument('--schedule', action='store_true', 
                       help='Ejecutar de forma programada')
    parser.add_argument('--report', action='store_true', 
                       help='Generar y mostrar reporte')
    
    # Opciones adicionales
    parser.add_argument('--config', default='config/settings.json',
                       help='Archivo de configuración (default: config/settings.json)')
    parser.add_argument('--interval', type=int, default=3600,
                       help='Intervalo en segundos para scheduling (default: 3600)')
    parser.add_argument('--days', type=int, default=7,
                       help='Días para el reporte (default: 7)')
    parser.add_argument('--email', type=str,
                       help='Email para enviar reporte')
    parser.add_argument('--host', default='localhost',
                       help='Host para dashboard (default: localhost)')
    parser.add_argument('--port', type=int, default=5000,
                       help='Puerto para dashboard (default: 5000)')
    parser.add_argument('--debug', action='store_true',
                       help='Modo debug para dashboard')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Salida detallada')
    
    args = parser.parse_args()
    
    # Si no se especifica ninguna acción, mostrar ayuda
    if not any([args.scrape, args.dashboard, args.schedule, args.report]):
        parser.print_help()
        return
    
    try:
        # Inicializar monitor
        print("🚀 Inicializando Price Monitor...")
        monitor = PriceMonitor(config_path=args.config)
        print("✅ Monitor inicializado correctamente")
        
        # Ejecutar acciones solicitadas
        if args.scrape:
            print("\n🕷️ Ejecutando scraping...")
            stats = monitor.scrape_once()
            print(f"\n📊 Resultados:")
            print(f"   ✅ Éxitos: {stats['success']}")
            print(f"   ❌ Errores: {stats['errors']}")
            print(f"   ⏱️ Duración: {stats['duration']:.1f} segundos")
            
            if args.verbose and stats['results']:
                print("\n📋 Detalle de resultados:")
                for result in stats['results'][:10]:  # Mostrar solo los primeros 10
                    status_icon = "✅" if result['status'] == 'success' else "❌"
                    print(f"   {status_icon} {result['product']} - {result['store']}: ${result['price']:.2f}")
        
        if args.report:
            print(f"\n📈 Generando reporte de últimos {args.days} días...")
            report = monitor.generate_report(days=args.days)
            
            print(f"\n📊 Resumen del reporte:")
            if report['statistics']:
                stats = report['statistics']
                print(f"   📦 Productos monitoreados: {stats['total_products']}")
                print(f"   🎯 Objetivos alcanzados: {stats['targets_met']}")
                print(f"   💰 Ahorro promedio: ${stats['avg_savings']:.2f}")
                print(f"   📊 Puntos de datos: {stats['total_data_points']}")
            
            if args.verbose and report['products']:
                print("\n📋 Detalle por producto:")
                for product in report['products'][:5]:  # Mostrar solo los primeros 5
                    target_icon = "🎯" if product['target_met'] else "📊"
                    print(f"   {target_icon} {product['name']}")
                    print(f"      Precio actual: ${product['current_price']:.2f}")
                    print(f"      Rango: ${product['min_price']:.2f} - ${product['max_price']:.2f}")
                    print(f"      Tendencia: {product['trend']}")
            
            if args.email:
                print(f"\n📧 Enviando reporte a {args.email}...")
                success = monitor.send_report_email(args.email, days=args.days)
                if success:
                    print("✅ Reporte enviado exitosamente")
                else:
                    print("❌ Error enviando reporte")
        
        if args.dashboard:
            print(f"\n🌐 Iniciando dashboard en http://{args.host}:{args.port}")
            print("Presiona Ctrl+C para detener")
            monitor.run_dashboard(host=args.host, port=args.port, debug=args.debug)
        
        if args.schedule:
            print(f"\n⏰ Iniciando scheduler (intervalo: {args.interval}s / {args.interval/3600:.1f}h)")
            print("Presiona Ctrl+C para detener")
            monitor.run_scheduler(interval=args.interval)
    
    except KeyboardInterrupt:
        print("\n\n👋 Programa detenido por el usuario")
    except FileNotFoundError as e:
        print(f"\n❌ Error: Archivo no encontrado - {str(e)}")
        print("💡 Tip: Verifica que el archivo de configuración exista")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
    
    print("\n🏁 ¡Gracias por usar Price Monitor!")


if __name__ == "__main__":
    main()