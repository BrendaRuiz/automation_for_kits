import configuration
import requests
import data

#Función para crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json()['authToken'])

#Función que retorna los valores existentes en la tabla de usuarios
'''
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response_user_table = get_users_table()

print(response_user_table.status_code)
print(response_user_table.text)
'''

#Función que crea un nuevo kit del usuario
def post_new_kit(kit):
    current_headers = data.headers.copy()
    current_headers["Authorization"] = "Bearer " + response.json()["authToken"]
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json= kit,
                         headers= current_headers)

response_kit = post_new_kit(data.kit_body)
print((response_kit.status_code))
print(response_kit.text)


