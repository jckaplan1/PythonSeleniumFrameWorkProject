import time
import pytest

from pageOpjects.loginPage import Login
from pageOpjects.addCustommerPage import AddCustomer
from pageOpjects.searchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_searchCustomerByEmail_004:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchCustomerByEmail(self,setup):
        self.driver = setup
        self.logger.info("***********searchCustomerByEmail***********")

        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.login_button()
        self.logger.info("***********Login Successful***********")

        self.logger.info("***********Starting searchCustomer ByEmail***********")
        self.ac = AddCustomer(self.driver)
        self.ac.clcikCustomerMenu()
        self.ac.clcikCustomerMenuItem()

        self.sc = SearchCustomer(self.driver)
        self.sc.setEmail('Christ80@email.com')
        self.sc.clickSearch()
        time.sleep(3)
        status  = self.sc.searchCustomerByEmail('Christ80@email.com')
        assert True == status
        self.logger.info("***********Test_searchCustomerByEmail_004 finished ***********")
        self.driver.close()
