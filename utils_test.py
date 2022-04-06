import pytest
from utils import get_posts_all, get_comments_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, \
    get_post_by_pk


def test_get_posts_all():

    result = get_posts_all()
    assert result is not None, 'ошибка вывода данных'


def test_get_comments_all():

    result = get_comments_all()
    assert result is not None, 'ошибка вывода данных'


def test_get_posts_by_user():

    result = get_posts_by_user('larry')['poster_name']
    assert result is not None, 'ошибка вывода пользователя'
    assert result == 'larry', 'ошибка вывода пользователя'


def test_get_comments_by_post_id():

    result = get_comments_by_post_id(1)
    assert result is not None, 'ошибка вывода комментария'
    assert result[0]['post_id'] == 1, 'ошибка вывода комментария'


def test_search_for_posts():

    result = search_for_posts('утром')
    assert result is not None, 'ошибка вывода поста'
    assert result[0]['pk'] == 4, 'ошибка вывода поста'


@pytest.mark.parametrize('test_input', [-1, 0, 3, 7, 99])
def test_get_post_by_pk(test_input):

    result = get_post_by_pk(test_input)
    count_posts = len(get_posts_all())

    if 0 < test_input < count_posts:
        assert result is not None, 'ошибка вывода поста'
        assert result['pk'] == test_input, 'ошибка вывода поста'
    else:
        return 'такого поста не существует'
