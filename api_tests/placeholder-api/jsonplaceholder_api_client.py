import requests


class JsonPlaceholderApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    # Posts endpoints
    def get_all_posts(self):
        return self.session.get(f"{self.base_url}/posts")

    def get_post_by_id(self, post_id):
        return self.session.get(f"{self.base_url}/posts/{post_id}")

    def create_post(self, data):
        return self.session.post(f"{self.base_url}/posts", json=data)

    def update_post(self, post_id, data):
        return self.session.put(f"{self.base_url}/posts/{post_id}", json=data)

    def delete_post(self, post_id):
        return self.session.delete(f"{self.base_url}/posts/{post_id}")

    # Users endpoints
    def get_all_users(self):
        return self.session.get(f"{self.base_url}/users")

    def get_user_by_id(self, user_id):
        return self.session.get(f"{self.base_url}/users/{user_id}")

    # Comments endpoints
    def get_comments_for_post(self, post_id):
        return self.session.get(f"{self.base_url}/posts/{post_id}/comments")

    # Helper methods
    def get_posts_by_user(self, user_id):
        return self.session.get(f"{self.base_url}/posts?userId={user_id}")