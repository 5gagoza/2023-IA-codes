
import nltk  # Importamos la biblioteca NLTK

#Guardamos la oracion en una variable string
oracion = "The cat is always sleeping"
#Tokenizamos la oracion (la dividimos en palabras para despues etiquetarla)
tokens = nltk.word_tokenize(oracion)

# Etiquetamos las partes de la oracion
etiquetado = nltk.pos_tag(tokens)

# Imprimimos los resultados
print(etiquetado)
