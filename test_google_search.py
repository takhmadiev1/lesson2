from selene.support.shared import browser
from selene import be, have


def test_valid_search_yashaka(resize_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_found_nothing(resize_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('hvkjhdcnckjsdncvdcevvsdchgvsdc').press_enter()
    browser.element('.card-section').should(have.text('По запросу hvkjhdcnckjsdncvdcevvsdchgvsdc ничего не найдено.'))
