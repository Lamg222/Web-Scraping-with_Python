"""
🏋️ EJERCICIO 1: Tu Primer Web Scraper
=====================================

📋 Descripción:
--------------
Crea un web scraper básico que extraiga información de la página de libros
ubicada en '../data/books_catalog.html'. 

🎯 Objetivos de Aprendizaje:
----------------------------
- Usar requests para obtener HTML (o leer archivo local)
- Parsear HTML con BeautifulSoup
- Extraer información básica con selectores
- Estructurar datos extraídos

📝 Tareas:
----------
1. Cargar el archivo HTML
2. Extraer TODOS los títulos de libros
3. Extraer los precios actuales de cada libro
4. Extraer las valoraciones (rating)
5. Crear una lista de diccionarios con la información
6. Contar cuántos libros están en stock vs agotados

💡 Pistas:
----------
- Usa BeautifulSoup con el parser 'html.parser'
- Los libros están en elementos <article class="book-item">
- Los títulos están en <h3 class="book-title">
- Los precios actuales tienen la clase "price current-price"
- El stock está en elementos con clase "stock"

🎁 Retos Adicionales:
---------------------
1. Extraer también el autor y editorial
2. Calcular el descuento en porcentaje cuando hay precio original
3. Ordenar los libros por valoración
4. Filtrar solo libros de Python
5. Exportar los resultados a CSV

✅ Tests Incluidos:
------------------
El código incluye tests automáticos para validar tu solución.
"""

# IMPORTS NECESARIOS
import os
from bs4 import BeautifulSoup
from typing import List, Dict
import json

# ZONA DE CÓDIGO - COMPLETA LAS FUNCIONES
# ========================================

def cargar_html(ruta_archivo: str) -> str:
    """
    Carga el contenido HTML desde un archivo local.
    
    Args:
        ruta_archivo: Ruta al archivo HTML
    
    Returns:
        Contenido HTML como string
    """
    # TODO: Implementa esta función
    # Pista: usa open() y read()
    pass


def extraer_libros(html_content: str) -> List[Dict]:
    """
    Extrae información de todos los libros del HTML.
    
    Args:
        html_content: Contenido HTML como string
    
    Returns:
        Lista de diccionarios con información de cada libro
        Cada diccionario debe tener:
        - titulo: str
        - precio_actual: float
        - precio_original: float (o None si no hay descuento)
        - valoracion: float
        - num_resenas: int
        - en_stock: bool
        - autor: str
        - editorial: str
    """
    # TODO: Implementa esta función
    # Pasos sugeridos:
    # 1. Crear objeto BeautifulSoup
    # 2. Encontrar todos los articles con clase "book-item"
    # 3. Para cada libro, extraer la información requerida
    # 4. Retornar lista de diccionarios
    
    libros = []
    
    # Tu código aquí
    
    return libros


def analizar_stock(libros: List[Dict]) -> Dict:
    """
    Analiza el estado del stock de los libros.
    
    Args:
        libros: Lista de diccionarios con información de libros
    
    Returns:
        Diccionario con estadísticas:
        - total_libros: int
        - en_stock: int
        - agotados: int
        - pocas_unidades: int (menos de 5 unidades)
    """
    # TODO: Implementa esta función
    estadisticas = {
        'total_libros': 0,
        'en_stock': 0,
        'agotados': 0,
        'pocas_unidades': 0
    }
    
    # Tu código aquí
    
    return estadisticas


def filtrar_por_categoria(libros: List[Dict], categoria: str) -> List[Dict]:
    """
    RETO ADICIONAL: Filtra libros por categoría.
    
    Args:
        libros: Lista de libros
        categoria: Categoría a filtrar ('python', 'javascript', 'data')
    
    Returns:
        Lista filtrada de libros
    """
    # TODO: Implementa esta función (OPCIONAL)
    pass


def calcular_descuentos(libros: List[Dict]) -> List[Dict]:
    """
    RETO ADICIONAL: Calcula el porcentaje de descuento para cada libro.
    
    Args:
        libros: Lista de libros
    
    Returns:
        Lista de libros con campo adicional 'descuento_porcentaje'
    """
    # TODO: Implementa esta función (OPCIONAL)
    pass


# TESTS - NO MODIFICAR
# ====================

