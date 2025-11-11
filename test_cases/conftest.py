import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser name (chrome or firefox)")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture()
def setup(browser):
    """Run tests on Chrome, Firefox, or Edge."""
    browser = browser.lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=options)
        # Optional: remove automation flag via CDP
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => undefined
                })
            """
        })

    elif browser == "firefox":
        # Create Firefox options
        options = FirefoxOptions()
        options.add_argument("--start-maximized")

        # Create Firefox profile
        profile = webdriver.FirefoxProfile()
        profile.set_preference("dom.webdriver.enabled", False)  # hide automation
        profile.set_preference("general.useragent.override", "Mozilla/5.0")  # override UA

        # Attach profile to options
        options.profile = profile
        driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Edge(options=options)
        # Optional: remove automation flag via CDP
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => undefined
                })
            """
        })

    else:
        raise ValueError(f"Browser '{browser}' is not supported. Choose 'chrome', 'firefox', or 'edge'.")
    return driver