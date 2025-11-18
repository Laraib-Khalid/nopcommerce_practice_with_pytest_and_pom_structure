import pytest
import socket
import sys
import warnings
from base_pages.Login_Admin_Page import Login_Admin_Page

@pytest.mark.skip(reason="Login API temporarily down")
def test_login_with_valid_credentials(driver):

    login = Login_Admin_Page(driver)
    login.enter_username("admin@yourstore.com")
    login.enter_password("admin")
    login.click_login()
    input("Press Enter to continue...")
    assert "Dashboard" in driver.title


def test_profile_picture_upload(driver, browser):
    # if request.config.getoption("--browser") == "firefox":
    #     pytest.skip("Feature not supported in Firefox")

    if browser == "firefox":
        pytest.skip("Feature not supported in Firefox")

    login = Login_Admin_Page(driver)
    login.enter_username("admin@yourstore.com")
    login.enter_password("admin")
    login.click_login()
    input("Press Enter to continue...")
    assert "Dashboard" in driver.title
    login.click_logout()





@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_not_for_windows():
    assert True



def has_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False

@pytest.mark.skipif(not has_internet(), reason="Internet required")
def test_needs_internet():
    assert True


@pytest.mark.xfail(reason="Bug #478: logout button not responding")
def test_logout(driver):

    login = Login_Admin_Page(driver)
    login.enter_username("admin@yourstore.com")
    login.enter_password("admin")
    login.click_login()
    input("Press Enter to continue...")
    assert "Dashboard" in driver.title
    login.click_logout()
    # assert False  # known bug


def is_dashboard_loaded(driver):
        return "Dashboard" in driver.title

@pytest.mark.xfail(reason="Dashboard title issue on staging")
@pytest.mark.parametrize("username,password",
    [
        ("wrong", "invalid"),
        ("admin@yourstore.com", "admin")
])
def test_login_pom(driver, username, password):
    login = Login_Admin_Page(driver)

    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    assert is_dashboard_loaded(driver)



# 1. Filter a specific warning inside a test using @pytest.mark.filterwarnings
@pytest.mark.filterwarnings("ignore:deprecated:DeprecationWarning")
def test_ignore_deprecation_warning():
    # This warning will be ignored
    warnings.warn("deprecated", DeprecationWarning)
    assert True


# ✅ 2. Filter ALL DeprecationWarnings for this test only

@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_ignore_all_deprecation():
    warnings.warn("This is deprecated", DeprecationWarning)
    assert True


# ✅ 3. Allow only a specific warning and fail for others


# 1) Allow specific warning first
@pytest.mark.filterwarnings("default:Allowed message:UserWarning")
# 2) Then turn all other warnings into errors
@pytest.mark.filterwarnings("error")
def test_only_allow_specific_warning():
    # This warning is ALLOWED and will not fail
    warnings.warn("Allowed message", UserWarning)

    # This would fail the test:
    # warnings.warn("Not allowed", UserWarning)

    assert True
