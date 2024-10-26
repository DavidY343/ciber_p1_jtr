import bcrypt
from concurrent.futures import ThreadPoolExecutor
import time

# Cargar las contraseñas crackeadas de foromotos (usuario:contraseña)
def load_cracked_passwords(file_path):
	cracked_passwords = {}
	with open(file_path, 'r', encoding='utf-8') as f:
		for line in f:
			if ':' in line:
				user, password = line.strip().split(":")
				cracked_passwords[user] = password
	return cracked_passwords

# Cargar el archivo de hashes bcrypt de meneate (usuario:hash)
def load_hash_file(file_path):
	user_hash_list = []
	with open(file_path, 'r') as f:
		for line in f:
			user, bcrypt_hash = line.strip().split(":")
			user_hash_list.append((user, bcrypt_hash.encode('utf-8')))
	return user_hash_list

# Función que intenta una contraseña contra un hash bcrypt específico
def try_password(password, bcrypt_hash):
	password_bytes = password.encode('utf-8')
	if bcrypt.checkpw(password_bytes, bcrypt_hash):
		return password
	return None

# Función para intentar romper el hash utilizando la contraseña de foormotos
def crack_bcrypt_with_known_password(cracked_passwords, user, bcrypt_hash):
	if user in cracked_passwords:
		password = cracked_passwords[user]
		if try_password(password, bcrypt_hash):
			return user, password
	return None

def main():
	start_time = time.time()
	cracked_passwords = load_cracked_passwords("cracked_passwd_foromotos.txt") 
	user_hash_list = load_hash_file("g21_meneate.txt")
	results = []

	with ThreadPoolExecutor(max_workers=8) as executor:
		futures = {executor.submit(crack_bcrypt_with_known_password, cracked_passwords, user, bcrypt_hash): user 
				for user, bcrypt_hash in user_hash_list}
		for future in futures:
			result = future.result()
			if result:
				results.append(f"{result[0]}:{result[1]}")

	# Escribir los resultados en un archivo
	with open("cracked_passwd_meneate.txt", 'w', encoding='utf-8') as output_file:
		for line in results:
			output_file.write(line + "\n")
	
	print(f"Total de contraseñas encontradas: {len(results)}.")
	print(f"Tiempo total: {time.time() - start_time} segundos.")

if __name__ == "__main__":
	main()