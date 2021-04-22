from  selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
"""
Login page locators and methods

"""

class Login():

    """*************** Locators for login Page *********"""
    def __init__(self, driver):
        self.driver = driver
        self.textbox_username_id = 'Email'
        self.textbox_password_id = 'Password'
        self.link_login_xpath = "//button[contains(text(),'Log in')]"
        self.link_logout_xpath = "//a[contains(text(),'Logout')]"



    """*************** Methods for login Page *********"""

    def enterUsername(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)


    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def login_button(self):
        self.driver.find_element_by_xpath(self.link_login_xpath).click()


    def click_logout(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()















