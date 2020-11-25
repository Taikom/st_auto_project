from .base_page import BasePage
from .locators import BasketPageLocators
from selenium import webdriver


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_not_items_message()
        self.should_be_empty()

    def should_not_items_message(self):
        #проверка: есть текст "нет товаров в корзине"
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",
        }
        language = self.browser.execute_script("return window.navigator.userLanguage || window.navigator.language")
        EMPTY_BASKET = languages[language]
        self.is_text_in_message(*BasketPageLocators.MESSAGE_IN_BASKET,EMPTY_BASKET)

    def should_be_empty(self):
        #проверка: в корзине нет товаров
        assert self.is_not_items_in_basket(*BasketPageLocators.ITEMS_IN_BASKET), "Basket is not empty"
