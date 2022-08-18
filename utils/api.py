import requests

from models.post.post import Post
from models.post.posts import Posts
from models.user.user import User
from models.user.users import Users
from utils.soft_assert import SoftAssert
from utils.test_data import TestData


class API:
    @staticmethod
    def get_all_posts(status_code):
        posts_response = requests.get(TestData.URL.value + TestData.POSTS_ENDPOINT.value)
        SoftAssert.is_response_correct(posts_response, status_code)
        return Posts(posts=[
            Post(post)
            for post in posts_response.json()
        ])

    @staticmethod
    def get_post(post_id, status_code):
        post_response = requests.get(TestData.URL.value + TestData.POSTS_ENDPOINT.value + str(post_id))
        assert post_response.status_code == status_code, "status codes don't match"
        return Post(post_response.json())

    @staticmethod
    def get_no_such_post(post_id, status_code):
        post_response = requests.get(TestData.URL.value + TestData.POSTS_ENDPOINT.value + str(post_id))
        assert post_response.status_code == status_code, "status codes don't match"
        assert post_response.json() == TestData.EMPTY_BODY_REQUEST.value, "response body is not empty"

    @staticmethod
    def add_post(post, status_code):
        post_response = requests.post(TestData.URL.value + TestData.POSTS_ENDPOINT.value, data=post.to_json())
        assert post_response.status_code == status_code, "status codes don't match"
        return Post(post_response.json())

    @staticmethod
    def get_users(status_code):
        users_response = requests.get(TestData.URL.value + TestData.USERS_ENDPOINT.value)
        SoftAssert.is_response_correct(users_response, status_code)
        return Users(users=[
            User(user)
            for user in users_response.json()
        ])

    @staticmethod
    def get_user(user_id, status_code):
        users_response = requests.get(TestData.URL.value + TestData.USERS_ENDPOINT.value + str(user_id))
        assert users_response.status_code == status_code, "status codes don't match"
        return User(users_response.json())
