from faker import Faker
import pytest
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Add_Customer_Page import Add_Customer_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_maker


class Test_03_Add_Customer:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_maker.log_gen()


    @pytest.mark.smoke
    @pytest.mark.regression
    def test_add_customer(self, setup):
        self.logger.info("********** Test_03 Add Customer Test Case Starting **********")
        self.driver = setup
        self.driver.implicitly_wait(10)

        self.logger.info("********** Login Started **********")

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
            self.logger.info("********** Dashboard Text Matched **********")
            assert True
        else:
            print("Dashboard title is not matched")
            self.driver.save_screenshot("screenshots/test_valid_login.png")
            self.logger.info("********** Dashboard Text Not Matched **********")
            assert False

        self.customer_page = Add_Customer_Page(self.driver)
        self.customer_page.click_customer_menu()
        self.customer_page.click_customer_sub_menu()
        self.customer_page.click_add_button()

        self.logger.info("********** Adding Customer Details **********")

        fake = Faker()
        self.customer_page.enter_email()
        self.customer_page.enter_password()
        self.customer_page.enter_first_name(fake.first_name())
        self.customer_page.enter_last_name(fake.last_name())
        self.customer_page.select_gender("Male")
        self.customer_page.enter_company_name(fake.company())
        self.customer_page.select_tax_exempt()
        # time.sleep(10)
        self.customer_page.select_customer_role("Guests")
        self.customer_page.manager_of_vendor("Vendor 1")
        self.customer_page.verify_active_checkbox()
        self.customer_page.select_customer_change_password_checkbox()
        self.customer_page.enter_admin_comment("This is a test comment")
        self.customer_page.click_save_button()

        self.logger.info("********** Checking Success Message **********")
        exp_success_message = "The new customer has been added successfully."
        act_success_message = self.customer_page.get_success_message()

        if act_success_message in exp_success_message:
            self.logger.info("********** Test_03 Add Customer Test Case is Passed **********")
            assert True
            self.driver.quit()
        else:
            self.logger.info("********** Test_03 Add Customer Test Case is Failed **********")
            self.driver.save_screenshot("screenshots/add_new_customer.png")
            self.driver.quit()
            assert False


        self.logger.info("********** Test_03 Add Customer Test Case Ending **********")

