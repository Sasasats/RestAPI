import requests

from schemas.post_models.post import Post
from utils.config_data import ConfigData
from utils import assert_utils


class Posts:
    """
    Business-model class for working with the Posts list
    """

    def __init__(self, posts: list):
        """
        Initializer of Posts list
        :param posts: list with Post objects
        """
        self.posts = posts

    def is_posts_sorted(self) -> bool:
        """
        Check the sorting of posts by id
        :return: boolean answer
        """
        sorted_posts = sorted(self.posts, key=lambda post: post.id)
        return self.posts == sorted_posts

    @staticmethod
    def get_all_posts() -> 'Posts':
        response = requests.get(ConfigData.URL.value + ConfigData.POSTS_ENDPOINT.value)
        assert_utils.is_response_correct(response, requests.status_codes.codes.ok)
        return Posts(posts=[
            Post(**post)
            for post in response.json()
        ])
