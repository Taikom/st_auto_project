from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import pytest


@pytest.mark.parametrize('promo_num',[0,1,2,3,4,5,6,pytest.param("7",marks=pytest.mark.xfail),8,9])
def test_guest_can_add_product_to_basket(browser, promo_num):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket_message()
    page.should_be_sum_correct()