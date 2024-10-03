from pages.base_page import BasePage
from pages.chemtalk_page_locators import Locators
from resources.constants import URL

class ChemTalkPage(BasePage):

    def navigate_to_home(self):
        self.driver.get(URL)

    def verify_menu_item_displayed(self):
        return self.wait_for_element(*Locators.MENU_ITEM).is_displayed()

    def click_dropdown_arrow(self):
        self.click_element(*Locators.DROPDOWN_ARROW)

    def select_interactive_periodic_table(self):
        self.click_element(*Locators.INTERACTIVE_PERIODIC_TABLE)

    def verify_manganese_element_displayed(self):
        return self.wait_for_element(*Locators.MANGANESE_ELEMENT).is_displayed()

    #def click_manganese_element(self):
        #self.click_element(*Locators.MANGANESE_ELEMENT)

    #def verify_atomic_number_displayed(self):
        #return self.wait_for_element(*Locators.ATOMIC_NUMBER, timeout=40).is_displayed()
