import time

from utilities import xlutliles
from utilities.readproperties import ReadConfig
from pageobject.Loginpage import LoginPage
from utilities.logger import LogGen


class TestDataDriver:
    file = "C:\\Users\\suraj\\Desktop\\automation project\\new project nope commerce\\testdata\\data.xlsx"
    url = ReadConfig.get_url()
    log = LogGen.loggen()

    def test_Case001(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.log.info("********* Browser is opened ********")
        self.lp = LoginPage(self.driver)
        self.row =xlutliles.row_num(self.file,'Sheet2')
        status = []

        for i in range(2, self.row+1):
            self.email = xlutliles.read_data(self.file, "Sheet2", i, 1)
            self.password = xlutliles.read_data(self.file, "Sheet2", i, 2)
            self.expected = xlutliles.read_data(self.file, "Sheet2", i, 3)
            self.lp.set_username(self.email)
            self.lp.set_password(self.password)
            self.lp.click_login()

            if self.driver.title == "Dashboard / nopCommerce administration":
                if self.expected == "pass":
                    self.driver.save_screenshot(
                        "C:\\Users\\suraj\\Desktop\\automation project\\new project nope commerce\\screenshots\\"
                        +self.email + "passloged.png")
                    status.append("pass")
                    xlutliles.write_data(self.file,"Sheet2", i, 4, "pass")
                    self.lp.logout()

                elif self.expected == "fail":
                    self.driver.save_screenshot(
                        "C:\\Users\\suraj\\Desktop\\automation project\\new project nope commerce\\screenshots\\"
                        +self.email +"logedd.png")
                    status.append("fail")
                    xlutliles.write_data(self.file, "Sheet2", i, 4, "fail")
                    self.lp.logout()

            else:
                if self.expected == "pass":
                    self.driver.save_screenshot(
                        "C:\\Users\\suraj\\Desktop\\automation project\\new project nope commerce\\screenshots\\"
                        +self.email+"logedd.png")
                    status.append("fail")
                    xlutliles.write_data(self.file, "Sheet2", i, 4, "fail")
                elif self.expected == "fail":
                    self.driver.save_screenshot(
                        "C:\\Users\\suraj\\Desktop\\automation project\\new project nope commerce\\screenshots\\"
                        + self.email +"logedd.png")
                    status.append("pass")
                    xlutliles.write_data(self.file, "Sheet2", i, 4, "pass")

        if "fail" not in status:
            assert True
        else:
            assert False




