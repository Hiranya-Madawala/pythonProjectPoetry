from selenium.webdriver.common.by import By

class ChemTalkPageLocators:
    LOGIN_LINK = (By.XPATH, '//*[@id="b_results"]/li[1]/h2/a')
    #FIRST_OPTION = (By.CSS_SELECTOR, '.first-option')
    FIRST_OPTION = (By.XPATH, "//*[@id='menu-item-7150']/div/a")
    LOGIN_BUTTON = (By.ID, 'login-button')
    MANGANESE_ELEMENT = (By.CSS_SELECTOR, '.element-manganese')

