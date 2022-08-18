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

    def __init__(self, data: dict):
        """
        Initializer of User entity object
        :param data: dictionary with information about User - id(int), name(str), username(str), email(str),
        address(dict), phone(str), website(str), company(dict)
        """
        self.id = data[self.ID_FIELD]
        self.name = data[self.NAME_FIELD]
        self.username = data[self.USERNAME_FIELD]
        self.email = data[self.EMAIL_FIELD]
        self.address = data[self.ADDRESS_FIELD]
        self.phone = data[self.PHONE_FIELD]
        self.website = data[self.WEBSITE_FIELD]
        self.company = data[self.COMPANY_FIELD]

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id and self.name == other.name and \
               self.username == other.username and self.email == other.email and self.address == other.address and \
               self.phone == other.phone and self.website == other.website and self.company == other.company

    def to_json(self):
        return {
            self.ID_FIELD: self.id,
            self.NAME_FIELD: self.name,
            self.USERNAME_FIELD: self.username,
            self.EMAIL_FIELD: self.email,
            self.ADDRESS_FIELD: self.address,
            self.PHONE_FIELD: self.phone,
            self.WEBSITE_FIELD: self.website,
            self.COMPANY_FIELD: self.company,
        }
