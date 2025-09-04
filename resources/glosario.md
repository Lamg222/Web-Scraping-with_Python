# 📚 Glosario de Web Scraping

Un diccionario completo de términos, conceptos y acrónimos utilizados en web scraping y tecnologías relacionadas.

---

## A

### **API (Application Programming Interface)**
Conjunto de reglas y protocolos que permite a diferentes aplicaciones comunicarse entre sí. En web scraping, las APIs son preferibles al scraping cuando están disponibles.

### **AJAX (Asynchronous JavaScript and XML)**
Tecnología que permite a las páginas web actualizar contenido dinámicamente sin recargar toda la página. Complica el web scraping tradicional ya que el contenido se carga después del HTML inicial.

### **Anti-bot**
Medidas técnicas implementadas por sitios web para detectar y bloquear bots automatizados, incluyendo scrapers.

### **Atributo HTML**
Información adicional asociada a elementos HTML (ej: `class`, `id`, `href`, `data-*`). Son fundamentales para localizar elementos durante el scraping.

### **Autenticación**
Proceso de verificar la identidad de un usuario o bot. En web scraping puede incluir login con credenciales, tokens API, o cookies de sesión.

---

## B

### **BeautifulSoup**
Biblioteca de Python para parsear documentos HTML y XML. Una de las herramientas más populares para web scraping básico e intermedio.

### **Bot**
Programa automatizado que realiza tareas repetitivas en internet. Los web scrapers son un tipo específico de bot.

### **Browser Engine**
Motor que renderiza páginas web (ej: Chromium, Gecko, WebKit). Selenium usa estos motores para scraping de contenido dinámico.

---

## C

### **CAPTCHA (Completely Automated Public Turing test)**
Sistema de desafío-respuesta para determinar si el usuario es humano. Método común anti-bot que complica el scraping automatizado.

### **Cookies**
Pequeños archivos de texto que los sitios web almacenan en el navegador para recordar información. Importantes para mantener sesiones en scraping.

### **Crawling**
Proceso sistemático de navegar y explorar sitios web siguiendo enlaces. Diferente del scraping, que se enfoca en extraer datos específicos.

### **CSS Selectors**
Patrones utilizados para seleccionar elementos HTML basados en sus atributos, posición o relaciones. Ejemplo: `.class`, `#id`, `div > p`.

### **CSRF (Cross-Site Request Forgery)**
Tipo de ataque web. Los tokens CSRF protegen formularios y pueden requerir manejo especial en scraping.

---

## D

### **DOM (Document Object Model)**
Representación estructurada de un documento HTML como árbol jerárquico. Los scrapers navegan por el DOM para extraer datos.

### **Dynamic Content**
Contenido web generado o modificado por JavaScript después de que se carga la página inicial. Requiere herramientas como Selenium para ser scrapeado.

---

## E

### **Encoding**
Sistema para representar caracteres de texto (ej: UTF-8, ISO-8859-1). Importante para manejar correctamente caracteres especiales en diferentes idiomas.

### **Endpoint**
URL específica de una API que acepta requests y devuelve datos. En scraping, preferible a extraer datos directamente del HTML.

---

## F

### **Forms**
Elementos HTML que permiten a usuarios enviar datos. En scraping pueden requerir manejo especial para envío de información.

### **Framework**
Conjunto de herramientas y librerías que facilitan el desarrollo. Scrapy es un framework específico para web scraping.

---

## G

### **GET Request**
Método HTTP para solicitar datos de un servidor. El tipo más común de request en web scraping básico.

### **GDPR (General Data Protection Regulation)**
Regulación europea sobre protección de datos personales que afecta el scraping de información de ciudadanos de la UE.

---

## H

### **Headers HTTP**
Metadatos que acompañan requests y responses HTTP. Incluyen información como User-Agent, cookies, y tipo de contenido.

### **HTML (HyperText Markup Language)**
Lenguaje de marcado estándar para crear páginas web. Los scrapers parsean HTML para extraer información estructurada.

