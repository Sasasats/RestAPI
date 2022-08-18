class Post:
    """
    Business-model class for working with the Post entity
    """

    USER_ID_FIELD = 'userId'
    ID_FIELD = 'id'
    TITLE_FIELD = 'title'
    BODY_FIELD = 'body'

    def __init__(self, data: dict):
        """
        Initializer of Post entity object
        :param data: dictionary with information about Post - user_id(int), id(int), title(str), body(str)
        """
        self.user_id = data[self.USER_ID_FIELD]
        self.id = data[self.ID_FIELD]
        self.title = data[self.TITLE_FIELD]
        self.body = data[self.BODY_FIELD]

    def __str__(self):
        return self.to_json()

    def to_json(self):
        return {self.USER_ID_FIELD: self.user_id,
                self.ID_FIELD: self.id,
                self.TITLE_FIELD: self.title,
                self.BODY_FIELD: self.body}
