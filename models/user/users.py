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

    def get_user_by_number(self, user_number):
        """
        Return the user by his number in the list, not index!
        :param user_number: the User's number in the list
        :return: User object
        """
        return self.users[user_number - 1]
