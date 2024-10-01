# Script para generar un diccionario personalizado
from itertools import product
import string

# Generar combinaciones alfanuméricas de 5 y 6 caracteres (minúsculas y algunas con símbolos)
chars = string.ascii_lowercase + string.digits
combinations = [''.join(i) for i in product(chars, repeat=5)] + [''.join(i) for i in product(chars, repeat=6)]

# Agregar palabras comunes en español
spanish_words = ['contraseña', 'secreto', 'usuario', 'clave', 'hack', 'admin']  # Agrega más palabras comunes

# Escribir en un archivo
with open("custom_dict.txt", "w") as f:
    for combo in combinations + spanish_words:
        f.write(combo + "\n")
