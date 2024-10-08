#!/bin/bash

# Nombre del archivo que contiene los nombres de usuario y hashes
input_file="g21_foromotos.txt"
# Nombre del archivo de salida para la wordlist
output_file="names_foromotos.txt"

# Limpiamos el archivo de salida antes de empezar
> "$output_file"

# Leer el archivo línea por línea
while IFS=: read -r username hash; do
    # Extraer solo el nombre de usuario (parte antes del ":")
    echo "$username" >> "$output_file"
done < "$input_file"

echo "Wordlist generada en $output_file"
