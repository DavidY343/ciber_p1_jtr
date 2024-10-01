#!/bin/bash

# Asumiendo que la salida del programa se encuentra en un archivo llamado 'salida.txt'
# Si tu programa produce la salida directamente a la consola, puedes redirigirlo a este archivo.
# Por ejemplo: ./tu_programa > salida.txt

# Lee el archivo línea por línea
while read -r line; do
    # Extrae el nombre de usuario y el nombre entre paréntesis
    user=$(echo "$line" | awk '{print $2}' | tr -d '()')
    name=$(echo "$line" | awk '{print $1}')
    
    # Imprime en el formato deseado
    echo "$user:$name"
done < salida.txt
