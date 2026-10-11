
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()

    # Disable password leak detection popups in test Chrome
    options.add_experimental_option(
        "prefs",
        {
            "profile.password_manager_leak_detection": False,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    yield browser

    browser.quit()
