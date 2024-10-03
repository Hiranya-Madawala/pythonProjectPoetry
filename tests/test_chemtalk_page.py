import pytest
from pages.base_page import BasePage
from pages.chemtalk_page_locators import Locators
from resources.constants import URL, MAX_WAIT_INTERVAL

class TestChemTalkNavigation:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.driver.get(URL)
        self.base_page = BasePage(driver)

    def test_chemtalk_navigation(self):
        # Verify menu item is displayed
        assert self.base_page.wait_for_element(*Locators.MENU_ITEM).is_displayed()

        # Click on the dropdown arrow for elements
        self.base_page.click_element(*Locators.DROPDOWN_ARROW)

        # Select "Interactive Periodic Table" from the popup window
        self.base_page.click_element(*Locators.INTERACTIVE_PERIODIC_TABLE)

        # Verify navigation by checking for the presence of the periodic table
        #assert self.base_page.wait_for_element(*Locators.MANGANESE_ELEMENT).is_displayed()

        # Scroll to Manganese Element and click
        #self.driver.execute_script("window.scrollBy(0, 200);")
        #self.base_page.click_element(*Locators.MANGANESE_ELEMENT)

        # Verify navigation by checking for the presence of the Mn element
        #assert self.base_page.wait_for_element(*Locators.ATOMIC_NUMBER, timeout=40).is_displayed()