def test_ejercicio():
    """Tests automáticos para validar la solución."""
    print("\n" + "="*50)
    print("🧪 EJECUTANDO TESTS")
    print("="*50)
    
    # Test 1: Cargar HTML
    print("\n📝 Test 1: Cargando archivo HTML...")
    try:
        ruta = os.path.join(os.path.dirname(__file__), '..', 'data', 'books_catalog.html')
        html = cargar_html(ruta)
        assert html is not None and len(html) > 0, "El HTML no se cargó correctamente"
        print("✅ HTML cargado correctamente")
    except AssertionError as e:
        print(f"❌ Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False
    
    # Test 2: Extraer libros
    print("\n📝 Test 2: Extrayendo información de libros...")
    try:
        libros = extraer_libros(html)
        assert isinstance(libros, list), "Debe retornar una lista"
        assert len(libros) > 0, "No se encontraron libros"
        
        # Verificar estructura del primer libro
        primer_libro = libros[0]
        campos_requeridos = ['titulo', 'precio_actual', 'valoracion', 
                            'num_resenas', 'en_stock', 'autor', 'editorial']
        for campo in campos_requeridos:
            assert campo in primer_libro, f"Falta el campo '{campo}'"
        
        print(f"✅ Se extrajeron {len(libros)} libros correctamente")
        print(f"   Ejemplo: {primer_libro['titulo'][:50]}...")
    except AssertionError as e:
        print(f"❌ Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False
    
    # Test 3: Analizar stock
    print("\n📝 Test 3: Analizando stock...")
    try:
        stats = analizar_stock(libros)
        assert isinstance(stats, dict), "Debe retornar un diccionario"
        assert stats['total_libros'] == len(libros), "Total de libros incorrecto"
        assert stats['en_stock'] + stats['agotados'] <= stats['total_libros'], \
               "La suma de stock no cuadra"
        
        print(f"✅ Análisis de stock correcto:")
        print(f"   Total: {stats['total_libros']} libros")
        print(f"   En stock: {stats['en_stock']}")
        print(f"   Agotados: {stats['agotados']}")
    except AssertionError as e:
        print(f"❌ Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False
    
    print("\n" + "="*50)
    print("🎉 ¡TODOS LOS TESTS PASADOS!")
    print("="*50)
    
    # Tests opcionales para retos adicionales
    print("\n🏆 RETOS ADICIONALES (Opcional):")
    try:
        # Test filtrado
        libros_python = filtrar_por_categoria(libros, 'python')
        if libros_python is not None:
            print(f"✅ Reto 1: Filtrado por categoría implementado")
            print(f"   Libros de Python: {len(libros_python)}")
    except:
        print("⏭️ Reto 1: No implementado")
    
    try:
        # Test descuentos
        libros_con_descuento = calcular_descuentos(libros)
        if libros_con_descuento is not None and len(libros_con_descuento) > 0:
            if 'descuento_porcentaje' in libros_con_descuento[0]:
                print(f"✅ Reto 2: Cálculo de descuentos implementado")
    except:
        print("⏭️ Reto 2: No implementado")
    
    return True


# FUNCIÓN PRINCIPAL
# =================

def main():
    """Función principal para ejecutar el ejercicio."""
    print("\n" + "🕷️"*20)
    print(" EJERCICIO 1: TU PRIMER WEB SCRAPER")
    print("🕷️"*20)
    
    print("\n📚 Este ejercicio te enseñará los fundamentos del web scraping.")
    print("📝 Completa las funciones marcadas con TODO.")
    print("💡 Usa las pistas si te quedas atascado.")
    print("✅ Ejecuta los tests para validar tu solución.")
    
    # Ejecutar tests
    if test_ejercicio():
        print("\n🏆 ¡EJERCICIO COMPLETADO!")
        print("⭐ Has ganado 10 puntos")
        print("\n📊 Resumen de tu scraper:")
        
        # Mostrar resumen si el ejercicio está completo
        try:
            ruta = os.path.join(os.path.dirname(__file__), '..', 'data', 'books_catalog.html')
            html = cargar_html(ruta)
            libros = extraer_libros(html)
            stats = analizar_stock(libros)
            
            print(f"   - Libros procesados: {stats['total_libros']}")
            print(f"   - Disponibles: {stats['en_stock']}")
            print(f"   - Agotados: {stats['agotados']}")
            print(f"   - Valoración promedio: {sum(l['valoracion'] for l in libros)/len(libros):.1f}⭐")
        except:
            pass
    else:
        print("\n❌ Hay errores en tu solución. Revisa el código y vuelve a intentar.")
        print("💡 Tip: Lee cuidadosamente los mensajes de error.")


# SOLUCIÓN DE REFERENCIA (No mirar hasta intentar!)
# ==================================================
"""
La solución completa está disponible en:
solutions/01_primer_scraper_solution.py

Pero intenta resolverlo por tu cuenta primero! 💪
"""

if __name__ == "__main__":
    main()