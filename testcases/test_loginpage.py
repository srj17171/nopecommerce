import time

import pytest

from pageobject.Loginpage import LoginPage
from utilities.logger import LogGen
from utilities.readproperties import *
from selenium import webdriver


class TestLogin:
    url = ReadConfig.get_url()
    password = ReadConfig.get_password()
    username = ReadConfig.get_username()
    mail = ReadConfig.get_mail()
    config = ReadConfig()
    log = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.suraj
    def test001(self, setup):
        self.log.info("******* Test1 is started ***********")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.driver.get(self.url)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        title = self.driver.title

        if title == "Dashboard / nopCommerce administration":
            self.log.info("************* Test1 is passed")
            self.driver.save_screenshot(
                "C:\\Users\\suraj\\Desktop\\automation project\\new project nope commerce\\screenshots\\test002.png")
            self.lp.logout()
            self.driver.close()
            assert True

        else:
            self.log.error("****************** Error is happend *********")
            self.driver.save_screenshot(
                "C:\\Users\\suraj\\Desktop\\automation project\\new project nope commerce\\screenshots\\test001fail2.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_002(self, setup):
        self.log.info("************ Test2 has started ***********")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.driver.get(self.url)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        time.sleep(5)
        self.lp.expand_cust()
        self.lp.customer_menu()
        self.lp.search_mail(self.mail)
        if self.driver.title == "Customers / nopCommerce administration":
            self.driver.save_screenshot("screenshots\\test2passed.png")
            self.log.info("***************** Test is passed **********")
            self.lp.logout()
            self.driver.close()
            assert True
        else:
            self.log.info("**************** Test2 is faile ************")
            self.driver.save_screenshot("screenshots\\test2failed.png")
            self.lp.logout()
            self.driver.close()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test003(self):
        a = 5
        self.log.info("*********** Test 3 has started **********")
        if a == 5:
            self.log.info("************ test 3 is passed ********")
            assert True
        else:
            self.log.info("************ test 3 is failed ********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.suraj
    def test004(self):
        a = 6
        self.log.info("*********** Test 4 has started **********")
        if a == 5:
            self.log.info("************ test 4 is passed ********")
            assert True
        else:
            self.log.info("************ test 4 is failed ********")
            assert False

    @pytest.mark.regression
    def test006(self):
        a = 18
        self.log.info("*********** Test 6 has started **********")
        if a == 5:
            self.log.info("************ test 6 is passed ********")
            assert True
        else:
            self.log.info("************ test 6 is failed ********")
            assert False
