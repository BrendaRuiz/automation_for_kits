import sender_stand_request
import data

#Esta función cambia el valor del parámetro 'name'
def get_user_kit(user_kit):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = user_kit
    return current_kit_body

#Función de prueba positiva
def positive_assert(user_kit):
    user_kit_body = get_user_kit(user_kit)
    sender_stand_request.post_new_user(data.user_body)
    response_new_kit = sender_stand_request.post_new_kit(user_kit_body)
    assert response_new_kit.status_code == 201
    assert response_new_kit.json()["name"] == user_kit_body["name"]

#Función de prueba negativa
def negative_assert_symbol(user_kit):
    user_kit_body = get_user_kit(user_kit)
    sender_stand_request.post_new_user(data.user_body)
    response_new_kit = sender_stand_request.post_new_kit(user_kit_body)
    assert response_new_kit.status_code == 400

#Función de prueba negativa
def negative_assert_no_name(kit_body):
    sender_stand_request.post_new_user(data.user_body)
    response_new_kit = sender_stand_request.post_new_kit(kit_body)
    assert response_new_kit == 400


#Prueba 1. El parametro 'name' contiene un caracter
def test_create_user_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

#Prueba 2. El parametro 'name' contiene quinientos once caracteres
def test_create_user_kit_511_letter_in_name_get_success_response():
    positive_assert(data.kit_body_test_2)

#Prueba 3. El parametro 'name' contiene cero caracteres
def test_create_user_kit_empty_name_get_error_response():
    negative_assert_symbol("")

#Prueba 4. El parametro 'name' contiene quinientos doce caracteres
def test_create_user_kit_512_letter_in_name_get_error_response():
    negative_assert_symbol(data.kit_body_test_4)

#Prueba 5. El parametro 'name' permite caracteres especiales
def test_create_user_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

#Prueba 6. El parametro 'name' permite espacios
def test_create_user_kit_has_space_in_name_get_success_response():
    positive_assert("A Aaa")

#Prueba 7.El parametro 'name' permite números
def test_create_user_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")

#Prueba 8. La solicitud no contiene el parametro 'name'
def test_create_user_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

#Prueba 9.El parametro 'name' contiene un tipo de dato diferente (int)
def test_create_user_kit_has_data_type_number_in_name_get_error_response():
    negative_assert_symbol(123)