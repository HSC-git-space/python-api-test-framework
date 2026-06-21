from api.base_client import BaseClient


class UserEndpoints(BaseClient):
    def get_all_users(self):
        return self.get("/users")

    def get_user_by_id(self, user_id):
        return self.get(f"/users/{user_id}")

    def create_user(self, payload):
        return self.post("/users", payload)

    def update_user(self, user_id, payload):
        return self.put(f"/users/{user_id}", payload)

    def delete_user(self, user_id):
        return self.delete(f"/users/{user_id}")


class PostEndpoints(BaseClient):
    def get_all_posts(self):
        return self.get("/posts")

    def get_post_by_id(self, post_id):
        return self.get(f"/posts/{post_id}")

    def create_post(self, payload):
        return self.post("/posts", payload)

    def update_post(self, post_id, payload):
        return self.put(f"/posts/{post_id}", payload)

    def delete_post(self, post_id):
        return self.delete(f"/posts/{post_id}")