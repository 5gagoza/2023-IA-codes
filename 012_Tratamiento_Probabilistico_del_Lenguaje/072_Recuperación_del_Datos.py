"""
La recuperación de datos se refiere al proceso de encontrar y extraer información 
relevante de grandes conjuntos de datos textuales. Implica la utilización de técnicas 
probabilísticas para determinar la relevancia y la importancia de los documentos 
en función de una consulta o un conjunto de palabras clave.
"""
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class InformationRetrievalSystem:
    def __init__(self, documents):
        self.documents = documents
        self.vectorizer = TfidfVectorizer() 
        self.vectorized_docs = self.vectorizer.fit_transform(self.documents) #Convertir documentos a vectores

    def search(self, query): #Consulta para obtener los resultados
        query_vec = self.vectorizer.transform([query])
        similarity_scores = cosine_similarity(query_vec, self.vectorized_docs)
        sorted_scores = np.argsort(similarity_scores, axis=1)[0][::-1]
        return [(doc_id, similarity_scores[0, doc_id]) for doc_id in sorted_scores]

    def display_results(self, query, sorted_scores, num_results=5): #Muestra los resultados 
        print("Query:", query)
        print("Results:")
        for doc_id, score in sorted_scores[:num_results]:
            print(f"Document ID: {doc_id}, Score: {score}")
            print(self.documents[doc_id])
            print("--------------------")

# Ejemplo de uso
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]
ir_system = InformationRetrievalSystem(documents)
query = "document"
results = ir_system.search(query)
ir_system.display_results(query, results)
