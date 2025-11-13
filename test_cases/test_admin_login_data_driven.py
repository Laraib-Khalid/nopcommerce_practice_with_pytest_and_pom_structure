from selenium.webdriver.common.by import By
import time
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_maker
from utilities.excel_utils import ExcelUtils

class Test_02_Admin_Login_Data_Driven:
    admin_page_url = Read_Config.get_admin_page_url()

    # Path to your Excel
    excel_path = "test_data/admin_login_data.xlsx"
    sheet_name = "Login_Data"

    # Load Excel utility
    excel = ExcelUtils(excel_path, sheet_name)

    logger = Log_maker.log_gen()

    status_list = []




    def test_login_data_driven(self, setup):
        self.logger.info("********** Test Login Using Data Driven Approach Starting **********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.login_page = Login_Admin_Page(self.driver)
        self.driver.get(self.admin_page_url)

        # Read total rows
        rows = self.excel.get_row_count()

        # Loop through Excel data
        for r in range(2, rows + 1):  # starting from row 2 (row 1 = header)
            username = self.excel.read_data(r, 1)
            password = self.excel.read_data(r, 2)
            expected_login = self.excel.read_data(r, 3)
            time.sleep(5)
            # Perform login using data from Excel

            self.login_page.enter_username(username)
            self.login_page.enter_password(password)
            self.login_page.select_remember_me_checkbox()
            self.login_page.click_login()
            input("Paused... Press Enter to continue.")
            # time.sleep(30)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if expected_login == "Yes":
                    self.status_list.append("Pass")
                    result = "Pass"
                    self.logger.info("********** Test Data is Pass **********")
                    time.sleep(10)
                    self.login_page.click_logout()
                elif expected_login == "No":
                    self.status_list.append("Fail")
                    result = "Fail"
                    self.logger.info("********** Test Data is Fail **********")

            elif act_title != exp_title:
                if expected_login == "Yes":
                    self.status_list.append("Fail")
                    result = "Fail"
                    self.logger.info("********** Test Data is Fail **********")
                elif expected_login == "No":
                    self.status_list.append("Pass")
                    result = "Pass"
                    self.logger.info("********** Test Data is Pass **********")

            # Write result back to Excel
            self.excel.write_data(1, 4, "Test_Status")
            self.excel.write_data(r, 4, result)

        print("Status List is: " , self.status_list)
        if "Fail" in result:
            self.logger.info("********** Test Admin Data Driven is Failed **********")
            self.logger.info("********** Test Login Using Data Driven Approach Ending **********")
            self.driver.quit()
            assert False

        else:
            self.logger.info("********** Test Admin Data Driven is Passed **********")
            self.logger.info("********** Test Login Using Data Driven Approach Ending **********")
            assert True
            self.driver.quit()

