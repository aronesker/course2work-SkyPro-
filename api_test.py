from main import app


keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

def test_posts():
    with app.test_client() as client:
        response = client.get('/api/posts')
        assert response.status_code == 200
        assert isinstance(response.json, list)
        for entity in response.json:
            assert set(entity.keys()) == keys_should_be
            

def test_post():
    with app.test_client() as client:
        response = client.get('/api/posts/1')
        assert response.status_code == 200
        assert isinstance(response.json, dict)
        assert set(response.json.keys()) == keys_should_be

