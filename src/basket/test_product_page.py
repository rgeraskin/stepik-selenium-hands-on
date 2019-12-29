import time

import pytest

from basket.pages.basket_page import BasketPage
from basket.pages.login_page import LoginPage
from basket.pages.main_page import MainPage
from basket.pages.product_page import ProductPage


@pytest.mark.TestUserAddToBasketFromProductPage
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, link)
        email = str(time.time()) + "@fakemail.org"
        password = "password123123"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.parametrize('link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    ])
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()

        page.should_not_be_success_message1()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    ])
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_added_to_basket()
        page.should_be_same_price()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_to_basket()
    page.should_be_same_price()


@pytest.mark.xfail()
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
])
def test_guest_cant_see_success_message_after_adding_product_to_basket(
    browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.should_not_be_success_message1()


@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_success_message1()


@pytest.mark.xfail()
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    time.sleep(300)
    page.should_not_be_success_message2()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, link)
    page.should_be_empty()
    page.should_be_text_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
