"""
Adquisición de como documentar en Python

Unidad: 00 Introducción a Python
Parte: Adquisición 01 Documentar

En este módulo aprenderemos sobre:
- Comentarios, ¿cómo usarlos y cuándo?
- ¿Qué es un docstring, para qué sirve y cuáles son sus usos?
- Buenas prácticas
        
Autor: Lucho Urtubey

Versión: 1.0.0 (08-03-2025)
"""

# --------------------------------------------------------------------------------------------------
# COMENTARIOS
# --------------------------------------------------------------------------------------------------

# Esto es un comentario de una sola línea utilizando al principio el símbolo hashtag (#)
# Por convención se recomienda no exceder de los 100 caracteres por línea
# Ejemplo de comentario largo:
# Este es un comentario muy largo que excede los 100 caracteres y por eso lo partimos en dos líneas
# para que sea más fácil de leer sin romper la convención de no exceder 100 caracteres.
# Este es el único tipo de comentario real en Python
# Los comentarios no son leídos por el programa, así que no interfiere en nuestro código
# Su función es la de ayudarnos a entender ciertas partes del código
# Se recomienda el uso mínimo necesario

# --------------------------------------------------------------------------------------------------
# DOCSTRINGS
# --------------------------------------------------------------------------------------------------

# Qué es un docstring?
# Es una documentación que describe diferentes partes del código, como modulos, funciones y clases
# Qué es un módulo? Es un archivo .py como este mismo.
# Pero y funciones y clases? No te preocupes lo veremos más adelante.
# El docstring se escribe entre tres comillas dobles """ """ o entre tres comillas simples ''' '''
# Como recién estamos arrancando sólo lo utilizaremos al principio de cada archivo.
# Fijate desde la línea 1 a la 15
# Se lo conoce como docstring de módulo, sirve para describir el contenido y propósito del archivo
# Sí o sí debe ir al principio del archivo
# Bueno todo muy lindo...pero para que nos sirve?
# Para tener el código documentado, cuando tengas muchos archivos o trabajes en equipo
# Lo vas a agradecer.
# Es útil tanto para otros desarrolladores como para herramientas de documentación automática.

# --------------------------------------------------------------------------------------------------
# BUENAS PRÁCTICAS
# --------------------------------------------------------------------------------------------------

# - Evitar comentarios redundantes: No comentes lo obvio.
# - Utilizar comentarios para explicar "por qué" se hace algo, no solo el "qué".
# - Mantén los comentarios claros y concisos.
# - Los docstrings deben usarse para documentar módulos, funciones y clases.
# - Para cualquier otra situación, usa comentarios
# - Recuerda, los comentarios no son interpretados por Python, pero los docstrings sí.
# - Sugerencia para docstrings de módulos:
#       -Descripción del archivo, qué utiliza y qué requisitos tiene si los hay
#       -Autor (opcional)
#       -Contacto (opcional)
#       -Versión (opcional)
# - Ante cualquier duda, checá PEP 257 sugerencia oficial de Python
# - Recuerda, no hay convención oficial, pero si es una sugerencia oficial... 🤷‍♂️
