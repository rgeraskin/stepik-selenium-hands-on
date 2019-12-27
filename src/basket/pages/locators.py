from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    MESSAGE_BOOK_ADDED_BOOK_NAME = (By.CSS_SELECTOR,
                          "#messages > div:nth-child(1) strong")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "#messages > .alert-info strong")
