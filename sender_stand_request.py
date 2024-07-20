import configuration
import requests
import data

# Función para crear un nuevo usuario
def post_new_user(body):
    try:
        response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                                 json=body,
                                 headers=data.headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error creating new user: {e}")
        return None

# Función que retorna los valores existentes en la tabla de usuarios
def get_users_table():
    try:
        response = requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching users table: {e}")
        return None

# Función que crea un nuevo kit del usuario
def post_new_kit(kit, auth_token):
    try:
        current_headers = data.headers.copy()
        current_headers["Authorization"] = "Bearer " + auth_token
        response = requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                                 json=kit,
                                 headers=current_headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error creating new kit: {e}")
        return None

def main():
    # Crear un nuevo usuario y obtener el token de autenticación
    user_response = post_new_user(data.user_body)
    if user_response is not None:
        print(user_response.status_code)
        auth_token = user_response.json().get('authToken')
        if auth_token:
            print(auth_token)

            # Obtener la tabla de usuarios
            user_table_response = get_users_table()
            if user_table_response is not None:
                print(user_table_response.status_code)
                print(user_table_response.text)

            # Crear un nuevo kit para el usuario
            kit_response = post_new_kit(data.kit_body, auth_token)
            if kit_response is not None:
                print(kit_response.status_code)
                print(kit_response.text)
        else:
            print("Failed to obtain auth token from response.")
    else:
        print("Failed to create new user.")

if __name__ == "__main__":
    main()



