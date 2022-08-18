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

    def is_posts_sorted(self):
        """
        Check the sorting of posts by id
        :return: boolean answer
        """
        sorted_posts = sorted(self.posts, key=lambda post: post.id)
        return True if self.posts == sorted_posts else False
