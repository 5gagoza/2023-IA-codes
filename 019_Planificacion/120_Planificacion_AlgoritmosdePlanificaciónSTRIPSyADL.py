# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:40:17 2023

@author: carlo

Algoritmos de Planificación: STRIPS y ADL

Los algoritmos de planificación, como STRIPS (Stanford Research Institute Problem Solver) y
 ADL (Action Description Language), se utilizan para generar planes o secuencias de acciones 
 que permiten alcanzar un objetivo en un estado inicial dado. Aquí tienes un ejemplo básico 
 de código utilizando la biblioteca "pyhop" para implementar el algoritmo STRIPS en Python:
     
"""

class Predicate:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __repr__(self):
        return f"{self.name}({', '.join(self.args)})"

class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

    def __repr__(self):
        return f"{self.name}:\n    preconditions: {self.preconditions}\n    effects: {self.effects}"

class Planner:
    def __init__(self, actions, initial_state, goal_state):
        self.actions = actions
        self.initial_state = initial_state
        self.goal_state = goal_state

    def plan(self):
        plan = []
        state = self.initial_state.copy()

        while not self.goal_state.issubset(state):
            applicable_actions = self.get_applicable_actions(state)

            if not applicable_actions:
                return None

            action = self.select_action(applicable_actions)
            plan.append(action)
            state = self.apply_effects(state, action.effects)

        return plan

    def get_applicable_actions(self, state):
        applicable_actions = []

        for action in self.actions:
            if action.preconditions.issubset(state):
                applicable_actions.append(action)

        return applicable_actions

    def select_action(self, applicable_actions):
        return applicable_actions[0]

    def apply_effects(self, state, effects):
        new_state = state.copy()

        for effect in effects:
            if effect[0] == '-':
                predicate = Predicate(effect[1:], effect[2:])
                new_state.discard(predicate)
            else:
                predicate = Predicate(effect, effect[1:])
                new_state.add(predicate)

        return new_state

# Definir acciones
actions = [
    Action(
        "ir_a_la_universidad",
        {Predicate("en_casa", ["juan"])},
        {Predicate("en_universidad", ["juan"]), Predicate("-en_casa", ["juan"])}
    ),
    Action(
        "ir_a_casa",
        {Predicate("en_universidad", ["juan"])},
        {Predicate("en_casa", ["juan"]), Predicate("-en_universidad", ["juan"])}
    )
]

# Definir estado inicial y objetivo
initial_state = {Predicate("en_casa", ["juan"])}
goal_state = {Predicate("en_universidad", ["juan"])}

# Ejecutar el planificador
planner = Planner(actions, initial_state, goal_state)
plan = planner.plan()

# Imprimir el plan generado
if plan:
    for action in plan:
        print(action.name)
else:
    print("No se pudo encontrar un plan")
