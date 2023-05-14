"""
Las gramáticas probabilísticas lexicalizadas son una extensión de las PCFG 
que tienen en cuenta información léxica, como las palabras y sus características.
Estas gramáticas asignan probabilidades no solo a las reglas de producción, sino
también a las palabras y sus combinaciones. Permiten capturar mejor las dependencias 
entre las palabras y mejorar la precisión en la generación y el análisis de oraciones.
"""
""" el código define una gramática probabilística lexicalizada y utiliza el algoritmo de 
Viterbi para realizar análisis sintáctico en una oración dada """

import nltk

# Definir la gramática probabilística lexicalizada
# Reglas de producción para frases nominales (NP), frases verbales (VP), 
# preposiciones y sustantivos (PP), determinantes (Det), verbos (V) y preposiciones (P).
grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.6] | Det N PP [0.4]
    VP -> V [0.3] | V NP [0.4] | V NP PP [0.3]
    PP -> P NP [1.0]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'dog' [0.3] | 'cat' [0.3] | 'man' [0.4]
    V -> 'chased' [0.5] | 'saw' [0.5]
    P -> 'in' [0.6] | 'on' [0.4]
""")

# Crear un parser para la gramática
parser = nltk.ViterbiParser(grammar)

# Analizar una oración utilizando el parser
sentence = "the dog chased a cat".split()
trees = parser.parse(sentence)

# Mostrar los árboles de análisis sintáctico generados
for tree in trees:
    print(tree)


