"""
La traducción automática estadística es un enfoque de traducción que 
utiliza modelos probabilísticos para encontrar la mejor traducción 
posible de una oración en un idioma de origen a un idioma de destino.
Se basa en alineaciones estadísticas entre oraciones paralelas en 
ambos idiomas y utiliza modelos de traducción probabilísticos para 
generar las mejores traducciones posibles.
"""
from transformers import MarianMTModel, MarianTokenizer

def translate_text(text):
    # Carga el modelo y el tokenizador preentrenados
    model_name = 'Helsinki-NLP/opus-mt-en-es'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokeniza y codifica el texto de entrada
    input_ids = tokenizer.encode(text, return_tensors='pt')

    # Realiza la traducción
    translated_ids = model.generate(input_ids)

    # Decodifica y retorna el texto traducido
    translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)
    return translated_text

# Ejemplo de uso
english_text = "I like cats."
translated_text = translate_text(english_text)
print(translated_text)
