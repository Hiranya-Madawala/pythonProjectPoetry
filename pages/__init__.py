from .base_page import BasePage
from .chemtalk_page import ChemTalkPage
from .chemtalk_page_locators import ChemTalkPageLocators

# ChemTalk page
class ChemTalkPage(BasePage):

    def wait_and_click_login_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ChemTalkPageLocators.LOGIN_LINK).click()

    def login(self):
        self.navigate_to(CHEMTALK_URL)
        self.wait_and_click_login_button()

    def select_first_option(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ChemTalkPageLocators.FIRST_OPTION).click()

    def locate_element(self, element_locator):
        element = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        return element

    def wait_for_seconds(self, seconds):
        self.driver.implicitly_wait(seconds)

    def is_logged_out(self):
        login_btn_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ChemTalkPageLocators.LOGIN_BUTTON).text
        return login_btn_text == LOGIN_BTN_TEXT

