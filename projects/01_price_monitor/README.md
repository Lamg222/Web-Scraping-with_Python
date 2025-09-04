# 💰 Monitor de Precios E-commerce

Un sistema completo para monitorear precios de productos en múltiples tiendas online, con alertas automáticas, visualizaciones y análisis de tendencias.

## 🎯 Características principales

- 🛒 **Multi-tienda**: Monitorea Amazon, eBay, MercadoLibre y más
- 📊 **Dashboard web**: Interfaz intuitiva con gráficos interactivos
- 📧 **Alertas inteligentes**: Notificaciones por email cuando hay ofertas
- 🗄️ **Base de datos**: Almacenamiento histórico con SQLite
- ⏰ **Automatización**: Ejecución programada con cron/scheduler
- 📈 **Análisis**: Tendencias de precios y predicciones simples

## 🔧 Instalación

### Requisitos previos
- Python 3.8+
- pip (gestor de paquetes de Python)
- Cuenta de email para notificaciones (opcional)

### Pasos de instalación

1. **Clonar el repositorio**:
```bash
git clone https://github.com/tu-usuario/price-monitor.git
cd price-monitor
```

2. **Crear entorno virtual**:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**:
```bash
cp .env.example .env
# Edita .env con tus configuraciones
```

5. **Inicializar base de datos**:
```bash
python src/database.py --init
```

## ⚙️ Configuración

### Archivo `.env`
```env
# Configuración de email
EMAIL_USER=tu-email@gmail.com
EMAIL_PASSWORD=tu-contraseña-app
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=587

# Configuración de scraping
SCRAPING_DELAY=2
USER_AGENT=Mozilla/5.0 (compatible; PriceMonitor/1.0)
TIMEOUT=30

# Base de datos
DATABASE_URL=sqlite:///data/prices.db

# Dashboard
DASHBOARD_HOST=localhost
DASHBOARD_PORT=5000
```

### Configuración de productos
Edita `config/products.json`:
```json
{
  "products": [
    {
      "name": "iPhone 15 Pro",
      "urls": [
        "https://amazon.com/dp/XXXXXXX",
        "https://ebay.com/itm/XXXXXXX"
      ],
      "target_price": 999.99,
      "alert_threshold": 0.1
    }
  ]
}
```

## 🚀 Uso

### 1. Ejecutar scraping manual
```bash
python main.py --scrape
```

### 2. Iniciar dashboard web
```bash
python main.py --dashboard
```
Visita http://localhost:5000

### 3. Configurar ejecución automática
```bash
# Ejecutar cada hora
python main.py --schedule --interval=3600
```

### 4. Enviar reporte por email
```bash
python main.py --report --email=destino@email.com
```

## 📊 Estructura del proyecto

```
01_price_monitor/
├── README.md                 # Este archivo
├── requirements.txt          # Dependencias Python
├── .env.example             # Plantilla de configuración
├── main.py                  # Punto de entrada principal
├── config/
│   ├── products.json        # Productos a monitorear
│   └── settings.py          # Configuraciones del sistema
├── src/
│   ├── __init__.py
│   ├── scraper.py           # Lógica de scraping
│   ├── database.py          # Manejo de base de datos
│   ├── dashboard.py         # Interface web con Flask
│   ├── alerts.py            # Sistema de alertas
│   ├── analyzer.py          # Análisis de tendencias
│   └── utils.py             # Funciones auxiliares
├── data/
│   ├── prices.db            # Base de datos SQLite (se crea automáticamente)
│   └── logs/                # Archivos de log
├── templates/               # Plantillas HTML del dashboard
│   ├── base.html
│   ├── dashboard.html
│   └── product_detail.html
├── static/                  # Archivos estáticos (CSS, JS)
│   ├── css/
│   ├── js/
│   └── images/
├── tests/
│   ├── test_scraper.py
│   ├── test_database.py
│   └── test_alerts.py
└── docs/
    ├── api.md               # Documentación de API
    ├── deployment.md        # Guía de despliegue
    └── troubleshooting.md   # Solución de problemas
```

## 🛠️ Componentes principales

### 1. Scraper (`src/scraper.py`)
- Extrae precios de múltiples tiendas
- Manejo robusto de errores y timeouts
- Rotación de user-agents
- Soporte para JavaScript con Selenium (opcional)

### 2. Base de datos (`src/database.py`)
- Esquema optimizado para histórico de precios
- Índices para consultas rápidas
- Funciones de limpieza y mantenimiento

### 3. Dashboard (`src/dashboard.py`)
- Interface web con Flask
- Gráficos interactivos con Plotly
- Tablas responsivas
- Filtros y búsqueda

### 4. Sistema de alertas (`src/alerts.py`)
- Alertas por email con plantillas HTML
- Múltiples criterios de alerta
- Rate limiting para evitar spam

