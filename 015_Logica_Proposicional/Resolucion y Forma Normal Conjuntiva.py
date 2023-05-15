
from sympy import symbols, Or, And, Not, to_cnf, simplify

def resolution_demo():
    # Definir los símbolos de las variables
    p, q, r = symbols('p q r')

    # Construir las cláusulas
    clause1 = Or(p, Not(q))
    clause2 = Or(Not(p), r)
    clause3 = Or(Not(r), q)
    clause4 = Or(Not(p), Not(q), Not(r))

    # Aplicar la regla de resolución
    resolvent1 = Or(clause1.args[0], clause2.args[0])  # Resolvente 1: (p OR ~q) OR ~p
    resolvent2 = Or(resolvent1, clause3.args[1])  # Resolvente 2: ((p OR ~q) OR ~p) OR q
    resolvent3 = Or(resolvent2, clause4.args[1])  # Resolvente 3: (((p OR ~q) OR ~p) OR q) OR ~q

    # Simplificar el resolvente final
    resolvent_final = simplify(resolvent3)

    # Imprimir las cláusulas y el resolvente final
    print("Cláusula 1:", clause1)
    print("Cláusula 2:", clause2)
    print("Cláusula 3:", clause3)
    print("Cláusula 4:", clause4)
    print("Resolvente Final:", resolvent_final)

def fnc_conversion_demo():
    # Definir los símbolos de las variables
    p, q, r = symbols('p q r')

    # Construir la fórmula lógica
    formula = Or(And(p, q), And(Not(p), r), And(Not(r), q))

    # Convertir la fórmula a su forma normal conjuntiva (FNC)
    fnc_formula = to_cnf(formula)

    # Imprimir la fórmula original y la FNC resultante
    print("Fórmula original:", formula)
    print("FNC:", fnc_formula)

# Ejecutar el programa
resolution_demo()
fnc_conversion_demo()