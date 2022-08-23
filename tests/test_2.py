import pytest

from schemas.post_models.posts import Posts


def test_send_get_requests_to_get_posts(is_user_model_tests_should_be_skipped):
    if is_user_model_tests_should_be_skipped:
        pytest.skip('Text skipped due to user_models input')
    posts = Posts.get_all_posts()
    assert posts.is_posts_sorted()
