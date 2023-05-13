# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:31:21 2023

@author: carlo

Razonamiento por Defecto y No Monotónico:
    
El razonamiento por defecto y no monotónico se refiere a la capacidad de realizar 
inferencias basadas en suposiciones por defecto, que pueden ser revisadas o anuladas 
por nueva información. Aquí tienes un ejemplo de código utilizando reglas de razonamiento 
por defecto:
"""

class KnowledgeBase:
    def __init__(self):
        self.facts = []
        self.rules = []

    def add_fact(self, fact):
        self.facts.append(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def infer(self, query):
        inferred_facts = []
        for rule in self.rules:
            if rule.applies(self.facts):
                inferred_facts.append(rule.conclusion)

        if query in inferred_facts:
            return True
        else:
            return False

class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion

    def applies(self, facts):
        for condition in self.conditions:
            if condition not in facts:
                return False
        return True

# Crear la base de conocimientos
kb = KnowledgeBase()

# Agregar hechos
kb.add_fact("Tiene alas")
kb.add_fact("Vuela")
kb.add_fact("Es un pájaro")

# Agregar reglas
kb.add_rule(Rule(["Tiene alas", "Vuela"], "Es un pájaro"))

# Inferir
result = kb.infer("Es un pájaro")
print(result)  # Salida: True

