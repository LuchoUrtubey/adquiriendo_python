"""
Codeando lo aprendido hasta el momento
 
Unidad: 01 Tipos de datos y variables 
Parte: Codear 02 Variables

Este módulo permite practicar la creación y manipulación de variables,
además de explorar errores y curiosidades del lenguaje.

Autor: Lucho Urtubey

Versión: 1.0.0 (09-03-2025)
"""

# Modifica los valores de estas variables, pueden ser tuyos o inventados

nombre = "Luis"
apellido = "Urtubey"
edad = 43
trabaja = True
altura = 1.87

# La siguiente línea de código si bien es correcta, supera la convención de 100 caracteres
print(f"Mi nombre es {nombre} {apellido}, tengo {edad} años, mido {altura} mts y tengo trabajo: {trabaja} ")

# Para optimizarla con las convenciones podemos separar en varias líneas poniendo la f en cada línea
print(
    f"Mi nombre es {nombre} {apellido}, tengo {edad} años, "
    f"mido {altura} mts y tengo trabajo: {trabaja}"
)


# 📝 Tareas:

# 1️⃣ Escribe otra frase con los mismos datos, cambiando el orden de presentación.
# 2️⃣ Escribe la misma frase pero sin usar f-strings. Puedes usar `+` o `,` para concatenar.
# 3️⃣ Define un nuevo grupo de variables sobre un tema que te guste (fútbol, anime, música, etc.).
# 4️⃣ Imprime dos frases con estos nuevos datos. Una de ellas debe contener un valor `None`.
