"""
Adquisición de las variables

Unidad: 01 Tipos de datos y variables
Parte: Asquisición 02 Variables

En este módulo aprenderemos sobre:
- ¿Qué son, cómo se usan?
- Constantes, ¿qué son, existen?
        
Autor: Lucho Urtubey

Versión: 1.0.0 (09-03-2025)
"""

# --------------------------------------------------------------------------------------------------
# VARIABLES
# --------------------------------------------------------------------------------------------------

# Una variable es:
# - Un espacio en memoria donde se almacena un valor que puede cambiar
#   durante la ejecución del programa
# - Un contenedor para almacenar datos


# Ejemplo de variable:
# nombre = "Lucho"

# Convención:
# - ✅ Usamos variables en minúsculas y con guiones bajos para mejorar la legibilidad (snake_case).
# - ❌ Las variables no pueden comenzar con un número.
# - ❌ Las variables no pueden contener espacios.
# - ❌ Las variables no pueden contener caracteres especiales, excepto guiones bajos.


# En vez de escribir el valor directamente en el código
# lo almacenamos en una variable y luego lo utilizamos en el código.

# Declaramos una variable llamada nombre y le asignamos el valor "Lucho"
nombre = "Lucho"
# Imprimimos la variable nombre
print(nombre) 
# Si lo ejecutamos en la terminal, veremos en pantalla el valor de la variable nombre

apellido = "Urtubey"
print(apellido)

# Nota: Al imprimir una variable esta NO debe ir entre comillas
#       de lo contrario, se imprimirá la palabra nombre y no su valor.

# Declaramos la variable num1 y le asignamos el valor de int 20
num1 = 20 
# Declaramos la variable num2 y le asignamos el valor de int 15
num2 = 15
# Declaramos la variable suma y le asignamos la operación suma entre num1 y num2
suma = num1 + num2
# Imprimimos la variable suma
print(suma) # output: 35

# Las variables se pueden reasignar
# Por ejemplo tomemos la variable nombre que tiene asignado Lucho y cambiemos su valor

nombre = "Luis"
print(nombre)
# Ahora la variable nombre es Luis y ya no mas Lucho

# --------------------------------------------------------------------------------------------------
# CONCATENACIÓN DE VARIABLES EN EL PRINT
# --------------------------------------------------------------------------------------------------

# Hasta ahora vimos que le ingresamos un solo dato al print

# Pero podemos ponerle mas de uno, por ejemplo texto y una variable:
print("Mi nombre es", nombre)

# Más de una variable
print(nombre, apellido)
print(nombre, num2, num1, suma)

# Al concatenar con una ,
# Nos da un espacio predeterminado entre elemento y elemento
# Si por alguna razón no deseamos ese espacio podemos concatenar utilizando el +
print(nombre + apellido) # output: LuisUrtubey
print(nombre + " " + apellido) # output: Luis Urtubey


# Variables de una sóla línea
# Podemos hacer una asignación múltiple y en el mismo orden
nombre, apellido, alias, edad = "Luis", "Urtubey", "Lucho", 43
print("Me llamo", nombre, apellido, ".Mi edad es de", edad, "y mi alias es", alias)

# Acá tenemos un problema, si queremos concatenar usando +
# sólo es permitido si todos los elementos son str
# y edad lo tenemos como int
# Descomenta la siguiente línea de código y ejecuta para ver el error, luego vuelve a comentarla

#print("Me llamo " + nombre + " " + apellido + ". Mi edad es de " + edad + " y mi alias es " + alias)
# error: TypeError: can only concatenate str (not "int") to str

# Una solución es usar:
# Formateo de concatenación
# debemos colocar al primcipio del string un f
# y las variables van entre llaves 
print(f"Me llamo {nombre} {apellido}. Mi edad es de {edad} y mi alias es {alias}")


# --------------------------------------------------------------------------------------------------
# CONSTANTES EN PYTHON EXISTEN?
# --------------------------------------------------------------------------------------------------

# Aunque en otros lenguajes existe la palabra const para definir constantes...
# En python no existen las constantes, no hay un tipo de variable que no se pueda modificar.
# Aunque no existen las constantes por convención,
# las variables que no se deben modificar se escriben en mayúsculas.
# Pero hay que tener en cuenta que estas pueden ser modificadas, aunque no se debería hacerlo.

#Ejemplo:
MI_CONSTANTE = "Valor que no se debe modificar"
print(MI_CONSTANTE)
MI_CONSTANTE = "Pero ojo que si se puede modificar"
print(MI_CONSTANTE)


# --------------------------------------------------------------------------------------------------
# BORRAR VARIABLES
# --------------------------------------------------------------------------------------------------

# Podemos borrar una variable agregando del

del MI_CONSTANTE
# Descomenta la siguiente línea para comprobar que está eliminado
#print(MI_CONSTANTE) # NameError: name 'MI_CONSTANTE' is not defined

# Ideal para liberar memoria en variables que ya no se usan o quedaron obsoletas
