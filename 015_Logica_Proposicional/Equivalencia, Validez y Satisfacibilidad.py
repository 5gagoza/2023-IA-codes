
import sympy

# Ejemplo de equivalencia
expresion1 = (3 + 2) == (2 + 3)
expresion2 = 5 == 5
equivalencia = expresion1 == expresion2
print("Equivalencia:", equivalencia)

# Ejemplo de validez
expresion3 = (4 < 5) or (5 < 4)
validez = expresion3
print("Validez:", validez)

# Ejemplo de satisfacibilidad
expresion4 = (1 > 0) and (9 < 10)
satisfacibilidad = sympy.satisfiable(expresion4)
print("Satisfacibilidad:", satisfacibilidad)