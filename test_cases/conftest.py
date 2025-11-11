import pytest
from pytest_metadata.plugin import metadata_key
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


# ************* For Pytest HTML Reports ****************
# Hook for adding environment information in HTML report

def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce Project, nopCommerce'
    config.stash[metadata_key]['Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester'] = 'Laraib Khalid'



# Hook for delete/modify environment information in HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    # metadata.pop('Python', None)
    # metadata.pop('Platform', None)
    # metadata.pop('Packages', None)
    metadata.pop('Plugins', None)
    metadata.pop('JAVA_HOME', None)