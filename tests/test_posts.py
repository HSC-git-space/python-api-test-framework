import pytest
import allure


@allure.feature("Posts API")
class TestPosts:

    @allure.story("Get all posts")
    @pytest.mark.smoke
    def test_get_all_posts(self, post_client):
        response = post_client.get_all_posts()
        assert response.status_code == 200
        posts = response.json()
        assert len(posts) > 0
        assert isinstance(posts, list)

    @allure.story("Get post by ID")
    @pytest.mark.smoke
    def test_get_post_by_id(self, post_client):
        response = post_client.get_post_by_id(1)
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == 1
        assert "title" in post
        assert "body" in post

    @allure.story("Create post")
    @pytest.mark.regression
    def test_create_post(self, post_client):
        payload = {
            "title": "Test Post by Rann",
            "body": "This is a test post body",
            "userId": 1
        }
        response = post_client.create_post(payload)
        assert response.status_code == 201
        created = response.json()
        assert created["title"] == "Test Post by Rann"
        assert "id" in created

    @allure.story("Update post")
    @pytest.mark.regression
    def test_update_post(self, post_client):
        payload = {"title": "Updated Post Title"}
        response = post_client.update_post(1, payload)
        assert response.status_code == 200
        updated = response.json()
        assert updated["title"] == "Updated Post Title"

    @allure.story("Delete post")
    @pytest.mark.regression
    def test_delete_post(self, post_client):
        response = post_client.delete_post(1)
        assert response.status_code == 200 