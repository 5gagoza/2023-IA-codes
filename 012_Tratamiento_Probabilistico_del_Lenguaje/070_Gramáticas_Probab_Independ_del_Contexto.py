"""
Las gramáticas probabilísticas independientes del contexto son modelos 
gramaticales que asignan probabilidades a las reglas de producción de una gramática.
Estas gramáticas se utilizan para generar y analizar oraciones en un lenguaje natural.
Cada regla de producción tiene asociada una probabilidad, lo que permite evaluar
la probabilidad de una oración generada por la gramática.
"""

import random
import nltk

# Crear una PCFG
pcfg = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.6] | Det N PP [0.4]
    VP -> V NP [0.7] | V NP PP [0.3]
    PP -> P NP [1.0]
    Det -> 'the' [0.5] | 'a' [0.5]
    N -> 'dog' [0.6] | 'cat' [0.4]
    V -> 'chased' [1.0]
    P -> 'on' [0.6] | 'over' [0.4]
""")

# Generar una oración aleatoria según la PCFG
def generate_sentence(grammar, symbol='S'):
    productions = grammar.productions(lhs=nltk.Nonterminal(symbol))
    production = random.choice(productions)
    sentence = []

    for sym in production.rhs():
        if isinstance(sym, nltk.Nonterminal):
            sentence.extend(generate_sentence(grammar, sym.symbol()))
        else:
            sentence.append(sym)

    return sentence

sentence = generate_sentence(pcfg) #Oración generada

# Imprimir la oración generada
print(' '.join(sentence))
