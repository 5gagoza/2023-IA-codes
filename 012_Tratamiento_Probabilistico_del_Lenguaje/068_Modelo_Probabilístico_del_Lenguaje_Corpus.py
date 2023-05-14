"""
representación estadística de la estructura y la probabilidad de las oraciones en un idioma.
Se basa en la idea de que la probabilidad de una oración se puede calcular en función 
de la probabilidad de sus palabras y su orden. Estos modelos se construyen a partir de un corpus
que es un conjunto de textos de ejemplo en un idioma determinado. Puede ser un conjunto de 
documentos escritos, transcripciones de voz u otros tipos de datos lingüísticos.
"""

import nltk
from nltk.util import ngrams
from collections import defaultdict

class LanguageModel: #Modelo probabilistico de lenguaje
    def __init__(self, ngram): #ngram es para representar el tamano que se utilizara en el modelo
        self.ngram = ngram
        self.ngram_counts = defaultdict(int)  # Diccionario para almacenar los recuentos de los n-gramas
        self.context_counts = defaultdict(int)  # Diccionario para almacenar los recuentos de los contextos (n-1 gramas)

    def train(self, corpus): #Entrenamiento del modelo con un corpus
        for sentence in corpus:
            tokens = sentence.split()  # Dividir la oración en tokens
            ngrams = self.generate_ngrams(tokens)  # Generar los n-gramas del texto
            for ngram in ngrams:
                context = " ".join(ngram[:-1])  # Obtener el contexto (n-1 gramas)
                self.ngram_counts[ngram] += 1  # Incrementar el recuento del n-grama
                self.context_counts[context] += 1  # Incrementar el recuento del contexto

    def generate_ngrams(self, tokens):
        ngrams = []
        for i in range(len(tokens) - self.ngram + 1):
            ngram = tuple(tokens[i:i+self.ngram])  # Crear el n-grama a partir de los tokens
            ngrams.append(ngram)
        return ngrams

    def probability(self, word, context):
        context_count = self.context_counts[context]  # Obtener el recuento del contexto
        ngram = tuple(context.split() + [word])  # Crear el n-grama a partir del contexto y la palabra
        ngram_count = self.ngram_counts[ngram]  # Obtener el recuento del n-grama específico
        if context_count == 0:
            return 0.0
        return ngram_count / context_count  # Calcular la probabilidad dividiendo el recuento del n-grama entre el recuento del contexto

# Ejemplo de uso
corpus = [
    "the cat sat on the mat",
    "the dog ate my homework",
    "the cat and the dog are friends"
]

ngram = 2
lm = LanguageModel(ngram)  # Crear una instancia del modelo de lenguaje con el tamaño del n-grama especificado
lm.train(corpus)  # Entrenar el modelo con el corpus de texto

context = "the cat"
word = "sat"
probability = lm.probability(word, context)  # Calcular la probabilidad de la palabra dada el contexto según el modelo
print("Probabilidad:", probability)
