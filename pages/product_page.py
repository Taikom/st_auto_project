from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_basket_message()
        self.should_be_sum_correct()
        self.should_not_be_success_message()
        self.add_to_basket()
        self.should_message_disappeared()


    def add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        add_to_basket_link.click()

    def should_be_add_to_basket_message(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_ADDED_TO_BASKET_MESSAGE).text == self.browser.find_element(*ProductPageLocators.NAME_ON_PRODUCT_PAGE).text, "Name in message and in product page are not equal"

    def should_be_sum_correct(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_ADDED_TO_BASKET_MESSAGE).text == self.browser.find_element(*ProductPageLocators.PRICE_ON_PRODUCT_PAGE).text, "Price in message and in product page are not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Message should disappeared, but didn't"