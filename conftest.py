import pytest
from selene.support.shared import browser
import random


@pytest.fixture
def resize_browser_height():
    browser.config.window_height = random.randint(500, 1000)

    yield

    browser.quit()


@pytest.fixture
def resize_browser_width():
    browser.config.window_width = random.randint(1000, 2000)

    yield

    browser.quit()
