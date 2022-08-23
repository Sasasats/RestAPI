import pytest


def pytest_addoption(parser):
    parser.addoption("--post_models-tests", action="store", default=True, help="host ip address")
    parser.addoption("--user_models-tests", action="store", default=True, help="port")


@pytest.fixture
def get_param(request):
    return {"post_tests": request.config.getoption("--post_models-tests"),
            "user_tests": request.config.getoption("--user_models-tests")}


@pytest.fixture()
def is_post_model_tests_should_be_skipped(get_param):
    return get_param['post_tests'] == True


@pytest.fixture
def is_user_model_tests_should_be_skipped(get_param):
    return get_param['user_tests'] == True
