#!/bin/bash

# Nombre del archivo que contiene los nombres de usuario y hashes
input_file="passwd_crack.txt"
# Nombre del archivo de salida para la wordlist
output_file="used_passwd.txt"

# Limpiamos el archivo de salida antes de empezar
> "$output_file"

# Leer el archivo línea por línea
while IFS=: read -r username paswwd; do
    # Extraer solo el nombre de usuario (parte antes del ":")
    echo "$passwd" >> "$output_file"
done < "$input_file"

echo "Wordlist generada en $output_file"