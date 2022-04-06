from flask import Flask, render_template, request

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user


app = Flask(__name__)


@app.route('/')
def page_main():
    """
    Главная страница.
    :return: представление, используя шаблон.
    """
    posts = get_posts_all()
    count_posts = len(posts)
    return render_template('index.html', posts=posts, count_posts=count_posts)


@app.route('/post/<int:post_id>')
def page_post(post_id):
    """
    Страница с постом
    :param post_id: идентификатор поста
    :return: представление, используя шаблон
    """
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    count_comments = len(comments)
    return render_template('post.html', post=post, comments=comments, count_comments=count_comments)


@app.route('/search')
def page_search():
    """
    Страница поиска
    :return: представление, используя шаблон
    """
    s = request.args.get('s', '')
    search_posts = search_for_posts(s)
    count_search_post = len(search_posts)
    max_out_posts = 10
    output_post = search_posts[:max_out_posts]
    return render_template('search.html', output_post=output_post, s=s, count_search_post=count_search_post)


@app.route('/users/<user_name>')
def page_user(user_name):
    """
    Посты пользователя по имени
    :param user_name: имя пользователя
    :return: представление, используя шаблон
    """
    user_posts = get_posts_by_user(user_name)
    return render_template('user-feed.html', user_posts=user_posts)


@app.route('/api/posts')
def api_posts():
    from flask import jsonify

    posts = get_posts_all()
    return jsonify(posts)


@app.route('/api/posts/<int:post_id>')
def api_post(post_id):
    from flask import jsonify

    post = get_post_by_pk(post_id)
    return jsonify(post)

if __name__ == '__main__':
    app.run()
