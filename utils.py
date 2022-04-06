import json


def get_posts_all():
    """
    Загружает данные из JSON файла
    """

    with open("data/data.json", encoding="utf-8") as f:
        posts = json.load(f)
    return posts


def get_comments_all():
    """
    Загружает данные из JSON файла
    """

    with open("data/comments.json", encoding="utf-8") as f:
        posts = json.load(f)
    return posts


def get_posts_by_user(user_name):
    """
    Возвращает данные по заданному параметру.
    :param user_name: Имя пользователя
    :return: Данные пользователя
    """
    list_posts_by_name = []
    posts = get_posts_all()

    for post in posts:
        if post["poster_name"] == user_name:
            list_posts_by_name.append(post)

    return list_posts_by_name


def get_comments_by_post_id(post_id):
    """
    Возвращает данные по заданному параметру.
    :param post_id: Идентификатор поста
    :return: Список комментариев к посту
    """

    comments = get_comments_all()
    comments_by_id = []

    for comment in comments:
        if comment["post_id"] == post_id:
            comments_by_id.append(comment)

    return comments_by_id


def search_for_posts(query):
    """
    Возвращает данные по заданному параметру.
    :param query: Ключевое слово
    :return: Данные, содержащие ключевое слово
    """

    posts_found = []
    query_lower = query.lower()
    posts = get_posts_all()

    for post in posts:
        if query_lower in post['content'].lower():
            posts_found.append(post)

    return posts_found


def get_post_by_pk(pk):
    """
    Возвращает данные по заданному параметру.
    :param pk: Идентификатор поста
    :return: Данные поста
    """

    posts = get_posts_all()

    for post in posts:
        if post["pk"] == pk:
            return post
