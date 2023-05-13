"""
El código implementa el algoritmo de propagación de restricciones (también conocido como algoritmo AC-3) para resolver un problema de restricción 
representado como un grafo de restricciones binarias.

El algoritmo consiste en iterativamente eliminar los valores inconsistentes de los dominios de las variables basándose en las restricciones entre ellas, 
hasta que no se puedan realizar más eliminaciones. 
Si en algún momento se reduce el dominio de alguna variable a un conjunto vacío, se sabe que no hay solución para el problema.
el grafo de restricciones se representa mediante un diccionario donde las claves son las variables y los valores son listas de 
tuplas que indican las restricciones entre la variable y otras variables. 
El algoritmo AC-3 se implementa en la función ac3, que recibe como parámetro el grafo de restricciones 
y devuelve un diccionario que asigna un valor a cada variable que satisface todas las restricciones, o None si no se encontró solución.
"""

from ortools.sat.python import cp_model

def solve_with_cutting_plane(model):
    solver = cp_model.CpSolver()
    while True:
        status = solver.Solve(model)
        if status == cp_model.OPTIMAL:
            return solver
        if status != cp_model.FEASIBLE:
            return None
        constraint = create_cutting_plane(solver, model)
        if constraint is None:
            return None
        model.add(constraint)

def create_cutting_plane(solver, model):
    # Create a new linear relaxation
    lp_model = cp_model.LinearRelaxation(model)
    for var in model.variables():
        lp_model.Add(var >= 0)
        lp_model.Add(var <= 1)
    for constr in model.constraints:
        if isinstance(constr, cp_model.LinearConstraint):
            linear = constr.linear
            lp_model.Add(
                sum(linear[i] * lp_model.Variable(model.variables()[i].name)
                    for i in range(len(linear))) <= constr.ub)
            lp_model.Add(
                sum(linear[i] * lp_model.Variable(model.variables()[i].name)
                    for i in range(len(linear))) >= constr.lb)

    # Solve the linear relaxation
    lp_solver = cp_model.CpSolver()
    lp_solver.parameters.linearization_level = 0
    status = lp_solver.Solve(lp_model)
    if status != cp_model.OPTIMAL:
        return None

    # Check if the solution is integral
    integral = True
    for var in model.variables():
        if lp_solver.Value(lp_model.Variable(var.name)) != round(
                solver.Value(var)):
            integral = False
            break

    # If the solution is integral, return None
    if integral:
        return None

    # Otherwise, add a new constraint to cut off the fractional solution
    cut_coeffs = []
    cut_vars = []
    for var in model.variables():
        value = lp_solver.Value(lp_model.Variable(var.name))
        cut_coeffs.append(value)
        cut_vars.append(var)
    rhs = sum(cut_coeffs) - 1
    return solver.scalProd(cut_vars, cut_coeffs) <= rhs

# Ejemplo de uso
model = cp_model.CpModel()
x = model.NewIntVar(0, 10, 'x')
y = model.NewIntVar(0, 10, 'y')
model.Add(x + y >= 5)
solver = solve_with_cutting_plane(model)
if solver is None:
    print('No se encontró solución óptima')
else:
    print('x = {}, y = {}, objetivo = {}'.format(
        solver.Value(x), solver.Value(y), solver.ObjectiveValue()))
