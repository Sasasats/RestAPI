import requests

from schemas.user_models.user import User
from utils import assert_utils
from utils.config_data import ConfigData


class Users:
    """
    Business-model class for working with the Users list
    """

    def __init__(self, users: list):
        """
        Initializer of Users list
        :param users: list with User objects
        """
        self.users = users

    def __getitem__(self, item) -> User:
        """
        Return the user_models by his number in the list, not index!
        :param item: User's number in the list, starts with 0!
        :return: User object
        """
        return self.users[item]

    @staticmethod
    def get_users() -> 'Users':
        response = requests.get(ConfigData.URL.value + ConfigData.USERS_ENDPOINT.value)
        assert_utils.is_response_correct(response, requests.status_codes.codes.ok)
        return Users(users=[
            User(**user)
            for user in response.json()
        ])
