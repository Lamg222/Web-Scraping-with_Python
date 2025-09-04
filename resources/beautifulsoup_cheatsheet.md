# 🍲 Beautiful Soup Cheat Sheet

## 📥 Importación y Configuración

```python
from bs4 import BeautifulSoup
import requests

# Crear objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Parsers disponibles
soup = BeautifulSoup(html, 'html.parser')    # Incluido en Python
soup = BeautifulSoup(html, 'lxml')           # Más rápido
soup = BeautifulSoup(html, 'html5lib')       # Más tolerante a errores
```

## 🔍 Métodos de Búsqueda

### find() - Primer elemento
```python
# Por etiqueta
soup.find('h1')
soup.find('div')

# Por atributos
soup.find('div', class_='container')
soup.find('div', id='main')
soup.find('a', href='https://example.com')

# Múltiples atributos
soup.find('div', {'class': 'post', 'id': 'article1'})

# Con función personalizada
soup.find('div', class_=lambda x: x and 'post' in x)
```

### find_all() - Todos los elementos
```python
# Todos los elementos de un tipo
soup.find_all('p')
soup.find_all('a')

# Con límite
soup.find_all('p', limit=5)

# Por múltiples etiquetas
soup.find_all(['h1', 'h2', 'h3'])

# Con atributos
soup.find_all('div', class_='article')
soup.find_all('img', src=True)  # Que tengan atributo src
```

## 🎯 Selectores CSS

```python
# Selector básico
soup.select('p')              # Todas las etiquetas p
soup.select('.class-name')    # Por clase
soup.select('#element-id')    # Por ID

# Selectores combinados
soup.select('div p')          # p dentro de div
soup.select('div > p')        # p hijo directo de div
soup.select('h1 + p')         # p inmediatamente después de h1
soup.select('h1 ~ p')         # todos los p hermanos después de h1

# Pseudo-selectores
soup.select('li:first-child')    # Primer li hijo
soup.select('li:last-child')     # Último li hijo
soup.select('li:nth-child(2)')   # Segundo li hijo

# Selectores de atributos
soup.select('a[href]')              # Enlaces con href
soup.select('img[alt*="logo"]')     # img cuyo alt contenga "logo"
soup.select('a[href^="https"]')     # Enlaces que empiecen con https
soup.select('a[href$=".pdf"]')      # Enlaces que terminen en .pdf
```

## 📝 Extracción de Contenido

### Texto
```python
element = soup.find('h1')
element.text                  # Texto limpio
element.get_text()           # Texto con separadores personalizados
element.get_text(strip=True) # Texto sin espacios extra
element.string               # Solo si es texto directo (sin hijos)

# Texto de múltiples elementos
texts = [p.text for p in soup.find_all('p')]
```

### Atributos
```python
element = soup.find('a')
element.get('href')          # Obtener atributo href
element['href']              # Forma alternativa
element.attrs                # Diccionario con todos los atributos

# Verificar si existe un atributo
if element.has_attr('class'):
    print(element['class'])
```

### HTML
```python
element.prettify()           # HTML formateado
str(element)                 # HTML como string
element.decode()             # Decodificar a string
```

## 🌳 Navegación del DOM

### Navegación por relaciones familiares
```python
element = soup.find('p')

# Padres
element.parent               # Elemento padre directo
element.parents             # Todos los ancestros

# Hijos
element.children            # Hijos directos (generador)
element.descendants         # Todos los descendientes
list(element.children)      # Lista de hijos

# Hermanos
element.next_sibling        # Siguiente hermano
element.previous_sibling    # Hermano anterior  
element.next_siblings       # Todos los hermanos siguientes
element.previous_siblings   # Todos los hermanos anteriores
```

### Navegación por elementos
```python
# Siguiente/anterior elemento (saltando texto)
element.find_next_sibling()
element.find_previous_sibling()
element.find_next()
element.find_previous()

# Con filtros
element.find_next_sibling('p')
element.find_next('div', class_='content')
```

## 🔧 Modificación del DOM

### Cambiar contenido
```python
element = soup.find('h1')
element.string = "Nuevo título"    # Cambiar texto
element['class'] = 'new-class'     # Cambiar atributo

# Agregar atributos
element['data-id'] = '123'

# Eliminar atributos
del element['class']
```