### **HTTP Status Codes**
Códigos numéricos que indican el resultado de un request HTTP:
- 200: Éxito
- 404: No encontrado
- 429: Too Many Requests
- 403: Prohibido

---

## I

### **iframe**
Elemento HTML que incrusta otra página web dentro de la actual. Puede complicar el scraping ya que el contenido está en un contexto diferente.

### **IP Blocking**
Técnica anti-bot que bloquea direcciones IP específicas después de detectar comportamiento sospechoso.

---

## J

### **JavaScript**
Lenguaje de programación que permite interactividad en páginas web. Sitios con mucho JavaScript requieren herramientas especiales para scraping.

### **JSON (JavaScript Object Notation)**
Formato ligero de intercambio de datos. Muchas APIs devuelven datos en JSON, más fácil de procesar que HTML.

---

## L

### **Latency**
Tiempo de retraso entre enviar un request y recibir la respuesta. Factor importante en la eficiencia del scraping.

### **Logging**
Registro sistemático de eventos durante la ejecución. Esencial para debugging y monitoreo de scrapers.

---

## M

### **Middleware**
Componente que procesa requests/responses entre el scraper y el sitio web. En Scrapy, permite implementar funcionalidades como proxies y rate limiting.

### **Mock Data**
Datos ficticios utilizados para testing. Útiles para probar scrapers sin hacer requests reales.

---

## N

### **NoSQL**
Tipo de base de datos no relacional. Útil para almacenar datos no estructurados obtenidos por scraping.

---

## O

### **OAuth**
Protocolo de autorización que permite acceso seguro a APIs. Alternativa segura al scraping para datos de servicios como Twitter o Facebook.

---

## P

### **Pagination**
División de contenido en múltiples páginas. Scrapers deben manejar paginación para obtener datos completos.

### **Parser**
Componente que analiza y estructura datos de texto (como HTML). BeautifulSoup incluye varios parsers (html.parser, lxml, html5lib).

### **POST Request**
Método HTTP para enviar datos al servidor. Usado en formularios y a menudo requerido para acceder a contenido específico.

### **Proxy**
Servidor intermediario entre el scraper y el sitio objetivo. Usado para ocultar IP real y evitar bloqueos.

---

## Q

### **Query Parameters**
Parámetros añadidos a URLs para modificar el contenido devuelto (ej: `?page=2&limit=10`). Importantes para navegar APIs y sitios dinámicos.

---

## R

### **Rate Limiting**
Técnica para controlar la frecuencia de requests. Implementada tanto por scrapers (para ser respetuosos) como por sitios web (para protección).

### **Regex (Regular Expressions)**
Patrones para buscar y extraer texto específico. Útil para limpiar y procesar datos extraídos.

### **robots.txt**
Archivo que especifica qué partes de un sitio web pueden ser accedidas por bots. Ubicado en `/robots.txt` de la raíz del sitio.

---

## S

### **Scrapy**
Framework de Python especializado para web scraping a gran escala. Incluye manejo de concurrencia, middlewares, y pipelines.

### **Scraping**
Proceso de extraer datos de sitios web de forma automatizada.

### **Selenium**
Herramienta que automatiza navegadores web. Permite scraping de contenido JavaScript y simulación de interacciones de usuario.

### **Session**
Estado persistente entre múltiples requests HTTP. Importante para mantener login y cookies durante scraping.

### **SPA (Single Page Application)**
Aplicación web que carga dinámicamente contenido sin cambiar de página. Complica el scraping tradicional.

---

## T

### **Tags HTML**
Elementos estructurales de HTML (ej: `<div>`, `<p>`, `<a>`). Los scrapers buscan tags específicos para extraer información.

### **Timeout**
Tiempo máximo de espera para una operación. Importante configurar timeouts apropiados para evitar que scrapers se cuelguen.

---

## U

### **URL (Uniform Resource Locator)**
Dirección web que identifica recursos en internet. Los scrapers navegan por URLs para acceder a diferentes contenidos.

