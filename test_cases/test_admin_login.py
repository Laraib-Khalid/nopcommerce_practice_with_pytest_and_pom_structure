from selenium.webdriver.common.by import By
import time
import pytest
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_maker

class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_maker.log_gen()

    @pytest.mark.smoke
    def test_title_verification(self, setup):
        self.logger.info("********** Test_01_Admin_Login **********")
        self.logger.info("********** Verification of Admin Login Page Title **********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        if act_title == exp_title:
            print("Title is matched")
            self.logger.info("********** Admin Login Page Title Matched **********")
            assert True
            self.driver.quit()
        else:
            print("Title is not matched")
            self.driver.save_screenshot("screenshots/test_title_verification.png")
            self.logger.info("********** Admin Login Page Title Not Matched **********")
            self.driver.quit()
            assert False
        # assert act_title == exp_title
    #

    @pytest.mark.regression
    def test_valid_login(self, setup):
        self.logger.info("********** Test Valid Login Started **********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.login_page = Login_Admin_Page(self.driver)
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.password)
        self.login_page.select_remember_me_checkbox()
        self.login_page.click_login()
        # input("Paused... Press Enter to continue.")
        time.sleep(30)
        act_dashboard_title = self.driver.find_element(By.XPATH, "//div[@class='content-header']//h1").text
        exp_dashboard_title = "Dashboard"
        if act_dashboard_title == exp_dashboard_title:
            print("Dashboard title is matched")
            self.logger.info("********** Dashboard Text Matched **********")
            assert True
            self.driver.quit()
        else:
            print("Dashboard title is not matched")
            self.driver.save_screenshot("screenshots/test_valid_login.png")
            self.logger.info("********** Dashboard Text Not Matched **********")
            self.driver.quit()
            assert False


    @pytest.mark.regression
    def test_invalid_login(self, setup):
        self.logger.info("********** Test Invalid Login Started **********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.login_page = Login_Admin_Page(self.driver)
        self.login_page.enter_username(self.invalid_username)
        self.login_page.enter_password(self.password)
        self.login_page.select_remember_me_checkbox()
        self.login_page.click_login()
        # input("Paused... Press Enter to continue.")
        time.sleep(30)
        error_message = self.driver.find_element(By.XPATH, "//li").text
        if error_message == "No customer account found":
            self.logger.info("********** Error Message Found **********")
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot("screenshots/test_invalid_login.png")
            self.logger.info("********** Error Message Not Found **********")
            self.driver.quit()
            assert False