#!/bin/bash
# Script para ejecutar el analizador semantico
temp_file=$(mktemp -t my_temp_file.XXXXXX)
echo "Ingresa todas las lineas a ejecutar. Presiona Ctrl+D para finalizar:"
while IFS= read -r line
do
    echo "$line" >> "$temp_file"
done
python semantic.py "$temp_file"
rm "$temp_file"