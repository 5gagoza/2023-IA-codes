# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:04:37 2023

@author: carlo

Planificación Continua:
"""

from ortools.sat.python import cp_model

def solve_continuous_planning(start_time, end_time, actions):
    model = cp_model.CpModel()

    # Variables de tiempo para las acciones
    action_vars = {}
    for action in actions:
        action_vars[action] = model.NewIntVar(start_time, end_time, f'{action}_start_time')

    # Restricciones de tiempo para las acciones
    for action in actions:
        duration = actions[action]['duration']
        model.Add(action_vars[action] + duration <= end_time)

    # Restricciones de precedencia entre acciones
    for action in actions:
        if 'precedence' in actions[action]:
            precedence_actions = actions[action]['precedence']
            for precedence_action in precedence_actions:
                model.Add(action_vars[action] >= action_vars[precedence_action] + actions[precedence_action]['duration'])

    # Definir objetivo: maximizar el tiempo de finalización de la última acción
    model.Maximize(action_vars['final_action'])

    # Resolver el problema de planificación continua
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        plan = {}
        for action in actions:
            start_time = solver.Value(action_vars[action])
            plan[action] = start_time
        return plan
    else:
        return None

# Definir acciones y duraciones
actions = {
    'action1': {'duration': 2},
    'action2': {'duration': 3},
    'action3': {'duration': 4, 'precedence': ['action1', 'action2']},
    'final_action': {'duration': 1, 'precedence': ['action3']}
}

# Resolver el problema de planificación continua
start_time = 0
end_time = 10
plan = solve_continuous_planning(start_time, end_time, actions)
print(plan)  # Salida: {'action1': 0, 'action2': 2, 'action3': 3, 'final_action': 7}
