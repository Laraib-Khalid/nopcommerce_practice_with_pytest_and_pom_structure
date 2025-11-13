import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Add_Customer_Page:
    customer_menu_xpath = "//p[normalize-space(text())='Customers']//parent::a[@href='#']"
    customer_sub_menu_xpath = "//li[@class='nav-item']//p[normalize-space(text())='Customers']"
    add_button_xpath = "//a[contains(.,'Add new')]"
    email_id = "Email"
    password_id = "Password"
    first_name_id = "FirstName"
    last_name_id = "LastName"
    male_gender_id = "Gender_Male"
    female_gender_id = "Gender_Female"
    company_name_id = "Company"
    tax_exempt_id = "IsTaxExempt"
    customer_role_list_id = "//div[@class='select2-blue']"
    registered_role_xpath = "//li[text()='Registered' and @role='option']"
    guests_role_xpath = "//li[text()='Guests' and @role='option']"
    administrators_role_xpath = "//li[text()='Administrators' and @role='option']"
    forum_moderators_role_xpath = "//li[text()='Forum Moderators' and @role='option']"
    vendors_role_xpath = "//li[text()='Vendors' and @role='option']"
    not_vendor_xpath = "//li[text()='Not a vendor' and @role='option']"
    vendor_1_xpath = "//li[text()='Vendor 1' and @role='option']"
    vendor_2_xpath = "//li[text()='Vendor 2' and @role='option']"
    active_checkbox_id = "Active"
    change_password_checkbox_id = "MustChangePassword"
    admin_comment_id = "AdminComment"
    save_button_xpath = "//button[@type='submit' and @name='save']"



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def click_customer_menu(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customer_menu_xpath)))
        self.driver.find_element(By.XPATH, self.customer_menu_xpath).click()

    def click_customer_sub_menu(self):
        self.driver.find_element(By.XPATH, self.customer_sub_menu_xpath).click()

    def click_add_button(self):
        self.driver.find_element(By.XPATH, self.add_button_xpath).click()

    def enter_email(self):
        email = self.generate_random_email()
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def enter_password(self):
        password = self.generate_random_password()
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def enter_first_name(self,first_name):
        self.driver.find_element(By.ID, self.first_name_id).clear()
        self.driver.find_element(By.ID, self.first_name_id).send_keys(first_name)

    def enter_last_name(self,last_name):
        self.driver.find_element(By.ID, self.last_name_id).clear()
        self.driver.find_element(By.ID, self.last_name_id).send_keys(last_name)

    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.male_gender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.female_gender_id).click()
        else:
            self.driver.find_element(By.ID, self.female_gender_id).click()

    def enter_company_name(self, company_name):
        self.driver.find_element(By.ID, self.company_name_id).clear()
        self.driver.find_element(By.ID, self.company_name_id).send_keys(company_name)

    def select_tax_exempt(self):
        self.driver.find_element(By.ID, self.tax_exempt_id).click()

    def select_customer_role(self, customer_role):
        elements = self.driver.find_elements(By.XPATH, self.customer_role_list_id)
        #
        # print(len(elements))
        # print("Locator used:", self.customer_role_list_id)

        if elements:
            customer_role_field = elements[0]
            # Now safely interact with it
            customer_role_field.click()
            # further logic to select role...
        else:
            raise Exception(f"No elements found with ID: {self.customer_role_list_id}")

        if customer_role == "Guests":
            self.driver.find_element(By.XPATH,self.registered_role_xpath).click()
            self.driver.find_element(By.XPATH,self.guests_role_xpath).click()
            customer_role_field.click()

        elif customer_role == "Administrators":
            self.driver.find_element(By.XPATH, self.administrators_role_xpath).click()
            customer_role_field.click()

        elif customer_role == "Forum Moderators":
            self.driver.find_element(By.XPATH,self.forum_moderators_role_xpath).click()
            customer_role_field.click()

        elif customer_role == "Registered":
            pass

        elif customer_role == "Vendors":
            self.driver.find_element(By.XPATH,self.vendors_role_xpath).click()
            customer_role_field.click()

    def manager_of_vendor(self, vendor):
        elements = self.driver.find_elements(By.XPATH, self.customer_role_list_id)
        #
        # print(len(elements))
        # print("Locator used:", self.customer_role_list_id)

        if elements:
            vendor_role_field = elements[1]
            # Now safely interact with it
            vendor_role_field.click()
            # further logic to select role...
        else:
            raise Exception(f"No elements found with ID: {self.customer_role_list_id}")

        if vendor == "Not a vendor":
            pass
        elif vendor == "Vendor 1":
            self.driver.find_element(By.XPATH,self.vendor_1_xpath).click()
        elif vendor == "Vendor 2":
            self.driver.find_element(By.XPATH,self.vendor_2_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.vendor_2_xpath).click()

    def verify_active_checkbox(self):
        if self.driver.find_element(By.ID, self.active_checkbox_id).is_selected():
            pass
        else:
            self.driver.find_element(By.ID, self.active_checkbox_id).click()

    def select_customer_change_password_checkbox(self):
        self.driver.find_element(By.ID, self.change_password_checkbox_id).click()

    def enter_admin_comment(self, admin_comment):
        self.driver.find_element(By.ID, self.admin_comment_id).clear()
        self.driver.find_element(By.ID, self.admin_comment_id).send_keys(admin_comment)

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def generate_random_email(self):
        # Generate random username (8–12 characters)
        username_length = random.randint(8, 12)
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))

        # Random domain name from a predefined list
        domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "example.com"]
        domain = random.choice(domains)

        # Combine to form email
        email = f"{username}@{domain}"
        return email

    def generate_random_password(self,length=12):
        # Define characters to include in password
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate random password
        password = ''.join(random.choices(characters, k=length))
        return password

    def get_success_message(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissable']//span")))
        text = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']//span").text.strip()
        print(text)
        return text