from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page

class Test_01_Admin_Login:
    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"
    invalid_username = "admindata@test.com"


    def test_title_verification(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        if act_title == exp_title:
            print("Title is matched")
            assert True
            self.driver.quit()
        else:
            print("Title is not matched")
            self.driver.save_screenshot("screenshots/test_title_verification.png")
            self.driver.quit()
            assert False
        # assert act_title == exp_title
    #
    def test_valid_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.login_page = Login_Admin_Page(self.driver)
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.password)
        self.login_page.select_remember_me_checkbox()
        self.login_page.click_login()
        input("Paused... Press Enter to continue.")
        act_dashboard_title = self.driver.find_element(By.XPATH, "//div[@class='content-header']//h1").text
        exp_dashboard_title = "Dashboard"
        if act_dashboard_title == exp_dashboard_title:
            print("Dashboard title is matched")
            assert True
            self.driver.quit()
        else:
            print("Dashboard title is not matched")
            self.driver.save_screenshot("screenshots/test_valid_login.png")
            self.driver.quit()
            assert False


    def test_invalid_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.login_page = Login_Admin_Page(self.driver)
        self.login_page.enter_username(self.invalid_username)
        self.login_page.enter_password(self.password)
        self.login_page.select_remember_me_checkbox()
        self.login_page.click_login()
        input("Paused... Press Enter to continue.")
        error_message = self.driver.find_element(By.XPATH, "//li").text
        if error_message == "No customer account found":
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot("screenshots/test_invalid_login.png")
            self.driver.quit()
            assert False