import matplotlib.pyplot as plt
import re
from collections import Counter

# Cargar las contraseñas crackeadas de foromotos (usuario:contraseña)
def leer_archivo(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip().split(":") for line in f.readlines()]



# 1. Verificar si hay pares duplicados
def duplicated_pairs(usuarios_contrasenas):
	pares_unicos = set(tuple(par) for par in usuarios_contrasenas)
	pares_duplicados = len(usuarios_contrasenas) - len(pares_unicos)
	
	duplicados_data = ['Duplicados', 'No duplicados']
	duplicados_cuenta = [pares_duplicados, len(usuarios_contrasenas) - pares_duplicados]

	print(f'Pares de Usuario-Contraseña Duplicados: {pares_duplicados}')
	print(f'Pares de Usuario-Contraseña No Duplicados: {len(usuarios_contrasenas) - pares_duplicados}')
	plt.figure(figsize=(6, 4))
	plt.bar(duplicados_data, duplicados_cuenta, color=['red', 'green'])
	plt.title('Pares de Usuario-Contraseña Duplicados vs No Duplicados')
	plt.ylabel('Cantidad')
	plt.show()

# 2. Longitud de las contraseñas y gráfico de barras
def longitud_contrasenas(usuarios_contrasenas):
	longitudes = [len(par[1]) for par in usuarios_contrasenas]
	longitudes_categoria = ['4', '5', '6', '7', '8', '9', '10', '11', '11+']
	longitudes_contador = Counter([str(l) if l < 12 else '11+' for l in longitudes])

	print('Longitudes de Contraseñas:')
	for longitud, cantidad in longitudes_contador.items():
		print(f'{longitud}: {cantidad}')

	plt.figure(figsize=(6, 4))
	plt.bar(longitudes_categoria, [longitudes_contador.get(l, 0) for l in longitudes_categoria], color='blue')
	plt.title('Distribución de Longitudes de Contraseñas')
	plt.xlabel('Longitud')
	plt.ylabel('Cantidad de Contraseñas')
	plt.show()


# 3. Contraseñas con números, caracteres especiales y sin ninguno de los dos
def contrasenas_numeros_especiales(usuarios_contrasenas):
	numeros_contador = sum(1 for par in usuarios_contrasenas if re.search(r'\d', par[1]))
	especiales_contador = sum(1 for par in usuarios_contrasenas if re.search(r'[^\w\s]', par[1]))
	sin_numeros_ni_especiales = sum(1 for par in usuarios_contrasenas if not re.search(r'\d', par[1]) and not re.search(r'[^\w\s]', par[1]))

	categorias = ['Números', 'Especiales', 'Sin Números ni Especiales']
	valores = [numeros_contador, especiales_contador, sin_numeros_ni_especiales]

	print(f'Contraseñas con Números: {numeros_contador}')
	print(f'Contraseñas con Caracteres Especiales: {especiales_contador}')
	print(f'Contraseñas sin Números ni Caracteres Especiales: {sin_numeros_ni_especiales}')
	plt.figure(figsize=(6, 4))
	plt.bar(categorias, valores, color=['orange', 'purple', 'gray'])
	plt.title('Contraseñas con Números, Caracteres Especiales y Ninguno')
	plt.ylabel('Cantidad de Contraseñas')
	plt.show()


# 4. Estadísticas sobre contraseñas únicas y usadas por varios usuarios
def contrasenas_unicas(usuarios_contrasenas):
	contador_contrasenas = Counter(par[1] for par in usuarios_contrasenas)
	contrasenas_unicas = sum(1 for count in contador_contrasenas.values() if count == 1)
	contrasenas_multis = sum(1 for count in contador_contrasenas.values() if count > 1)

	categorias_contrasenas = ['Únicas', 'Múltiples']
	valores_contrasenas = [contrasenas_unicas, contrasenas_multis]

	print(f'Contraseñas Únicas: {contrasenas_unicas}')
	print(f'Contraseñas Múltiples: {contrasenas_multis}')
	plt.figure(figsize=(6, 4))
	plt.bar(categorias_contrasenas, valores_contrasenas, color=['blue', 'orange'])
	plt.title('Contraseñas Únicas vs Múltiples Usuarios')
	plt.ylabel('Cantidad de Contraseñas')
	plt.show()

def main():
	file_path = 'g21_foromotos.txt'
	usuarios_contrasenas = leer_archivo(file_path)
	duplicated_pairs(usuarios_contrasenas)
	longitud_contrasenas(usuarios_contrasenas)
	contrasenas_numeros_especiales(usuarios_contrasenas)
	contrasenas_unicas(usuarios_contrasenas)

if __name__ == "__main__":
    main()