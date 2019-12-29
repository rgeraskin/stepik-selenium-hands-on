from pages.base_page import BasePage
from pages.locators import ProductPageLocators


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

        assert book_price_el.text == basket_price_el.text, \
            "Book price <> basket price"

    def should_not_be_success_message1(self):
        assert self.is_not_element_present(
            *ProductPageLocators.MESSAGE_BOOK_ADDED_BOOK_NAME
        ), "Success message is present"

    def should_not_be_success_message2(self):
        assert self.is_disappeared(
            *ProductPageLocators.MESSAGE_BOOK_ADDED_BOOK_NAME
        ), "Success message is not dissapeared"
