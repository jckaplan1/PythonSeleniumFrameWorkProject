from selenium import webdriver
from  pageOpjects.loginPage import Login
from pageOpjects.homePage import HomePage
import unittest
from time import sleep
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

''' Testing login validation by using data from conftest.py -with hard code'''
class Test_001_login:

    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    """" Verifying Home page """

    @pytest.mark.regression
    def test_home_page(self,setup):
        self.logger.info("************Test_001_login************")
        self.logger.info('************Verifying HomePageTitle************')
        self.driver = setup
        self.driver.get(self.baseurl)

        if self.driver.title == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info('************Homepage title test passed************')
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"homepage.png")
            self.driver.close()
            self.logger.error('************Homepage title test failed************')
            assert False

    """" Verifying login validation """

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_valid(self,setup):
        self.logger.info('************Verifying Loginpage************')
        self.driver = setup
        self.driver.get(self.baseurl)
        lg = Login(self.driver)
        lg.enterUsername(self.username)
        lg.setPassword(self.password)
        lg.login_button()

        if self.driver.title == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"logintest.png")
            self.driver.close()
            assert False





    # def test_home_page(self,setup):
    # self.driver =setup
    #     driver = setup
    #     hp =HomePage(driver)
    #     if driver.title == 'Dashboard / nopCommerce administration':
    #         assert True
    #     else:
    #         assert False
    #     hp.click_logout()



