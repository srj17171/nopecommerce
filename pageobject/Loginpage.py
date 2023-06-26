from selenium.webdriver.common.by import By


class LoginPage:

    userid_box_xpath = "//input[@id='Email']"
    pass_box_xpath = "//input[@id='Password']"
    login_btn_click = "//button[@type='submit']"
    logout_btn_click = "//a[normalize-space()='Logout']"
    Customer_menu_exp_xpath = "//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]"
    customer_menu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    search_by_mail_xpath = "//input[@id='SearchEmail']"
    search_btn_xpath = "//button[@id='search-customers']//i[@class='fas fa-search']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.userid_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.userid_box_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.pass_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.pass_box_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_btn_click).click()

    def logout(self):
        self.driver.find_element(By.XPATH, self.logout_btn_click).click()

    def expand_cust(self):
        self.driver.find_element(By.XPATH, self.Customer_menu_exp_xpath).click()

    def customer_menu(self):
        self.driver.find_element(By.XPATH, self.customer_menu_xpath).click()

    def search_mail(self, mail):
        self.driver.find_element(By.XPATH, self.search_by_mail_xpath).send_keys(mail)
        self.driver.find_element(By.XPATH, self.search_btn_xpath).click()

