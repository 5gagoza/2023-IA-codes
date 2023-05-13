# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:37:53 2023

@author: carlo

Sistemas Expertos:
    
Los sistemas expertos son programas que utilizan conocimiento experto para tomar 
decisiones o proporcionar recomendaciones en un dominio específico. Aquí tienes un 
ejemplo básico de un sistema experto utilizando reglas if-then en Python:
"""

class ExpertSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def infer(self, inputs):
        for rule in self.rules:
            if rule.applies(inputs):
                return rule.conclusion

        return "No se pudo llegar a una conclusión"

class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion

    def applies(self, inputs):
        for condition in self.conditions:
            if condition not in inputs:
                return False
        return True

# Crear el sistema experto
expert_system = ExpertSystem()

# Agregar reglas
expert_system.add_rule(Rule(["síntoma1", "síntoma2"], "Enfermedad A"))
expert_system.add_rule(Rule(["síntoma3", "síntoma4"], "Enfermedad B"))
expert_system.add_rule(Rule(["síntoma5"], "Enfermedad C"))

# Realizar una inferencia
symptoms = ["síntoma1", "síntoma2"]
result = expert_system.infer(symptoms)
print(result)  # Salida: "Enfermedad A"