## 📈 Casos de uso

### Caso 1: Monitor personal
```python
from src.scraper import PriceScraper
from src.database import PriceDB

# Configurar productos a monitorear
products = [
    {
        'name': 'Laptop Gaming',
        'url': 'https://amazon.com/dp/B08N5WRWNW',
        'target_price': 1200.00
    }
]

# Inicializar scraper
scraper = PriceScraper()
db = PriceDB()

# Scraping y guardado
for product in products:
    price_data = scraper.scrape_price(product['url'])
    db.save_price(product['name'], price_data)
```

### Caso 2: Análisis de tendencias
```python
from src.analyzer import PriceAnalyzer
import matplotlib.pyplot as plt

analyzer = PriceAnalyzer()
trends = analyzer.get_price_trends('iPhone 15 Pro', days=30)

# Visualizar tendencias
plt.figure(figsize=(12, 6))
plt.plot(trends['dates'], trends['prices'])
plt.title('Tendencia de precios - iPhone 15 Pro')
plt.xlabel('Fecha')
plt.ylabel('Precio ($)')
plt.show()
```

### Caso 3: Alertas automáticas
```python
from src.alerts import AlertSystem

alert_system = AlertSystem()

# Configurar alerta
alert_system.add_alert(
    product='MacBook Pro M3',
    condition='price_below',
    threshold=2000.00,
    email='mi-email@gmail.com'
)

# Verificar alertas
alert_system.check_all_alerts()
```

## 🧪 Testing

Ejecutar todos los tests:
```bash
python -m pytest tests/ -v
```

Ejecutar tests específicos:
```bash
# Test del scraper
python -m pytest tests/test_scraper.py -v

# Test de la base de datos
python -m pytest tests/test_database.py -v

# Test con cobertura
python -m pytest tests/ --cov=src --cov-report=html
```

## 🚀 Despliegue

### Opción 1: Servidor local
```bash
# Usar gunicorn para producción
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 src.dashboard:app
```

### Opción 2: Docker
```bash
# Construir imagen
docker build -t price-monitor .

# Ejecutar contenedor
docker run -p 5000:5000 -v $(pwd)/data:/app/data price-monitor
```

### Opción 3: Cloud (Heroku)
```bash
# Instalar Heroku CLI
pip install heroku3

# Desplegar
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

## 📊 Dashboard Screenshots

### Vista principal
![Dashboard principal](docs/screenshots/dashboard-main.png)

### Detalle de producto
![Detalle de producto](docs/screenshots/product-detail.png)

### Análisis de tendencias
![Análisis de tendencias](docs/screenshots/trends-analysis.png)

## 🔧 Personalización

### Agregar nueva tienda
1. Crear clase scraper en `src/scrapers/`:
```python
class NuevaTiendaScraper(BaseScraper):
    def extract_price(self, soup):
        # Lógica específica de extracción
        pass
```

2. Registrar en `src/scraper.py`:
```python
SCRAPERS = {
    'nuevatienda.com': NuevaTiendaScraper,
    # ... otros scrapers
}
```

### Personalizar alertas
```python
# En src/alerts.py
class CustomAlert(BaseAlert):
    def should_trigger(self, price_data):
        # Lógica personalizada
        return your_custom_logic(price_data)
```

## 🐛 Troubleshooting

### Error: "No se puede conectar a la tienda"
- Verificar conexión a internet
- Revisar si la tienda bloquea bots
- Usar proxies o VPN si es necesario

### Error: "Base de datos bloqueada"
- Cerrar otras conexiones a la DB
- Reiniciar la aplicación
- Verificar permisos del archivo

### Dashboard no carga
- Verificar puerto 5000 disponible
- Revisar logs en `data/logs/`
- Comprobar variables de entorno

## 📋 Roadmap

### Versión 2.0
- [ ] Soporte para más tiendas (AliExpress, Walmart)
- [ ] Alertas por Telegram/WhatsApp
- [ ] Machine Learning para predicción de precios
- [ ] API REST completa
- [ ] App móvil

### Versión 2.1
- [ ] Soporte para criptomonedas
- [ ] Integración con Google Sheets
- [ ] Sistema de usuarios múltiples
- [ ] Webhooks para integraciones

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!

1. Fork el proyecto
2. Crear branch para feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👥 Créditos

- **Scraping**: BeautifulSoup, Selenium
- **Web Framework**: Flask
- **Gráficos**: Plotly.js
- **Base de datos**: SQLite
- **Alertas**: smtplib
- **Styling**: Bootstrap 5

## 📞 Soporte

- 📧 Email: soporte@pricemonitor.com
- 🐛 Issues: [GitHub Issues](https://github.com/tu-usuario/price-monitor/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/tu-usuario/price-monitor/discussions)

---

**¡Feliz monitoreo de precios! 💰📊**