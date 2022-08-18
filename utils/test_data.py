from enum import Enum

from models.user.user import User
from utils.file_utils import get_file_contents


class TestData(Enum):
    URL = 'https://jsonplaceholder.typicode.com/'
    POSTS_ENDPOINT = 'posts/'
    USERS_ENDPOINT = 'users/'

    EXPECTED_USER_5 = User(get_file_contents("templates/user5.json"))
    EMPTY_BODY_REQUEST = {}
