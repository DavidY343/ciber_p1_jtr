import bcrypt
from concurrent.futures import ThreadPoolExecutor

# Cargar las contraseñas crackeadas del otro foro (usuario:contraseña)
def load_cracked_passwords(file_path):
    cracked_passwords = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if ':' in line:
                user, password = line.strip().split(":")
                cracked_passwords[user] = password
    return cracked_passwords

# Cargar el archivo de hashes bcrypt del nuevo foro (usuario:hash)
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
        return password  # Si la contraseña es correcta, la devolvemos
    return None  # Si la contraseña es incorrecta, devolvemos None

# Función para intentar romper el hash utilizando la contraseña del otro foro
def crack_bcrypt_with_known_password(cracked_passwords, user, bcrypt_hash):
    if user in cracked_passwords:  # Comprobamos si el nombre de usuario está en el diccionario de contraseñas crackeadas
        password = cracked_passwords[user]
        if try_password(password, bcrypt_hash):
            return user, password  # Devolvemos el usuario y la contraseña encontrada
    return None

if __name__ == "__main__":
    # Cargar las contraseñas crackeadas del otro foro
    cracked_passwords = load_cracked_passwords("passwd_crack.txt")  # Cambia por el archivo de contraseñas ya crackeadas

    # Cargar los pares usuario:hash del nuevo foro
    user_hash_list = load_hash_file("g21_meneate.txt")  # Cambia por tu archivo de hashes bcrypt

    results = []  # Lista para almacenar los resultados encontrados

    # Usar ThreadPoolExecutor para intentar romper cada hash usando las contraseñas del otro foro
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(crack_bcrypt_with_known_password, cracked_passwords, user, bcrypt_hash): user 
                   for user, bcrypt_hash in user_hash_list}

        for future in futures:
            result = future.result()  # Obtener el resultado del hilo
            if result:
                results.append(f"{result[0]}:{result[1]}")  # Agregar el resultado encontrado a la lista
                print(f"{result[0]}:{result[1]}")  # Imprimir en consola

    # Escribir los resultados en un archivo
    with open("passwd_meneate.txt", 'w', encoding='utf-8') as output_file:
        for line in results:
            output_file.write(line + "\n")
    
    print(f"Total de contraseñas encontradas: {len(results)}.")
