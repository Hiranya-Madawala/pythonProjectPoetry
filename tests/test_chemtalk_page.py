import pytest
from pages.chemtalk_page import ChemTalkPage
from pages.chemtalk_page_locators import ChemTalkPageLocators


def test_login_and_select_first_option(driver):
    page = ChemTalkPage(driver)
    page.login()
    page.select_first_option()
    # Add assertions here
    assert page.find_element(ChemTalkPageLocators.FIRST_OPTION).is_selected()


def test_locate_elements(driver):
    page = ChemTalkPage(driver)
    page.login()

    # Locate Iodine
    iodine_element = page.locate_element(ChemTalkPageLocators.IODINE_ELEMENT)
    page.wait_for_seconds(20)
    assert iodine_element.is_displayed()

    # Locate Manganese
    manganese_element = page.locate_element(ChemTalkPageLocators.MANGANESE_ELEMENT)
    page.wait_for_seconds(20)
    assert manganese_element.is_displayed()
