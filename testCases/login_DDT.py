from selenium import webdriver
from  pageOpjects.loginPage import Login
from pageOpjects.homePage import HomePage
import unittest
from time import sleep
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


"""" Testing Login validation with Data Driven Test Method by reading credential information from excel file"""

class Test_002DDT_login:

    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    """ Excel file path"""
    path = ".\\TestData\\login.xlsx"

    @pytest.mark.regression
    def test_login_valid_ddt(self,setup):
        self.logger.info('************Verifying Loginpage************')
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lg = Login(self.driver)
        self.rows= XLUtils.getRowCount(self.path,'test')
        print('number of rows ', self.rows)
        list_status = []
        """ Reading data from excel file in directory-path"""
        for r in range(2, self.rows+1):
            self.username = XLUtils.readData(self.path,'test',r,1)
            self.password = XLUtils.readData(self.path, 'test', r, 2)
            self.exp = XLUtils.readData(self.path, 'test', r, 3)

            """Using the credential  data which retrieved from excel file"""
            self.lg.enterUsername(self.username)
            self.lg.setPassword(self.password)
            self.lg.login_button()
            sleep(3)

            """verifying if login is succesfull with checking title"""

            if self.driver.title == 'Dashboard / nopCommerce administration':
                if self.exp == 'pass':
                    self.logger.info('*****Passed')
                    self.lg.click_logout()
                    list_status.append('pass')
                elif self.exp == 'fail':
                    print(self.exp)
                    self.logger.info('*****Failed')
                    self.driver.save_screenshot(".\\Screenshots\\" + "login_DDT.png")
                    self.lg.click_logout()
                    list_status.append('fail')
            elif self.driver.title != 'Dashboard / nopCommerce administration':
                if self.exp == 'pass':
                    self.logger.info('******fail')
                    list_status.append('fail')
                    self.driver.save_screenshot(".\\Screenshots\\" + "login_DDT.png")
                elif self.exp == 'fail':
                    self.logger.info('***pass')
                    list_status.append('pass')

            """" Writing status list values in excel file"""

            XLUtils.writeData(self.path, 'test', r, 4,list_status[r-2])
            # print(str(list_status[r-2]), ' new list')
        # Verifying if test pass by checking if list_status has fail
        if 'fail' not in list_status:
            self.logger.info('***Loging DDT Pass***')
            self.driver.close()
            assert True
        else:
            self.logger.error('***Loging DDT Failed***')
            self.driver.close()
            assert False








