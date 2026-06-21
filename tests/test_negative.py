import pytest
import allure
from requests.exceptions import HTTPError


@allure.feature("Negative Tests")
class TestNegative:

    @allure.story("Get non-existent user")
    @pytest.mark.negative
    def test_get_invalid_user(self, user_client):
        with pytest.raises(HTTPError) as exc_info:
            user_client.get_user_by_id(99999)
        assert exc_info.value.response.status_code == 404

    @allure.story("Get non-existent post")
    @pytest.mark.negative
    def test_get_invalid_post(self, post_client):
        with pytest.raises(HTTPError) as exc_info:
            post_client.get_post_by_id(99999)
        assert exc_info.value.response.status_code == 404

    @allure.story("Create user with empty payload")
    @pytest.mark.negative
    def test_create_user_empty_payload(self, user_client):
        response = user_client.create_user({})
        assert response.status_code == 201

    @allure.story("Create post with missing fields")
    @pytest.mark.negative
    def test_create_post_missing_fields(self, post_client):
        payload = {"title": "Incomplete Post"}
        response = post_client.create_post(payload)
        assert response.status_code == 201