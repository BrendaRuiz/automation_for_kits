import sender_stand_request
import data

#Esta función cambia el valor del parámetro 'name'
def get_user_kit(user_kit):
    #El diccionario que contiene el cuerpo de solicitud se copia del archivo "data.py"
    #para conservar los datos del diccionario de origen
    current_kit_body = data.kit_body.copy()
    #Se cambia el valor del parámetro 'name'
    current_kit_body["name"] = user_kit
    #Se devuelve un nuevo diccionario con el valor 'name' requerido
    return current_kit_body

#Función de prueba positiva
def positive_assert(user_kit):
    #El cuerpo de la solicitud actualizada se guarda en la variable user_kit_body
    user_kit_body = get_user_kit(user_kit)
    #Se crea un nuevo usuario para obtener un authToken que servirá para crear un
    #nuevo kit posteriormente
    sender_stand_request.post_new_user(data.user_body)
    #El resultado de la solicitud para crear un nuevo kit se guarda
    #en la variable response_new_kit
    response_new_kit = sender_stand_request.post_new_kit(user_kit_body)
    #Comprueba si el código de estado es 201
    assert response_new_kit.status_code == 201
    # Comprueba si el parámetro 'name' es igual entre el cuerpo de la respuesta
    #y el cuerpo de la solicitud
    assert response_new_kit.json()["name"] == user_kit_body["name"]

#Función de prueba negativa
def negative_assert_symbol(user_kit):
    #El cuerpo de la solicitud actualizada se guarda en la variable user_kit_body
    user_kit_body = get_user_kit(user_kit)
    #Se crea un nuevo usuario para obtener un authToken que servirá para crear un
    #nuevo kit posteriormente
    sender_stand_request.post_new_user(data.user_body)
    #El resultado de la solicitud para crear un nuevo kit se guarda
    #en la variable response_new_kit
    response_new_kit = sender_stand_request.post_new_kit(user_kit_body)
    #Comprueba si el código de estado es 400
    assert response_new_kit.status_code == 400

#Función de prueba negativa
#Esta función servirá para la prueba 8 donde no se enviará el parametro 'name'
def negative_assert_no_name(kit_body):
    #Se crea un nuevo usuario para obtener un authToken que servirá para crear un
    #nuevo kit posteriormente
    sender_stand_request.post_new_user(data.user_body)
    #El resultado de la solicitud para crear un nuevo kit se guarda
    #en la variable response_new_kit
    response_new_kit = sender_stand_request.post_new_kit(kit_body)
    #Comprueba si el código de estado es 400
    assert response_new_kit == 400


#Prueba 1. Creación de un nuevo kit del usuario
#El parametro 'name' contiene un caracter
def test_create_user_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

#Prueba 2. Creación de un nuevo kit del usuario
#El parametro 'name' contiene quinientos once caracteres
def test_create_user_kit_511_letter_in_name_get_success_response():
    positive_assert(data.kit_body_test_2)

#Prueba 3. Creación de un nuevo kit del usuario
#El parametro 'name' contiene cero caracteres
def test_create_user_kit_empty_name_get_error_response():
    negative_assert_symbol("")

#Prueba 4. Creación de un nuevo kit del usuario
#El parametro 'name' contiene quinientos doce caracteres
def test_create_user_kit_512_letter_in_name_get_error_response():
    negative_assert_symbol(data.kit_body_test_4)

#Prueba 5. Creación de un nuevo kit del usuario
#El parametro 'name' permite caracteres especiales
def test_create_user_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

#Prueba 6. Creación de un nuevo kit del usuario
#El parametro 'name' permite espacios
def test_create_user_kit_has_space_in_name_get_success_response():
    positive_assert("A Aaa")

#Prueba 7. Creación de un nuevo kit del usuario
#El parametro 'name' permite números
def test_create_user_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")

#Prueba 8. Creación de un nuevo kit del usuario
#La solicitud no contiene el parametro 'name'
def test_create_user_kit_no_name_get_error_response():
    #El diccionario que contiene el cuerpo de solicitud se copia del archivo "data.py"
    #para conservar los datos del diccionario de origen
    kit_body = data.kit_body.copy()
    #Se elimina el parametro 'name' de la variable copiada
    kit_body.pop("name")
    #Se ejecuta la funcion con el nuevo cuerpo de la solicitud donde
    #se elimino el parámetro 'name'
    negative_assert_no_name(kit_body)

#Prueba 9. Creación de un nuevo kit del usuario
#El parametro 'name' contiene un tipo de dato diferente (int)
def test_create_user_kit_has_data_type_number_in_name_get_error_response():
    negative_assert_symbol(123)