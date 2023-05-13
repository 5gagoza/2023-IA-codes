"""Lógica Difusa
    
    Su objetivo principal es capturar y representar el razonamiento humano en situaciones donde 
    la precisión matemática no es suficiente.

    Crear un conjunto difuso: Cada elemento tendrá un valor de pertenencia.
    Reglas difusas: Describen las relaciones y el comportamiento de los elementos.
    Fuzzificación: Asignar grados de pertenencia a las entradas numéricas.
    Determinar los grados de activación de una regla.
    Combinar las reglas.
    Defuzzificación: Convierte la salida difusa en un valor numérico o una decisión concreta.
    Evaluación de resultados en el contexto del problema.
    
"""

# Importar librerías necesarias
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Paso 1: Definir el universo del discurso
# Definimos el rango del universo del discurso para la temperatura (0 a 100 grados)
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')

# Paso 2: Definir conjuntos difusos
# Definimos los conjuntos difusos "baja", "media" y "alta" para la temperatura
temperatura['baja'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['media'] = fuzz.trimf(temperatura.universe, [0, 50, 100])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [50, 100, 100])

# Paso 3: Definir reglas difusas
# Definimos las reglas difusas para relacionar los antecedentes y consecuentes
regla1 = ctrl.Rule(temperatura['baja'], temperatura['alta'])
regla2 = ctrl.Rule(temperatura['media'], temperatura['media'])
regla3 = ctrl.Rule(temperatura['alta'], temperatura['baja'])

# Paso 4: Fuzzificación
# Realizamos la fuzzificación para convertir la temperatura de entrada en un valor difuso
temperatura_input = 75
temperatura['baja'].view()
temperatura['media'].view()
temperatura['alta'].view()
temperatura.view(sim=ctrl.ControlSystemSimulation(temperatura.ctrl))

# Paso 5: Evaluación de las reglas
# Evaluamos las reglas difusas para determinar los grados de activación de cada regla
sistema_ctrl = ctrl.ControlSystem([regla1, regla2, regla3])
simulador = ctrl.ControlSystemSimulation(sistema_ctrl)
simulador.input['temperatura'] = temperatura_input
simulador.compute()

# Paso 6: Combinación de las reglas
# Combinamos los resultados de las reglas difusas para obtener una salida difusa
temperatura.view(sim=simulador)

# Paso 7: Defuzzificación
# Realizamos la defuzzificación para obtener un valor numérico para la temperatura de salida
temperatura_salida = simulador.output['temperatura']
print("Temperatura de salida:", temperatura_salida)

# Paso 8: Interpretación y aplicación
# Interpretamos el valor de la temperatura de salida y tomamos una acción basada en ello
if temperatura_salida < 50:
    print("La temperatura de salida es baja.")
elif temperatura_salida > 50:
    print("La temperatura de salida es alta.")
else:
    print("La temperatura de salida es media.")
