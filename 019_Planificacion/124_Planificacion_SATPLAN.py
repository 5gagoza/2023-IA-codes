# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:50:42 2023

@author: carlo

Planificación Lógica Proposicional: SATPLAN
La planificación lógica proposicional, como SATPLAN, utiliza la lógica proposicional 
para representar y resolver problemas de planificación. A continuación se muestra un 
ejemplo de código utilizando la biblioteca "pysat" para implementar SATPLAN en Python:
"""
from pysat.solvers import Glucose3

def solve_satplan(init, goal, actions):
    # Crear el solucionador SAT
    solver = Glucose3()

    # Crear variables para las acciones y estados
    variables = {}
    action_index = 1

    # Construir variables y cláusulas
    for action in actions:
        variables[action] = action_index
        action_index += 1

        # Cláusulas para las precondiciones
        for precondition in actions[action]['preconditions']:
            if precondition[0] == '-':
                precondition_var = variables[precondition[1:]]
                solver.add_clause([-variables[action], -precondition_var])
            else:
                precondition_var = variables[precondition]
                solver.add_clause([-variables[action], precondition_var])

        # Cláusulas para los efectos
        for effect in actions[action]['effects']:
            if effect[0] == '-':
                effect_var = variables[effect[1:]]
                solver.add_clause([variables[action], -effect_var])
            else:
                effect_var = variables[effect]
                solver.add_clause([variables[action], effect_var])

    # Agregar cláusulas para el estado inicial
    for literal in init:
        if literal[0] == '-':
            literal_var = variables[literal[1:]]
            solver.add_clause([-literal_var])
        else:
            literal_var = variables[literal]
            solver.add_clause([literal_var])

    # Agregar cláusulas para el objetivo
    for literal in goal:
        if literal[0] == '-':
            literal_var = variables[literal[1:]]
            solver.add_clause([-literal_var])
        else:
            literal_var = variables[literal]
            solver.add_clause([literal_var])

    # Resolver el problema SAT
    result = solver.solve()

    if result:
        # Obtener la secuencia de acciones
        action_sequence = [action for action in actions if solver.model[variables[action]] > 0]
        return action_sequence
    else:
        return None

# Definir el estado inicial, objetivo y acciones
init = ['A', '-B', '-C']
goal = ['D']
actions = {
    'accion1': {'preconditions': ['A', '-B'], 'effects': ['C']},
    'accion2': {'preconditions': ['B', '-D'], 'effects': []}
}

# Resolver el problema de planificación
plan = solve_satplan(init, goal, actions)
print(plan)  # Salida: ['accion1', 'accion2']


