import pytest

from schemas.post_models.post import Post
from schemas.post_models.posts import Posts
from schemas.user_models.user import User
from schemas.user_models.users import Users
from utils import assert_utils
from utils.file_utils import get_file_contents


def test_send_get_requests_to_get_posts():
    posts = Posts.get_all_posts()
    assert posts.is_posts_sorted()


@pytest.mark.parametrize('post_user_id, post_id', [(10, 99)])
def test_send_get_request_to_get_post(post_user_id, post_id):
    post = Post.get_post(post_id)
    assert_utils.is_post_correct(post, post_user_id, post_id)


@pytest.mark.parametrize('post_id', [150])
def test_send_get_request_to_get_no_such_post(post_id):
    Post.get_no_such_post(post_id)


@pytest.mark.parametrize('expected_post', [Post(userId=1, id=101, title='AlexExample', body='example_body')])
def test_create_post(expected_post):
    post = Post.add_post(expected_post)
    assert_utils.is_created_post_correct(post, expected_post)


@pytest.mark.parametrize('actual_user_number, expected_user',
                         [(4, User(**get_file_contents("templates/user5.json")))])
def test_get_user_from_users(actual_user_number, expected_user):
    users = Users.get_users()
    assert users[actual_user_number] == expected_user, 'The returned user_models is not expected'


@pytest.mark.parametrize('user_id, expected_user', [(5, User(**get_file_contents("templates/user5.json")))])
def test_send_get_request_to_get_user(user_id, expected_user):
    user = User.get_user(user_id)
    assert_utils.is_objects_identical(user, expected_user)
