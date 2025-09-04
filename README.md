# 🕸️ Web Scraping con Python - Curso Completo

## 📚 Descripción del Curso

Bienvenido al curso completo de Web Scraping con Python. Este curso te llevará desde los conceptos básicos hasta técnicas avanzadas de extracción de datos web, proporcionándote las habilidades necesarias para construir scrapers robustos y eficientes.

## 🎯 Objetivos del Curso

Al finalizar este curso serás capaz de:
- Comprender la estructura HTML y cómo navegar por ella
- Dominar las bibliotecas principales de web scraping en Python
- Crear scrapers eficientes y respetuosos con los sitios web
- Procesar y almacenar datos extraídos de manera efectiva
- Implementar buenas prácticas y consideraciones éticas
- Manejar sitios web dinámicos y APIs
- Resolver problemas comunes de web scraping

## 📋 Prerrequisitos

- **Python Básico**: Conocimiento de variables, funciones, bucles y estructuras de datos
- **Terminal/Command Line**: Uso básico de la línea de comandos
- **HTML/CSS Básico**: Comprensión básica de etiquetas HTML (se repasará en el curso)

## 🚀 Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/Web-Scraping_with-Python.git
cd Web-Scraping_with-Python
```

### 2. Crear Entorno Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Iniciar Jupyter Notebook
```bash
jupyter notebook
```

## 📖 Estructura del Curso

### **Módulo 1: Fundamentos de Web Scraping**
#### 📘 [Lección 1: Introducción a Web Scraping y HTML](notebooks/01_Introduccion_Web_Scraping_HTML.ipynb)
- ¿Qué es Web Scraping?
- Aplicaciones y casos de uso
- Estructura HTML y DOM
- Herramientas del desarrollador en el navegador
- Tu primer scraper con urllib

#### 📘 [Lección 2: HTTP Requests y Beautiful Soup](notebooks/02_HTTP_Requests_BeautifulSoup.ipynb)
- Protocolo HTTP y métodos de petición
- Biblioteca requests
- Introducción a Beautiful Soup
- Navegación por el árbol HTML
- Búsqueda y extracción de elementos

### **Módulo 2: Técnicas de Selección Avanzadas**
#### 📘 [Lección 3: XPath y Técnicas de Selección](notebooks/03_XPath_Seleccion_Avanzada.ipynb)
- Sintaxis XPath completa
- Expresiones y funciones XPath
- Selección por atributos y contenido
- XPath vs CSS Selectors
- Casos de uso avanzados

#### 📘 [Lección 4: CSS Selectors y Métodos de Encadenamiento](notebooks/04_CSS_Selectors_Chaining.ipynb)
- Sintaxis de CSS Selectors
- Selectores complejos y pseudo-clases
- Combinación de selectores
- Encadenamiento de métodos
- Optimización de selectores

### **Módulo 3: Framework Scrapy**
#### 📘 [Lección 5: Introducción a Scrapy](notebooks/05_Introduccion_Scrapy.ipynb)
- Arquitectura de Scrapy
- Instalación y configuración
- Creación de proyectos
- Items y pipelines
- Configuración y settings

#### 📘 [Lección 6: Construcción de Spiders Avanzados](notebooks/06_Spiders_Avanzados.ipynb)
- Tipos de spiders
- Seguimiento de enlaces
- Manejo de paginación
- Procesamiento paralelo
- Middlewares personalizados

### **Módulo 4: Procesamiento y Almacenamiento**
#### 📘 [Lección 7: Procesamiento y Almacenamiento de Datos](notebooks/07_Procesamiento_Almacenamiento.ipynb)
- Limpieza de datos
- Validación y normalización
- Exportación a diferentes formatos (CSV, JSON, Excel)
- Bases de datos (SQLite, PostgreSQL, MongoDB)
- Data pipelines

### **Módulo 5: Consideraciones Avanzadas**
#### 📘 [Lección 8: Ética, Robots.txt y Mejores Prácticas](notebooks/08_Etica_Mejores_Practicas.ipynb)
- Aspectos legales y éticos
- Robots.txt y políticas de uso
- Rate limiting y throttling
- User agents y headers
- Manejo de errores y reintentos
- Detección y evasión de anti-scraping

## 🛠️ Tecnologías y Herramientas

### Bibliotecas Principales
- **requests**: Para realizar peticiones HTTP
- **Beautiful Soup 4**: Parser HTML/XML
- **Scrapy**: Framework completo de web scraping
- **lxml**: Parser XML/HTML rápido
- **Selenium**: Para sitios web dinámicos

### Bibliotecas de Apoyo
- **pandas**: Manipulación de datos
- **numpy**: Operaciones numéricas
- **matplotlib/seaborn**: Visualización
- **SQLAlchemy**: ORM para bases de datos
- **pymongo**: Cliente MongoDB

## 💻 Ejercicios y Proyectos

### Ejercicios por Lección
Cada notebook incluye ejercicios prácticos con diferentes niveles de dificultad:
- 🟢 **Básico**: Ejercicios guiados paso a paso
- 🟡 **Intermedio**: Ejercicios con menor guía
- 🔴 **Avanzado**: Desafíos para aplicar múltiples conceptos

### Proyectos Finales
1. **E-commerce Scraper**: Extraer información de productos de un sitio de comercio electrónico
2. **News Aggregator**: Recopilar noticias de múltiples fuentes
3. **Job Board Monitor**: Monitorear ofertas de trabajo y crear alertas
4. **Social Media Analytics**: Analizar tendencias en redes sociales
5. **Real Estate Tracker**: Seguimiento de precios inmobiliarios

## 📊 Datasets de Práctica

La carpeta `data/` contiene HTML de ejemplo y sitios web de práctica para que puedas experimentar sin afectar sitios reales:
- `sample_ecommerce.html`: Sitio de e-commerce ficticio
- `news_portal.html`: Portal de noticias de ejemplo
- `job_listings.html`: Listados de trabajo simulados

## 🤝 Contribuciones

Las contribuciones son bienvenidas! Por favor:
1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Recursos Adicionales

### Documentación Oficial
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Scrapy Documentation](https://docs.scrapy.org/)
- [Requests Documentation](https://requests.readthedocs.io/)
- [XPath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)

### Sitios de Práctica
- [Quotes to Scrape](http://quotes.toscrape.com/)
- [Books to Scrape](http://books.toscrape.com/)
- [Scrape This Site](https://scrapethissite.com/)

### Herramientas Útiles
- [XPath Tester](https://www.freeformatter.com/xpath-tester.html)
- [CSS Selector Tester](https://www.w3schools.com/cssref/trysel.asp)
- [Regex101](https://regex101.com/)
- [Postman](https://www.postman.com/)

## ⚠️ Aviso Legal

Este curso es únicamente con fines educativos. Siempre:
- Respeta los términos de servicio de los sitios web
- Implementa rate limiting apropiado
- Considera usar APIs cuando estén disponibles
- Solicita permiso cuando sea necesario

## 📧 Contacto y Soporte

Si tienes preguntas o encuentras problemas:
- Escríbeme en [Linkedin](www.linkedin.com/in/mendezgasca)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

⭐ **¡No olvides dar una estrella al repositorio si te resulta útil!** ⭐

Última actualización: Agosto 2025