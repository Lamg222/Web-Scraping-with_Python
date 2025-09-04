"""
🏆 SOLUCIÓN - EJERCICIO 1: Tu Primer Web Scraper
================================================
"""

import os
from bs4 import BeautifulSoup
from typing import List, Dict
import csv
import json


def cargar_html(ruta_archivo: str) -> str:
    """
    Carga el contenido HTML desde un archivo local.
    """
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        return file.read()


def extraer_libros(html_content: str) -> List[Dict]:
    """
    Extrae información de todos los libros del HTML.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    libros = []
    
    # Encontrar todos los artículos de libros
    articulos = soup.find_all('article', class_='book-item')
    
    for articulo in articulos:
        libro = {}
        
        # Título
        titulo_elem = articulo.find('h3', class_='book-title')
        libro['titulo'] = titulo_elem.text.strip() if titulo_elem else 'Sin título'
        
        # Precio actual
        precio_actual_elem = articulo.find('span', class_='current-price')
        if precio_actual_elem:
            # Extraer el precio del atributo data-price o del texto
            precio_data = precio_actual_elem.get('data-price')
            if precio_data:
                libro['precio_actual'] = float(precio_data)
            else:
                # Limpiar el texto del precio
                precio_texto = precio_actual_elem.text.strip()
                precio_texto = precio_texto.replace('$', '').replace(',', '')
                try:
                    libro['precio_actual'] = float(precio_texto)
                except:
                    libro['precio_actual'] = 0.0
        else:
            libro['precio_actual'] = 0.0
        
        # Precio original (si existe)
        precio_original_elem = articulo.find('span', class_='original-price')
        if precio_original_elem:
            precio_texto = precio_original_elem.text.strip()
            precio_texto = precio_texto.replace('$', '').replace(',', '')
            try:
                libro['precio_original'] = float(precio_texto)
            except:
                libro['precio_original'] = None
        else:
            libro['precio_original'] = None
        
        # Valoración
        rating_elem = articulo.find('span', class_='rating')
        if rating_elem:
            rating_data = rating_elem.get('data-rating')
            libro['valoracion'] = float(rating_data) if rating_data else 0.0
        else:
            libro['valoracion'] = 0.0
        
        # Número de reseñas
        reviews_elem = articulo.find('span', class_='reviews-count')
        if reviews_elem:
            # Extraer número del texto (ej: "(234 reseñas)")
            import re
            match = re.search(r'\d+', reviews_elem.text)
            libro['num_resenas'] = int(match.group()) if match else 0
        else:
            libro['num_resenas'] = 0
        
        # Estado del stock
        stock_elem = articulo.find('span', class_='stock')
        if stock_elem:
            stock_text = stock_elem.text.lower()
            libro['en_stock'] = 'agotado' not in stock_text and 'out' not in stock_text
            
            # Extraer cantidad si está disponible
            stock_data = stock_elem.get('data-stock')
            libro['cantidad_stock'] = int(stock_data) if stock_data else 0
        else:
            libro['en_stock'] = False
            libro['cantidad_stock'] = 0
        
        # Autor
        autor_elem = articulo.find('p', class_='author')
        libro['autor'] = autor_elem.text.strip() if autor_elem else 'Autor desconocido'
        
        # Editorial
        editorial_elem = articulo.find('p', class_='publisher')
        if editorial_elem:
            # Buscar el span dentro que contiene el nombre
            span_editorial = editorial_elem.find('span')
            libro['editorial'] = span_editorial.text.strip() if span_editorial else 'Editorial desconocida'
        else:
            libro['editorial'] = 'Editorial desconocida'
        
        # ISBN (información adicional)
        libro['isbn'] = articulo.get('data-isbn', 'Sin ISBN')
        
        # Categoría
        libro['categoria'] = articulo.get('data-category', 'Sin categoría')
        
        libros.append(libro)
    
    return libros


def analizar_stock(libros: List[Dict]) -> Dict:
    """
    Analiza el estado del stock de los libros.
    """
    estadisticas = {
        'total_libros': len(libros),
        'en_stock': 0,
        'agotados': 0,
        'pocas_unidades': 0
    }
    
    for libro in libros:
        if libro['en_stock']:
            estadisticas['en_stock'] += 1
            # Verificar si quedan pocas unidades
            if libro.get('cantidad_stock', 0) < 5 and libro.get('cantidad_stock', 0) > 0:
                estadisticas['pocas_unidades'] += 1
        else:
            estadisticas['agotados'] += 1
    
    return estadisticas


def filtrar_por_categoria(libros: List[Dict], categoria: str) -> List[Dict]:
    """
    Filtra libros por categoría.
    """
    return [libro for libro in libros if libro.get('categoria', '').lower() == categoria.lower()]


def calcular_descuentos(libros: List[Dict]) -> List[Dict]:
    """
    Calcula el porcentaje de descuento para cada libro.
    """
    for libro in libros:
        if libro.get('precio_original') and libro.get('precio_actual'):
            descuento = (libro['precio_original'] - libro['precio_actual']) / libro['precio_original'] * 100
            libro['descuento_porcentaje'] = round(descuento, 1)
        else:
            libro['descuento_porcentaje'] = 0
    
    return libros


def ordenar_por_valoracion(libros: List[Dict], descendente: bool = True) -> List[Dict]:
    """
    Función adicional: Ordena los libros por valoración.
    """
    return sorted(libros, key=lambda x: x['valoracion'], reverse=descendente)


def exportar_a_csv(libros: List[Dict], nombre_archivo: str = 'libros.csv'):
    """
    Función adicional: Exporta los libros a un archivo CSV.
    """
    if not libros:
        return
    
    # Obtener todas las claves para los encabezados
    fieldnames = libros[0].keys()
    
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(libros)
    
    print(f"✅ Datos exportados a {nombre_archivo}")


def exportar_a_json(libros: List[Dict], nombre_archivo: str = 'libros.json'):
    """
    Función adicional: Exporta los libros a un archivo JSON.
    """
    with open(nombre_archivo, 'w', encoding='utf-8') as jsonfile:
        json.dump(libros, jsonfile, ensure_ascii=False, indent=2)
    
    print(f"✅ Datos exportados a {nombre_archivo}")


def generar_reporte(libros: List[Dict]) -> str:
    """
    Genera un reporte completo del scraping.
    """
    stats = analizar_stock(libros)
    libros_con_desc = calcular_descuentos(libros)
    
    # Calcular estadísticas adicionales
    precio_promedio = sum(l['precio_actual'] for l in libros) / len(libros) if libros else 0
    valoracion_promedio = sum(l['valoracion'] for l in libros) / len(libros) if libros else 0
    
    # Libro más caro y más barato
    mas_caro = max(libros, key=lambda x: x['precio_actual']) if libros else None
    mas_barato = min(libros, key=lambda x: x['precio_actual']) if libros else None
    
    # Mejor valorado
    mejor_valorado = max(libros, key=lambda x: x['valoracion']) if libros else None
    
    reporte = f"""
    ╔══════════════════════════════════════════════╗
    ║     REPORTE DE SCRAPING - CATÁLOGO DE LIBROS  ║
    ╚══════════════════════════════════════════════╝
    
    📊 ESTADÍSTICAS GENERALES
    ─────────────────────────
    📚 Total de libros: {stats['total_libros']}
    ✅ En stock: {stats['en_stock']}
    ❌ Agotados: {stats['agotados']}
    ⚠️ Pocas unidades: {stats['pocas_unidades']}
    
    💰 ANÁLISIS DE PRECIOS
    ──────────────────────
    💵 Precio promedio: ${precio_promedio:.2f}
    📈 Más caro: {mas_caro['titulo'][:30]}... (${mas_caro['precio_actual']:.2f})
    📉 Más barato: {mas_barato['titulo'][:30]}... (${mas_barato['precio_actual']:.2f})
    
    ⭐ VALORACIONES
    ───────────────
    ⭐ Valoración promedio: {valoracion_promedio:.1f}/5.0
    🏆 Mejor valorado: {mejor_valorado['titulo'][:30]}... ({mejor_valorado['valoracion']:.1f}⭐)
    
    🏷️ CATEGORÍAS
    ──────────────
    """
    
    # Contar libros por categoría
    categorias = {}
    for libro in libros:
        cat = libro.get('categoria', 'Sin categoría')
        categorias[cat] = categorias.get(cat, 0) + 1
    
    for cat, count in categorias.items():
        reporte += f"    • {cat}: {count} libros\n"
    
    # Libros con mayor descuento
    libros_con_desc_ordenados = sorted(
        [l for l in libros_con_desc if l.get('descuento_porcentaje', 0) > 0],
        key=lambda x: x['descuento_porcentaje'],
        reverse=True
    )
    
    if libros_con_desc_ordenados:
        reporte += f"""
    🎁 TOP 3 DESCUENTOS
    ───────────────────
    """
        for i, libro in enumerate(libros_con_desc_ordenados[:3], 1):
            reporte += f"    {i}. {libro['titulo'][:40]}... (-{libro['descuento_porcentaje']:.0f}%)\n"
    
    reporte += """
    ═══════════════════════════════════════════════
    """
    
    return reporte


# FUNCIÓN DE DEMOSTRACIÓN
def demo_completa():
    """
    Ejecuta una demostración completa de todas las funcionalidades.
    """
    print("\n🎯 DEMOSTRACIÓN COMPLETA DE LA SOLUCIÓN")
    print("="*50)
    
    # Cargar y procesar datos
    ruta = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'books_catalog.html')
    html = cargar_html(ruta)
    libros = extraer_libros(html)
    
    # Generar y mostrar reporte
    reporte = generar_reporte(libros)
    print(reporte)
    
    # Mostrar algunos ejemplos específicos
    print("\n📚 EJEMPLOS DE LIBROS EXTRAÍDOS:")
    print("-"*50)
    for libro in libros[:3]:
        print(f"\n📖 {libro['titulo']}")
        print(f"   Autor: {libro['autor']}")
        print(f"   Editorial: {libro['editorial']}")
        print(f"   Precio: ${libro['precio_actual']:.2f}")
        if libro.get('precio_original'):
            print(f"   Precio original: ${libro['precio_original']:.2f}")
        print(f"   Valoración: {libro['valoracion']}⭐ ({libro['num_resenas']} reseñas)")
        print(f"   Stock: {'✅ Disponible' if libro['en_stock'] else '❌ Agotado'}")
    
    # Exportar datos (opcional)
    print("\n💾 EXPORTANDO DATOS...")
    print("-"*50)
    exportar_a_csv(libros, 'catalogo_libros.csv')
    exportar_a_json(libros, 'catalogo_libros.json')
    
    print("\n✨ ¡Demostración completa finalizada!")


if __name__ == "__main__":
    demo_completa()