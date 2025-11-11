from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Login_Admin_Page:

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    remember_me_id = "RememberMe"
    button_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def select_remember_me_checkbox(self):
        self.driver.find_element(By.ID, self.remember_me_id).click()
        # select = Select(self.driver.find_element(By.ID, self.remember_me_id))
        # select.select_by_visible_text("RememberMe")

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

