from constraint import *

# Definir el problema CSP
problem = Problem()

# Definir variables
variables = ["x", "y", "z"]
for var in variables:
    problem.addVariable(var, range(1, 4))

# Definir restricciones
def sum_constraint(x, y, z):
    return x + y + z == 6
def product_constraint(x, y, z):
    return x * y * z == 6

problem.addConstraint(sum_constraint, variables)
problem.addConstraint(product_constraint, variables)

# Resolver el problema CSP
solutions = problem.getSolutions()

# Imprimir soluciones
print("Soluciones:")
for solution in solutions:
    print(solution)
