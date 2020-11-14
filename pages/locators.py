from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_LINK=(By.CSS_SELECTOR,".btn-add-to-basket")
    NAME_ADDED_TO_BASKET_MESSAGE=(By.XPATH,'//div[contains(@class,"alertinner")]/strong')
    NAME_ON_PRODUCT_PAGE=(By.CSS_SELECTOR,".content h1")
    PRICE_ADDED_TO_BASKET_MESSAGE=(By.XPATH,'//div[@id="messages"]/div[3]/div//strong')
    PRICE_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main .price_color")




