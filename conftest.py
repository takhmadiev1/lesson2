import pytest
from selene.support.shared import browser


@pytest.fixture
def resize_browser():
    browser.config.window_height = 1000
    browser.config.window_width = 1000

    yield

    browser.quit()

def some_func():
    pass