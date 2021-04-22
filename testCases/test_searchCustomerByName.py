import time
import pytest

from pageOpjects.loginPage import Login
from pageOpjects.addCustommerPage import AddCustomer
from pageOpjects.searchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_searchCustomerByName_005:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchCustomerByName(self,setup):
        self.driver = setup
        self.logger.info("***********searchCustomerByName***********")

        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.login_button()

        self.ac = AddCustomer(self.driver)
        self.ac.clcikCustomerMenu()
        self.ac.clcikCustomerMenuItem()
        self.logger.info("***********Starting searchCustomer ByName***********")
        self.sc = SearchCustomer(self.driver)
        self.sc.setFirstName('Steve')
        self.sc.setLasttName('Gates')
        self.sc.clickSearch()
        time.sleep(3)
        status  = self.sc.searchCustomerByName('Steve Gates')
        assert True == status
        self.logger.info("***********Test_searchCustomerByName_005 finished ***********")
        self.driver.close()



