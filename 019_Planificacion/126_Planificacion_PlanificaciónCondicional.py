# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:00:13 2023

@author: 
    
    Planificación Condicional
"""
class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

class Plan:
    def __init__(self):
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def execute(self):
        for action in self.actions:
            print("Executing action:", action.name)
            # Lógica para ejecutar la acción

# Definir acciones
action1 = Action("Action1", {"A"}, {"B"})
action2 = Action("Action2", {"B"}, {"C"})
action3 = Action("Action3", {"C"}, {"D"})

# Crear un plan y agregar acciones
plan = Plan()
plan.add_action(action1)
plan.add_action(action2)
plan.add_action(action3)

# Ejecutar el plan
plan.execute()

