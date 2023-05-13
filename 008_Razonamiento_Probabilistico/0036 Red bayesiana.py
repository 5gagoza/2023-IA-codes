from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Definir la estructura de la Red Bayesiana
model = BayesianModel([('Edad', 'EnfermedadCardiovascular'),
                       ('Género', 'EnfermedadCardiovascular'),
                       ('Colesterol', 'EnfermedadCardiovascular'),
                       ('Fumar', 'EnfermedadCardiovascular')])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_edad = TabularCPD(variable='Edad', variable_card=3,
                      values=[[0.2], [0.5], [0.3]])

cpd_genero = TabularCPD(variable='Género', variable_card=2,
                        values=[[0.6], [0.4]])

cpd_colesterol = TabularCPD(variable='Colesterol', variable_card=2,
                            values=[[0.7], [0.3]])

cpd_fumar = TabularCPD(variable='Fumar', variable_card=2,
                       values=[[0.8], [0.2]])

cpd_enfermedad = TabularCPD(variable='EnfermedadCardiovascular', variable_card=2,
                            values=[[0.9, 0.7, 0.8, 0.5],
                                    [0.1, 0.3, 0.2, 0.5]],
                            evidence=['Edad', 'Género', 'Colesterol', 'Fumar'],
                            evidence_card=[3, 2, 2, 2])

# Asignar las CPDs al modelo
model.add_cpds(cpd_edad, cpd_genero, cpd_colesterol, cpd_fumar, cpd_enfermedad)

# Comprobar la consistencia del modelo
model.check_model()

# Calcular la probabilidad condicional de enfermedad cardiovascular dado ciertos valores
prob_enfermedad = model.predict_probability({'Edad': 1, 'Género': 0, 'Colesterol': 1, 'Fumar': 1}, ['EnfermedadCardiovascular'])

print("La probabilidad de enfermedad cardiovascular es:", prob_enfermedad.values[1])
