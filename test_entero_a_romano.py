"""
1. Crear una funcion que pase de entero > 0 y 4000 a romano
2. Cualquier otra entrada debe dar error

Casos de prueba
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError("El valor debe ser menor de 4000")
c)"unacadena" -> RomanNumberError("Debe ser un entero")
d) 0 -> RomanNumberError("El valor debe ser mayor de cero)
e) -3 -> RomanNumberError("El valor debe ser mayor de cero)
f) 4.5 -> RomanNumberError("Debe ser un entero")

"""
from first_part import *
from first_part import entero_a_romano


def test_tres_es_igual_a_dos_mas_uno():
    assert 2 + 1 == 3

def test_valor_1994():
    assert entero_a_romano(1994) == "MCMXCIV"

def test_valor_1995():
    assert entero_a_romano(1995) == "MCMXCV"