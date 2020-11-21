from selenium.webdriver.common.by import By


#class MainPageLocators():


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_LINK=(By.CSS_SELECTOR,".btn-add-to-basket")
    NAME_ADDED_TO_BASKET_MESSAGE=(By.XPATH,'//div[contains(@class,"alertinner")]/strong')
    NAME_ON_PRODUCT_PAGE=(By.CSS_SELECTOR,".content h1")
    PRICE_ADDED_TO_BASKET_MESSAGE=(By.XPATH,'//div[@id="messages"]/div[3]/div//strong')
    PRICE_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE =(By.CSS_SELECTOR,"#messages .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET=(By.CSS_SELECTOR, ".basket-mini .btn")

class BasketPageLocators():
    MESSAGE_IN_BASKET = (By.CSS_SELECTOR, "#content_inner")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")


