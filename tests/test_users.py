import pytest
from models.user_model import UserModel
import allure


@allure.feature("Users API")
class TestUsers:

    @allure.story("Get all users")
    @pytest.mark.smoke
    def test_get_all_users(self, user_client):
        response = user_client.get_all_users()
        assert response.status_code == 200
        users = response.json()
        assert len(users) > 0
        assert isinstance(users, list)

    @allure.story("Get user by ID")
    @pytest.mark.smoke
    def test_get_user_by_id(self, user_client):
        response = user_client.get_user_by_id(1)
        assert response.status_code == 200
        user = UserModel(**response.json())
        assert user.id == 1
        assert user.name is not None
        assert "@" in user.email

    @allure.story("Create user")
    @pytest.mark.regression
    def test_create_user(self, user_client):
        payload = {
            "name": "Rann Chandel",
            "username": "rann_test",
            "email": "rann@test.com"
        }
        response = user_client.create_user(payload)
        assert response.status_code == 201
        created = response.json()
        assert created["name"] == "Rann Chandel"
        assert "id" in created

    @allure.story("Update user")
    @pytest.mark.regression
    def test_update_user(self, user_client):
        payload = {"name": "Rann Updated"}
        response = user_client.update_user(1, payload)
        assert response.status_code == 200
        updated = response.json()
        assert updated["name"] == "Rann Updated"

    @allure.story("Delete user")
    @pytest.mark.regression
    def test_delete_user(self, user_client):
        response = user_client.delete_user(1)
        assert response.status_code == 200