# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:53:29 2023

@author: carlo

Redes Jerárquicas de Tareas
Las redes jerárquicas de tareas (HTN, por sus siglas en inglés) son un enfoque de 
planificación que utiliza tareas de alto nivel para descomponer problemas en subtareas 
más pequeñas. A continuación se muestra un ejemplo de código para representar una red 
jerárquica de tareas en Python:
    
"""

class Task:
    def __init__(self, name, subtasks=None):
        self.name = name
        self.subtasks = subtasks or []

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

def execute_task(task):
    print("Ejecutando tarea:", task)
    for subtask in task.subtasks:
        execute_task(subtask)

# Crea una jerarquía de tareas
root_task = Task("Root")
task1 = Task("Tarea 1")
task2 = Task("Tarea 2")
task3 = Task("Tarea 3")
subtask1 = Task("Subtarea 1")
subtask2 = Task("Subtarea 2")

task1.add_subtask(subtask1)
task2.add_subtask(subtask2)
root_task.add_subtask(task1)
root_task.add_subtask(task2)
root_task.add_subtask(task3)

# Ejecuta la jerarquía de tareas
execute_task(root_task)

