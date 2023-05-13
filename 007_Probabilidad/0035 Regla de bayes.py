import pandas as pd

# Crear un DataFrame con datos de ejemplo
data = {'Clima': ['Soleado', 'Nublado', 'Lluvioso', 'Soleado', 'Nublado', 'Lluvioso'],
        'Temperatura': ['Caliente', 'Moderada', 'Fresca', 'Moderada', 'Caliente', 'Fresca'],
        'ProbabilidadLluvia': ['Baja', 'Baja', 'Alta', 'Alta', 'Baja', 'Alta']}
df = pd.DataFrame(data)

# Calcular las probabilidades condicionales
p_T_given_C = df.groupby('Clima')['Temperatura'].value_counts(normalize=True)
p_R_given_C = df.groupby('Clima')['ProbabilidadLluvia'].value_counts(normalize=True)

# Comprobar la independencia condicional
independence = True
for clima, temp, prob_lluvia in df[['Clima', 'Temperatura', 'ProbabilidadLluvia']].values:
    p_T_R_given_C = p_T_given_C[clima][temp] * p_R_given_C[clima][prob_lluvia]
    p_T_R = (df['Temperatura'] == temp).mean() * (df['ProbabilidadLluvia'] == prob_lluvia).mean()
    if p_T_R_given_C != p_T_R:
        independence = False
        break

# Imprimir el resultado
if independence:
    print("La temperatura y la probabilidad de lluvia son independientes condicionalmente al clima.")
else:
    print("La temperatura y la probabilidad de lluvia no son independientes condicionalmente al clima.")
