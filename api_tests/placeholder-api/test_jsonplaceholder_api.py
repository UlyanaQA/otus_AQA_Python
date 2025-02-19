import pytest

def test_get_all_posts(api_client):
    response = api_client.get_all_posts()
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) == 100
    assert all(key in posts[0] for key in ['userId', 'id', 'title', 'body'])

@pytest.mark.parametrize("post_id,expected_user", [
    (1, 1),
    (50, 5),
    (100, 10)
])
def test_get_post_by_id(api_client, post_id, expected_user):
    response = api_client.get_post_by_id(post_id)
    assert response.status_code == 200
    post = response.json()
    assert post['id'] == post_id
    assert post['userId'] == expected_user

def test_create_post(api_client):
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = api_client.create_post(new_post)
    assert response.status_code == 201
    created_post = response.json()
    assert created_post['id'] == 101  # API всегда возвращает 101 для новых постов

@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_get_posts_by_user(api_client, user_id):
    response = api_client.get_posts_by_user(user_id)
    assert response.status_code == 200
    posts = response.json()
    assert all(post['userId'] == user_id for post in posts)

def test_get_comments_for_post(api_client):
    response = api_client.get_comments_for_post(1)
    assert response.status_code == 200
    comments = response.json()
    assert len(comments) == 5
    assert all(comment['postId'] == 1 for comment in comments)

def test_delete_post(api_client):
    response = api_client.delete_post(1)
    assert response.status_code == 200