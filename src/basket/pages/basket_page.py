from basket.pages.base_page import BasePage
from basket.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_CONTENTS), "Basket contents is present"

    def should_be_text_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT
                                       ), "Basket empty text is absent"