### Agregar elementos
```python
from bs4 import NavigableString, Tag

# Crear nuevo elemento
new_tag = soup.new_tag('p', class_='new-paragraph')
new_tag.string = "Texto del párrafo"

# Insertar elementos
parent.append(new_tag)           # Al final
parent.insert(0, new_tag)        # En posición específica
element.insert_before(new_tag)   # Antes del elemento
element.insert_after(new_tag)    # Después del elemento
```

### Eliminar elementos
```python
element.decompose()              # Eliminar y liberar memoria
element.extract()                # Extraer del árbol (se puede reusar)
element.clear()                  # Eliminar contenido del elemento
```

## 🔍 Búsquedas Avanzadas

### Con expresiones regulares
```python
import re

# Buscar por patrón
soup.find_all('a', href=re.compile(r'https://'))
soup.find_all(text=re.compile(r'Email'))
soup.find_all('div', class_=re.compile(r'post-\d+'))
```

### Con funciones personalizadas
```python
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

soup.find_all(has_class_but_no_id)

# Función más específica
def find_price_elements(tag):
    return (tag.name == 'span' and 
            tag.has_attr('class') and 
            'price' in ' '.join(tag['class']))

prices = soup.find_all(find_price_elements)
```

### Búsqueda de texto
```python
# Buscar texto específico
soup.find_all(text="Buscado")
soup.find_all(text=re.compile("patrón"))

# Buscar elementos que contienen texto
soup.find_all('p', text=True)  # p con texto
```

## 🎨 Casos de Uso Comunes

### Extraer enlaces
```python
# Todos los enlaces
links = [a.get('href') for a in soup.find_all('a', href=True)]

# Enlaces externos
external_links = [a.get('href') for a in soup.find_all('a', href=re.compile(r'^https?://'))]
```

### Extraer imágenes
```python
# Todas las imágenes
images = [img.get('src') for img in soup.find_all('img', src=True)]

# Con información adicional
img_data = []
for img in soup.find_all('img'):
    img_data.append({
        'src': img.get('src'),
        'alt': img.get('alt', ''),
        'title': img.get('title', '')
    })
```

### Extraer tablas
```python
table = soup.find('table')
if table:
    rows = []
    for tr in table.find_all('tr'):
        cells = [td.text.strip() for td in tr.find_all(['td', 'th'])]
        rows.append(cells)
```

### Extraer formularios
```python
form = soup.find('form')
if form:
    fields = []
    for input_tag in form.find_all('input'):
        fields.append({
            'name': input_tag.get('name'),
            'type': input_tag.get('type'),
            'value': input_tag.get('value')
        })
```

## ⚡ Tips de Rendimiento

```python
# Usar SoupStrainer para parsing parcial
from bs4 import SoupStrainer

# Solo parsear divs con clase 'content'
parse_only = SoupStrainer("div", class_="content")
soup = BeautifulSoup(html, "html.parser", parse_only=parse_only)

# Elegir parser apropiado
soup = BeautifulSoup(html, 'lxml')  # Más rápido para HTML válido

# Evitar búsquedas innecesarias
container = soup.find('div', class_='main')
if container:
    articles = container.find_all('article')  # Buscar solo dentro del container
```

## 🐛 Debugging

```python
# Ver estructura del HTML
print(soup.prettify()[:500])

# Verificar que el elemento existe
element = soup.find('div', class_='target')
if element:
    print(f"Encontrado: {element.name}")
else:
    print("Elemento no encontrado")

# Ver todos los atributos
print(element.attrs)

# Ver el HTML original del elemento
print(element)
```

## 🚨 Errores Comunes

```python
# ❌ Error: AttributeError cuando no existe
element = soup.find('nonexistent')
print(element.text)  # Error!

# ✅ Correcto: Verificar existencia
element = soup.find('h1')
if element:
    print(element.text)

# ✅ O usar get_text() con default
text = element.get_text() if element else "No encontrado"

# ❌ Error: Buscar por class con palabra reservada
soup.find('div', class='my-class')  # Error en sintaxis

# ✅ Correcto: Usar class_
soup.find('div', class_='my-class')
# O usar attrs
soup.find('div', attrs={'class': 'my-class'})
```

## 📚 Recursos Adicionales

- **Documentación oficial**: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- **Cookbook**: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start
- **Parsers comparison**: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser