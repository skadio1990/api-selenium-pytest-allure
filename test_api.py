import utils
import allure

DO = utils.UserRequest

# Create instances of users 
valid_user = DO(name="User", id="1")
valid_user_2 = DO(name="User2", id="1")
invalid_user = DO(name="User", id=1)
empty_user = DO(name="", id="")

@utils.allure_data("Get All Users (Start)", 
                   "Description", "CRITICAL")
def test_get_all_users_start():
    response = DO.get_all_users()
    with allure.step(f"response text: {response.text}"):
        pass
    with allure.step("Assert Status Code 200"):
        assert response.status_code == 200
    with allure.step("Assert No Duplicates"):
        assert utils.has_duplicates(response.text, 'id') == False
    

@utils.allure_data("Create Valid User", 
                   "Description", "Severity")
def test_post_valid_user():
    response = DO.post(valid_user)
    with allure.step(f"response text: {response.text}"):
        pass
    with allure.step("Assert Status Code 200"):
        assert response.status_code == 200 


@utils.allure_data("Get User By ID", 
                   "Description", "CRITICAL")
def test_get_user_id():
    response = DO.get_user(valid_user)
    with allure.step(f"response text: {response.text}"):
        pass
    with allure.step("Assert Status Code 200"):
        assert response.status_code == 200


@utils.allure_data("Update User By ID", 
                   "Description", "CRITICAL")
def test_update_user_id():
    response = DO.put(valid_user)
    with allure.step(f"response text: {response.text}"):
        pass
    with allure.step("Assert Status Code 200"):
        assert response.status_code == 200
    with allure.step("Assert User Name Changed"):
        print(DO.get_user(valid_user).text)
        print(valid_user_2.data())
        assert DO.get_user(valid_user).text == valid_user_2.data()


@utils.allure_data("Delete Valid User", 
                   "Description", "Severity")
def test_delete_valid_user():
    response = DO.delete(valid_user)
    with allure.step(f"response text: {response.text}"):
        pass
    with allure.step("Assert Status Code 200"):
        assert response.status_code == 200


@utils.allure_data("Create Duplicate User", 
                   "Description", "Severity")
def test_post_duplicate_user():
    response = DO.post(valid_user)
    with allure.step(f"response text: {response.text}"):
        pass
    with allure.step("Assert Status Code Not 200"):
        assert response.status_code != 200 


@utils.allure_data("Create Invalid User", 
                   "Description", "Severity")
def test_post_invalid_user():
    response = DO.post(invalid_user)
    with allure.step(f"response text: {response.text}"):
        pass
    with allure.step("Assert Status Code not 200"):
        assert response.status_code != 200


@utils.allure_data("Delete Invalid User", 
                   "Description", "Severity")
def test_delete_user():
    response = DO.delete(invalid_user)
    with allure.step(f"response text: {response.text}"):
        pass
    with allure.step("Assert Status Code 200"):
        assert response.status_code == 200


@utils.allure_data("Create Empty User", 
                   "Description", "Severity")
def test_post_empty_user():
    response = DO.post(empty_user)
    with allure.step(f"response text: {response.text}"):
        pass
    with allure.step("Assert Status Code not 200"):
        assert response.status_code != 200


@utils.allure_data("Create Empty Object", 
                   "Description", "Severity")
def test_post_none_user():
    response = DO.post_none()
    with allure.step(f"response text: {response.text}"):
        pass
    with allure.step("Assert Status Code not 200"):
        assert response.status_code != 200


@utils.allure_data("Incorrectly Format Header", 
                   "Description", "Severity")
def test_post_null_user():
    response = DO.post_null()
    with allure.step(f"response text: {response.text}"):
        pass
    with allure.step("Assert Status Code not 200"):
        assert response.status_code != 200


@utils.allure_data("Get All Users (End)", 
                   "Description", "CRITICAL")
def test_get_all_users_begin():
    response = DO.get_all_users()
    with allure.step(f"response text: {response.text}"):
        pass
    with allure.step("Assert Status Code 200"):
        assert response.status_code == 200
    with allure.step("Assert No Duplicates"):
        assert utils.has_duplicates(response.text, 'id') == False
    
