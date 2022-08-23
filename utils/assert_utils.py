def is_status_code_correct(response, expected_status_code):
    assert response.status_code == expected_status_code, \
        f"status codes don't match! Expected - {response.status_code}, actual - {expected_status_code}"


def is_response_body_empty(response):
    assert response.json() == {}, f"response body is not empty! Actual - {response.json()}"


def is_response_correct(response, expected_status_code):
    errors = []
    if 'application/json' not in response.headers['Content-Type']:
        errors.append('Content-Type')
    if response.status_code != expected_status_code:
        errors.append(expected_status_code)
    assert not errors, f'Response have these problems: {errors}'


def is_objects_identical(actual_object, expected_object):
    actual_object_dict = actual_object.to_json()
    expected_object_dict = expected_object.to_json()

    not_matched_fields = [
        field
        for field in actual_object_dict
        if (field in expected_object_dict) and (actual_object_dict[field] != expected_object_dict[field])
    ]

    assert not not_matched_fields, f'Not matched fields are: {not_matched_fields}'


def is_post_correct(post, post_user_id: int, post_id: int):
    not_matched_fields = []
    if post.user_id != post_user_id:
        not_matched_fields.append(post.USER_ID_FIELD)
    if post.id != post_id:
        not_matched_fields.append(post.ID_FIELD)
    if post.title == '':
        not_matched_fields.append(post.TITLE_FIELD)
    if post.body == '':
        not_matched_fields.append(post.BODY_FIELD)

    assert not not_matched_fields, f'Not matched fields are: {not_matched_fields}'


def is_created_post_correct(created_post, expected_post):
    not_matched_fields = []
    if created_post.user_id != expected_post.user_id:
        not_matched_fields.append(created_post.USER_ID_FIELD)
    if not isinstance(created_post.id, int):
        not_matched_fields.append(created_post.ID_FIELD)
    if created_post.title != expected_post.title:
        not_matched_fields.append(created_post.TITLE_FIELD)
    if created_post.body != expected_post.body:
        not_matched_fields.append(created_post.BODY_FIELD)

    assert not not_matched_fields, f'Not matched fields are: {not_matched_fields}'
