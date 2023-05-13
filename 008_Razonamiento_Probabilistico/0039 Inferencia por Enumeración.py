from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura de la Red Bayesiana
model = BayesianModel([('Fiebre', 'Enfermedad'),
                       ('Tos', 'Enfermedad')])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_fiebre = TabularCPD(variable='Fiebre', variable_card=2,
                        values=[[0.3], [0.7]])

cpd_tos = TabularCPD(variable='Tos', variable_card=2,
                     values=[[0.2], [0.8]])

cpd_enfermedad = TabularCPD(variable='Enfermedad', variable_card=2,
                            values=[[0.9, 0.6, 0.7, 0.1],
                                    [0.1, 0.4, 0.3, 0.9]],
                            evidence=['Fiebre', 'Tos'],
                            evidence_card=[2, 2])

# Asignar las CPDs al modelo
model.add_cpds(cpd_fiebre, cpd_tos, cpd_enfermedad)

# Crear el objeto de inferencia
inference = VariableElimination(model)

# Realizar la inferencia por enumeración
query = inference.query(variables=['Enfermedad'], evidence={'Fiebre': 1, 'Tos': 1})

print("La probabilidad de tener la enfermedad dado fiebre y tos es:")
print(query['Enfermedad'])
