#Supongamos que tenemos un modelo de red bayesiana que representa el riesgo de tener una enfermedad en función de tres variables: fiebre, tos y fatiga. Queremos calcular la probabilidad de tener la enfermedad dado que la persona tiene fiebre y fatiga.
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura de la Red Bayesiana
model = BayesianModel([('Fiebre', 'Enfermedad'),
                       ('Tos', 'Enfermedad'),
                       ('Fatiga', 'Enfermedad')])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_fiebre = TabularCPD(variable='Fiebre', variable_card=2,
                        values=[[0.3], [0.7]])

cpd_tos = TabularCPD(variable='Tos', variable_card=2,
                     values=[[0.2], [0.8]])

cpd_fatiga = TabularCPD(variable='Fatiga', variable_card=2,
                        values=[[0.4], [0.6]])

cpd_enfermedad = TabularCPD(variable='Enfermedad', variable_card=2,
                            values=[[0.9, 0.6, 0.8, 0.1, 0.7, 0.3, 0.5, 0.2],
                                    [0.1, 0.4, 0.2, 0.9, 0.3, 0.7, 0.5, 0.8]],
                            evidence=['Fiebre', 'Tos', 'Fatiga'],
                            evidence_card=[2, 2, 2])

# Asignar las CPDs al modelo
model.add_cpds(cpd_fiebre, cpd_tos, cpd_fatiga, cpd_enfermedad)

# Crear el objeto de inferencia
inference = VariableElimination(model)

# Realizar la eliminación de variables
query = inference.query(variables=['Enfermedad'], evidence={'F
