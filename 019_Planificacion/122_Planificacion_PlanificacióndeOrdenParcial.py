# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:46:11 2023

@author: carlo

Planificación de Orden Parcial:
La planificación de orden parcial se refiere a la generación de planes que no necesariamente 
especifican un orden total para todas las acciones. Aquí tienes un ejemplo básico de código 
utilizando la biblioteca "pyPOSH" para implementar la planificación de orden parcial en 
Python:
"""

from pyPOSH.action import Action
from pyPOSH.condition import Condition
from pyPOSH.plan import Plan

# Definir acciones y condiciones
cond_caja_abierta = Condition("CajaAbierta")
cond_caja_cerrada = Condition("CajaCerrada")
cond_objeto_cogido = Condition("ObjetoCogido")
cond_objeto_no_cogido = Condition("ObjetoNoCogido")

action_abrir_caja = Action("AbrirCaja", [cond_caja_cerrada], [cond_caja_abierta])
action_coger_objeto = Action("CogerObjeto", [cond_caja_abierta, cond_objeto_no_cogido], [cond_objeto_cogido])
action_poner_objeto = Action("PonerObjeto", [cond_caja_abierta, cond_objeto_cogido], [cond_objeto_no_cogido])

# Crear un plan y agregar acciones
plan = Plan()
plan.add_action(action_abrir_caja)
plan.add_action(action_coger_objeto)
plan.add_action(action_poner_objeto)

# Ejecutar el plan
plan.execute()


"""
En este ejemplo, se definen acciones y condiciones utilizando la biblioteca "pyPOSH". 
Las condiciones representan estados del sistema, y las acciones tienen precondiciones y
 efectos en forma de condiciones. El plan creado contiene las acciones y se ejecuta para 
 generar una secuencia de acciones que satisfacen las condiciones.
"""