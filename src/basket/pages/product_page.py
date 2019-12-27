import time

from basket.pages.base_page import BasePage
from basket.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(
            *ProductPageLocators.BTN_ADD_TO_BASKET).click()

    def should_be_added_to_basket(self):
        book_name_el = self.browser.find_element(
            *ProductPageLocators.BOOK_NAME)
        book_added_el = self.browser.find_element(
            *ProductPageLocators.MESSAGE_BOOK_ADDED_BOOK_NAME)
        assert book_name_el.text == book_added_el.text, \
            "Book name in basket <> book name on book page"

    def should_be_same_price(self):
        book_price_el = self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE)
        basket_price_el = self.browser.find_element(
            *ProductPageLocators.MESSAGE_BASKET_PRICE)
        # time.sleep(300)
        assert book_price_el.text == basket_price_el.text, \
            "Book price <> basket price"
