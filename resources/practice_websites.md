# 🌐 Sitios Web Para Practicar Web Scraping

Una lista curada de sitios web seguros y éticos donde puedes practicar técnicas de web scraping.

## 🎯 Sitios Específicamente para Scraping

### 📚 Principiantes - Contenido Estático

#### [Quotes to Scrape](http://quotes.toscrape.com/)
- **URL**: http://quotes.toscrape.com/
- **Nivel**: 🟢 Principiante
- **Contenido**: Citas famosas con autor y tags
- **Técnicas a practicar**:
  - Extracción básica de texto
  - Navegación por páginas
  - Manejo de atributos
  - CSS selectors y XPath

```python
# Ejemplo rápido
import requests
from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(response.content, 'html.parser')

for quote in soup.find_all('div', class_='quote'):
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f"{text} - {author}")
```

#### [Books to Scrape](http://books.toscrape.com/)
- **URL**: http://books.toscrape.com/
- **Nivel**: 🟢 Principiante
- **Contenido**: Catálogo de libros con precios y valoraciones
- **Técnicas a practicar**:
  - Extracción de productos
  - Manejo de precios y números
  - Navegación por categorías
  - Paginación

#### [Scrape This Site](https://scrapethissite.com/)
- **URL**: https://scrapethissite.com/
- **Nivel**: 🟢 Principiante a 🟡 Intermedio
- **Contenido**: Múltiples sandboxes temáticos
- **Sandboxes incluidos**:
  - Países del mundo
  - Hockey teams
  - Oscar winning films
  - Turtle racing

### 🔧 Intermedios - Contenido Dinámico

#### [ToScrape with JavaScript](http://quotes.toscrape.com/js/)
- **URL**: http://quotes.toscrape.com/js/
- **Nivel**: 🟡 Intermedio
- **Contenido**: Versión JavaScript de Quotes to Scrape
- **Técnicas a practicar**:
  - Selenium WebDriver
  - Esperas dinámicas
  - Manejo de AJAX

#### [Infinite Scroll](http://quotes.toscrape.com/scroll)
- **URL**: http://quotes.toscrape.com/scroll
- **Nivel**: 🟡 Intermedio
- **Contenido**: Scroll infinito con carga dinámica
- **Técnicas a practicar**:
  - Scroll automatizado
  - Detección de carga de contenido
  - APIs de JavaScript

### 🎓 Avanzados - Desafíos Complejos

#### [Login Required](http://quotes.toscrape.com/login)
- **URL**: http://quotes.toscrape.com/login
- **Nivel**: 🔴 Avanzado
- **Contenido**: Contenido que requiere autenticación
- **Técnicas a practicar**:
  - Manejo de sesiones
  - Formularios de login
  - Cookies y autenticación

## 🏪 E-commerce y Productos (Para uso educativo únicamente)

### Sitios que permiten scraping educativo

#### [Fake Store API](https://fakestoreapi.com/)
- **URL**: https://fakestoreapi.com/
- **Tipo**: API REST (no scraping requerido)
- **Contenido**: Productos ficticios de e-commerce
- **Uso**: Practicar consumo de APIs

#### [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
- **URL**: https://jsonplaceholder.typicode.com/
- **Tipo**: API REST de prueba
- **Contenido**: Posts, usuarios, comentarios ficticios
- **Uso**: Practicar consumo de APIs REST

## 📰 Noticias y Blogs

### ⚠️ IMPORTANTE: Siempre revisar robots.txt y términos de uso

#### [Hacker News](https://news.ycombinator.com/)
- **URL**: https://news.ycombinator.com/
- **Contenido**: Noticias de tecnología
- **robots.txt**: Permitido para bots educativos
- **Técnicas a practicar**:
  - Extracción de títulos y enlaces
  - Manejo de votaciones
  - Navegación por páginas

#### [Reddit (públic content)](https://www.reddit.com/)
- **URL**: https://www.reddit.com/
- **API**: https://www.reddit.com/dev/api/
- **Recomendación**: Usar la API oficial
- **Técnicas**: Autenticación OAuth, rate limiting

## 🏛️ Datos Gubernamentales

#### [Data.gov](https://www.data.gov/)
- **URL**: https://www.data.gov/
- **Contenido**: Datasets gubernamentales de EE.UU.
- **Formato**: Principalmente CSV y JSON
- **Uso**: Más para descarga directa que scraping

#### [OpenData de la UE](https://data.europa.eu/)
- **URL**: https://data.europa.eu/
- **Contenido**: Datos abiertos europeos
- **Formato**: Múltiples formatos

## 🎭 Sitios de Testing Local

### Para configurar en tu entorno local

