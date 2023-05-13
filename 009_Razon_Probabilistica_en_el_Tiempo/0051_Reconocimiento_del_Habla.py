"""
El código implementa un reconocimiento de voz utilizando la biblioteca de Python speech_recognition. 
Primero, se utiliza la función sr.Microphone() para detectar el micrófono del dispositivo y luego se llama a la función recognize_google() de speech_recognition 
para transcribir lo que se dice en el micrófono a texto. Luego, se imprime el texto transcribido en la consola.
"""

import speech_recognition as sr

# Creamos un objeto recognizer
r = sr.Recognizer()

# Definimos la fuente de audio, en este caso utilizamos el micrófono
with sr.Microphone() as source:
    print("Habla ahora...")
    # Escuchamos el audio del micrófono
    audio = r.listen(source)

try:
    # Utilizamos la función recognize_google para convertir el audio a texto utilizando el servicio de Google
    text = r.recognize_google(audio, language="es-ES")
    print("Google Speech Recognition ha interpretado: " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition no ha podido entender el audio")
except sr.RequestError as e:
    print("No se puede conectar con el servicio de Google Speech Recognition; {0}".format(e))
