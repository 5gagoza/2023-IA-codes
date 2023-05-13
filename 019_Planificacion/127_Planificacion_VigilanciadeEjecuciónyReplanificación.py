# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:02:48 2023

@author: carlo

Vigilancia de Ejecución y Replanificación:
"""
class ExecutionMonitor:
    def __init__(self, initial_state, goals, actions):
        self.state = initial_state
        self.goals = goals
        self.actions = actions

    def update_state(self, action):
        # Actualizar el estado según los efectos de la acción ejecutada
        for effect in self.actions[action]['effects']:
            if effect[0] == '-':
                self.state[effect[1:]] = False
            else:
                self.state[effect] = True

    def check_goals(self):
        # Verificar si se alcanzaron las metas
        for goal in self.goals:
            if self.goals[goal] != self.state.get(goal, False):
                return False
        return True

    def replan(self):
        # Replanificar un nuevo plan basado en el estado actual y las metas
        # Implementa tu lógica de replanificación aquí
        new_plan = self.generate_plan()
        return new_plan

    def generate_plan(self):
        # Generar un nuevo plan basado en el estado actual y las metas
        # Implementa tu lógica de generación de plan aquí
        pass

# Definir el estado inicial, metas y acciones
initial_state = {'A': True, 'B': False, 'C': False}
goals = {'D': True}
actions = {
    'accion1': {'preconditions': ['A'], 'effects': ['B']},
    'accion2': {'preconditions': ['B'], 'effects': ['C']},
    'accion3': {'preconditions': ['C'], 'effects': ['D']}
}

# Crear un monitor de ejecución y replanificación
monitor = ExecutionMonitor(initial_state, goals, actions)

# Ejecutar el plan inicial
plan = ['accion1', 'accion2', 'accion3']
for action in plan:
    print('Executing action:', action)
    monitor.update_state(action)

# Verificar si se alcanzaron las metas
if monitor.check_goals():
    print('Goals achieved!')
else:
    # Replanificar si las metas no se alcanzaron
    new_plan = monitor.replan()
    print('New plan:', new_plan)