#### [HTTP Testing Service](https://httpbin.org/)
- **URL**: https://httpbin.org/
- **Uso**: Testing de requests HTTP
- **Características**: Endpoints para probar headers, cookies, etc.

```python
# Ejemplos de uso
requests.get('https://httpbin.org/html')     # HTML simple
requests.get('https://httpbin.org/json')     # Respuesta JSON
requests.get('https://httpbin.org/xml')      # Respuesta XML
```

#### [MockAPI](https://mockapi.io/)
- **URL**: https://mockapi.io/
- **Uso**: Crear APIs de prueba personalizadas
- **Características**: Datos ficticios personalizables

## 🧪 Entornos de Sandbox

### Sitios para experimentar sin restricciones

#### [Scrapy Playground](https://scrapy.org/doc/)
- **Documentación oficial**: https://docs.scrapy.org/
- **Tutoriales**: Incluye spiders de ejemplo
- **Uso**: Seguir tutoriales oficiales

#### [Selenium Testing Playground](https://the-internet.herokuapp.com/)
- **URL**: https://the-internet.herokuapp.com/
- **Contenido**: Varios casos de testing web
- **Casos incluidos**:
  - Login forms
  - Dropdown lists
  - Dynamic loading
  - File uploads
  - Hovers
  - Frames

## 📱 APIs Públicas (Alternativa al Scraping)

### Cuando el scraping no es necesario

#### [Public APIs](https://github.com/public-apis/public-apis)
- **GitHub**: Lista masiva de APIs públicas
- **Categorías**: Múltiples categorías disponibles
- **Uso**: Alternativa mejor que el scraping

#### [API List](https://apilist.fun/)
- **URL**: https://apilist.fun/
- **Contenido**: APIs categorizadas y curadas
- **Filtros**: Por categoría, autenticación, CORS, etc.

## ⚖️ Consideraciones Legales y Éticas

### ✅ Buenas prácticas

1. **Revisar robots.txt**
   ```
   https://sitio-web.com/robots.txt
   ```

2. **Leer términos de servicio**
   - Buscar secciones sobre scraping/automation
   - Respetar restricciones

3. **Implementar rate limiting**
   ```python
   import time
   time.sleep(1)  # Pausa entre requests
   ```

4. **Usar User-Agent apropiado**
   ```python
   headers = {
       'User-Agent': 'Mozilla/5.0 (Educational Bot)'
   }
   ```

### ❌ Evitar

- Scraping de sitios que lo prohíben explícitamente
- Sobrecargar servidores con requests masivos
- Scraping de datos personales sin permiso
- Violación de derechos de autor

## 🛠️ Herramientas de Desarrollo

### Para probar selectores

#### [CSS Selector Tester](https://www.w3schools.com/cssref/trysel.asp)
- Probar selectores CSS online

#### [XPath Tester](https://www.freeformatter.com/xpath-tester.html)
- Probar expresiones XPath

#### [Regex101](https://regex101.com/)
- Probar expresiones regulares

## 📚 Conjuntos de Datos para Práctica

### Datasets estáticos

#### [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)
- **GitHub**: Lista curada de datasets públicos
- **Formato**: CSV, JSON, XML
- **Uso**: Practicar procesamiento de datos

#### [Kaggle Datasets](https://www.kaggle.com/datasets)
- **URL**: https://www.kaggle.com/datasets
- **Contenido**: Miles de datasets
- **Formato**: Principalmente CSV
- **Uso**: Análisis de datos post-scraping

## 🏆 Desafíos Progresivos

### Nivel 1: Principiante
1. Extraer todas las citas de quotes.toscrape.com
2. Crear un CSV con libros de books.toscrape.com
3. Obtener datos de países de scrapethissite.com

### Nivel 2: Intermedio
1. Scraping con paginación automática
2. Manejo de formularios simples
3. Extracción de datos de tablas complejas

### Nivel 3: Avanzado
1. Scraping de contenido con JavaScript
2. Manejo de autenticación
3. Scraping distribuido/concurrente

## 💡 Consejos Pro

1. **Empezar simple**: Comienza con sitios estáticos
2. **Usar herramientas del navegador**: DevTools para inspeccionar
3. **Probar selectores**: Usar console del navegador
4. **Documentar hallazgos**: Guardar patrones útiles
5. **Respetar límites**: No sobrecargar servidores

## 📞 Recursos de Ayuda

- **Stack Overflow**: Tag `web-scraping`
- **Reddit**: r/webscraping
- **Discord**: Servers de Python y web scraping
- **GitHub**: Repositorios de ejemplo

---

⚠️ **Disclaimer**: Siempre verifica la legalidad y términos de uso antes de hacer scraping de cualquier sitio web. Esta lista es solo para propósitos educativos.