### **User-Agent**
String que identifica el navegador o cliente haciendo el request. Scrapers deben usar User-Agents realistas para evitar detección.

---

## V

### **Virtual Environment**
Entorno aislado de Python que permite instalar dependencias específicas sin afectar el sistema global.

---

## W

### **Web Driver**
Interfaz que permite control programático de navegadores web. Usado por Selenium para automatizar acciones de usuario.

---

## X

### **XML (eXtensible Markup Language)**
Formato de marcado estructurado similar a HTML. Algunos sitios devuelven datos en XML que debe ser parseado.

### **XPath (XML Path Language)**
Lenguaje para seleccionar nodos en documentos XML/HTML usando rutas tipo filesystem. Más potente que CSS selectors para navegación compleja.

---

## Términos Técnicos Específicos

### **Backoff**
Estrategia de incrementar gradualmente los delays entre requests después de errores o rate limiting.

### **Circuit Breaker**
Patrón que detiene temporalmente requests a un servicio que está fallando para evitar sobrecarga.

### **ETL (Extract, Transform, Load)**
Proceso de extracción, transformación y carga de datos. Web scraping es típicamente la fase de extracción.

### **Headless Browser**
Navegador que opera sin interfaz gráfica. Más eficiente para scraping ya que no renderiza elementos visuales.

### **Pipeline**
Serie de procesadores que transforman datos secuencialmente. En Scrapy, los pipelines procesan items extraídos.

### **Spider**
En Scrapy, clase que define cómo extraer datos de un sitio específico. Cada spider maneja un dominio o tipo de contenido.

---

## Códigos de Estado HTTP Importantes

- **200 OK**: Request exitoso
- **301/302**: Redirección permanente/temporal
- **403 Forbidden**: Acceso prohibido
- **404 Not Found**: Página no encontrada
- **429 Too Many Requests**: Rate limit excedido
- **500 Internal Server Error**: Error del servidor
- **503 Service Unavailable**: Servicio no disponible

---

## Extensiones de Archivo Comunes

- **.py**: Archivo Python
- **.html/.htm**: Documento HTML
- **.xml**: Documento XML
- **.json**: Datos en formato JSON
- **.csv**: Datos separados por comas
- **.log**: Archivo de registro
- **.db/.sqlite**: Base de datos SQLite

---

## Bibliotecas de Python Relacionadas

### **Core Scraping**
- `requests`: HTTP requests
- `beautifulsoup4`: Parsing HTML/XML
- `lxml`: Parser XML/HTML rápido
- `scrapy`: Framework completo
- `selenium`: Automatización de navegador

### **Procesamiento de Datos**
- `pandas`: Análisis de datos
- `numpy`: Computación numérica
- `json`: Manejo de JSON
- `csv`: Manejo de CSV
- `re`: Expresiones regulares

### **Base de Datos**
- `sqlite3`: SQLite (incluida en Python)
- `pymongo`: MongoDB
- `sqlalchemy`: ORM para bases de datos relacionales

### **Utilidades**
- `time`: Manejo de tiempo y delays
- `random`: Generación de números aleatorios
- `logging`: Sistema de logging
- `urllib`: Utilidades de URL
- `fake-useragent`: User agents aleatorios

---

## Patrones de Diseño Comunes

### **Singleton Pattern**
Un scraper que mantiene una única conexión de base de datos.

### **Factory Pattern**
Crear diferentes tipos de scrapers basados en el dominio objetivo.

### **Observer Pattern**
Notificar cuando se extraen ciertos tipos de datos.

### **Strategy Pattern**
Diferentes estrategias de scraping para diferentes tipos de sitios.

---

## Métricas de Rendimiento

### **Throughput**
Número de páginas/items procesados por unidad de tiempo.

### **Success Rate**
Porcentaje de requests exitosos vs totales.

### **Response Time**
Tiempo promedio para completar un request.

### **Error Rate**
Porcentaje de requests que resultan en error.

---

Este glosario se actualiza regularmente con nuevos términos y conceptos. ¿Encontraste un término que no está incluido? ¡Contribuye al glosario!