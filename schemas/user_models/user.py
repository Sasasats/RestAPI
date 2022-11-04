import requests

from utils import assert_utils
from utils.config_data import ConfigData


class User:
    """
    Business-model class for working with the User entity
    """

    ID_FIELD = 'id'
    NAME_FIELD = 'name'
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    ADDRESS_FIELD = 'address'
    PHONE_FIELD = 'phone'
    WEBSITE_FIELD = 'website'
    COMPANY_FIELD = 'company'

    def __init__(self, **data: dict):
        """
        Initializer of User entity object
        :param data: dictionary with information about User - id(int), name(str), username(str), email(str),
        address(dict), phone(str), website(str), company(dict)
        """
        self.id = data[self.ID_FIELD]
        self.name = data[self.NAME_FIELD]
        self.username = data[self.USERNAME_FIELD]
        self.email = data.get(self.EMAIL_FIELD)
        self.address = data.get(self.ADDRESS_FIELD)
        self.phone = data.get(self.PHONE_FIELD)
        self.website = data.get(self.WEBSITE_FIELD)
        self.company = data.get(self.COMPANY_FIELD)

    def __eq__(self, other) -> bool:
        if self.__class__ != other.__class__:
            raise TypeError(f"types don't match: {self.__class__}, {other.__class__}")
        return self.to_json() == other.to_json()

    def to_json(self) -> dict:
        return {self.ID_FIELD: self.id,
                self.NAME_FIELD: self.name,
                self.USERNAME_FIELD: self.username,
                self.EMAIL_FIELD: self.email,
                self.ADDRESS_FIELD: self.address,
                self.PHONE_FIELD: self.phone,
                self.WEBSITE_FIELD: self.website,
                self.COMPANY_FIELD: self.company}

    @staticmethod
    def get_user(user_id) -> 'User':
        response = requests.get(ConfigData.URL.value + ConfigData.USERS_ENDPOINT.value + str(user_id))
        assert_utils.is_status_code_correct(response, requests.status_codes.codes.ok)
        return User(**response.json())
