import pytest
import requests

from models.post.post import Post
from utils.api import API
from utils.soft_assert import SoftAssert
from utils.test_data import TestData


@pytest.mark.parametrize('status_code', [requests.status_codes.codes.ok])
def test_send_get_requests_to_get_posts(status_code):
    posts = API.get_all_posts(status_code)
    assert posts.is_posts_sorted()


@pytest.mark.parametrize('post_user_id, post_id, status_code', [(10, 99, requests.status_codes.codes.ok)])
def test_send_get_request_to_get_post(post_user_id, post_id, status_code):
    post = API.get_post(post_id, status_code)
    SoftAssert.is_post_correct(post, post_user_id, post_id)


@pytest.mark.parametrize('post_id, status_code', [(150, requests.status_codes.codes.not_found)])
def test_send_get_request_to_get_no_such_post(post_id, status_code):
    API.get_no_such_post(post_id, status_code)


@pytest.mark.parametrize('expected_post, status_code',
                         [(Post({'userId': 1, 'id': 101, 'title': 'AlexExample', 'body': 'example_body'}),
                           requests.status_codes.codes.created)])
def test_create_post(expected_post, status_code):
    created_post = API.add_post(expected_post, status_code)
    SoftAssert.is_created_post_correct(created_post, expected_post)


@pytest.mark.parametrize('actual_user_number, expected_user, status_code',
                         [(5, TestData.EXPECTED_USER_5.value, requests.status_codes.codes.ok)])
def test_get_user_from_users(actual_user_number, expected_user, status_code):
    users = API.get_users(status_code)
    assert users.get_user_by_number(actual_user_number) == expected_user, 'The returned user is not expected'


@pytest.mark.parametrize('user_id, expected_user, status_code',
                         [(5, TestData.EXPECTED_USER_5.value, requests.status_codes.codes.ok)])
def test_send_get_request_to_get_user(user_id, expected_user, status_code):
    user = API.get_user(user_id, status_code)
    SoftAssert.is_objects_identical(user, expected_user)
