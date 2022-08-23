import requests

from utils import assert_utils
from utils.config_data import ConfigData


class Post:
    """
    Business-model class for working with the Post entity
    """

    USER_ID_FIELD = 'userId'
    ID_FIELD = 'id'
    TITLE_FIELD = 'title'
    BODY_FIELD = 'body'

    def __init__(self, **kwargs):
        """
        Initializer of Post entity object
        :param data: dictionary with information about Post - user_id(int), id(int), title(str), body(str)
        """
        self.user_id = kwargs.get(self.USER_ID_FIELD)
        self.id = kwargs[self.ID_FIELD]
        self.title = kwargs[self.TITLE_FIELD]
        self.body = kwargs.get(self.BODY_FIELD)

    def to_json(self) -> dict:
        return {self.USER_ID_FIELD: self.user_id,
                self.ID_FIELD: self.id,
                self.TITLE_FIELD: self.title,
                self.BODY_FIELD: self.body}

    @staticmethod
    def get_post(post_id) -> 'Post':
        response = requests.get(ConfigData.URL.value + ConfigData.POSTS_ENDPOINT.value + str(post_id))
        assert_utils.is_status_code_correct(response, requests.status_codes.codes.ok)
        return Post(**response.json())

    @staticmethod
    def add_post(post) -> 'Post':
        response = requests.post(ConfigData.URL.value + ConfigData.POSTS_ENDPOINT.value, data=post.to_json())
        assert_utils.is_status_code_correct(response, requests.status_codes.codes.created)
        return Post(**response.json())

    @staticmethod
    def get_no_such_post(post_id):
        response = requests.get(ConfigData.URL.value + ConfigData.POSTS_ENDPOINT.value + str(post_id))
        assert_utils.is_status_code_correct(response, requests.status_codes.codes.not_found)
        assert_utils.is_response_body_empty(response)
