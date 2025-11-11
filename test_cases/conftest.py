import pytest
from utilities.driver import create_driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser name (chrome or firefox)")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture()
def setup(browser):
    """Run tests on Chrome, Firefox, or Edge."""
    driver = create_driver(browser)
    return driver