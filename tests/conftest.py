import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_config_desktop():
    browser.config.window_width = 1440
    browser.config.window_height = 800


@pytest.fixture()
def browser_config_mobile():
    browser.config.window_width = 414
    browser.config.window_height = 896
