from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random
from time import sleep

class AddCustomer():

    linkCustomer_menu_xpath = "//a[@href='#']//p[contains (text(),'Customers')]"
    linkCustomer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains (text(),'Customers')]"
    linkAddCustomer_xpath = "//a[@href='/Admin/Customer/Create']"

    txtEmail_id = "Email"
    textPassword_id ="Password"
    textFirstName = "FirstName"
    textLastName = "LastName"

    rdbtnmale_id= "Gender_Male"
    rdbtnfmale_id = "Gender_Female"

    textDob_id = "DateOfBirth"
    textCompanyName_id = "Company"

    textCustomerRoles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    listItemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    listItemForummoderator_xpath = "//li[contains(text(),'Forum Moderators')]"
    listItemGuest_xpath  = "//li[contains(text(),'Guests')]"
    listItemRegistered_xpath  = "//li[contains(text(),'Registered')]"
    listItemDeleteRgistered_xpath= "//span[@title='delete']"
    listItemVendor_xpath  = "//li[contains(text(),'Vendors')]"
    listManagerRoles_id = 'VendorId'



    textAdminComment_id = "AdminComment"
    buttonSave_xpath = "//button[@name='save']"


    def  __init__(self,driver):
        self.driver = driver

    def clcikCustomerMenu(self):
        self.driver.find_element_by_xpath(self.linkCustomer_menu_xpath).click()

    def clcikCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.linkCustomer_menuitem_xpath).click()

    def clickAddCustomer(self):
        self.driver.find_element_by_xpath(self.linkAddCustomer_xpath).click()

    def addEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)


    def addPassword(self,password):
        self.driver.find_element_by_id(self.textPassword_id).send_keys(password)


    def addFirstName(self,fname):
        self.driver.find_element_by_id(self.textFirstName).send_keys(fname)

    def addLastName(self,lname):
        self.driver.find_element_by_id(self.textLastName).send_keys(lname)

    def selectGender(self,gender):
        if gender == 'male':
            self.driver.find_element_by_id(self.rdbtnmale_id).click()

        else:
            self.driver.find_element_by_id(self.rdbtnfmale_id).click()

    def addDob(self,dob):
        self.driver.find_element_by_id(self.textDob_id).send_keys(dob)

    def addCompanyName(self,cname):
        self.driver.find_element_by_id(self.textCompanyName_id).send_keys(cname)

    def addCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.textCustomerRoles_xpath)
        sleep(2)
        if role == 'Administrator':
           self.listitem =  self.driver.find_element_by_xpath(self.listItemAdministrators_xpath)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element_by_xpath(self.listItemForummoderator_xpath)

        elif role == 'Guests':
            self.driver.find_element_by_xpath(self.listItemDeleteRgistered_xpath).click()
            self.listitem = self.driver.find_element_by_xpath(self.listItemGuest_xpath)

        elif role == 'Vendors':
            self.listitem =  self.driver.find_element_by_xpath(self.listItemVendor_xpath)

        sleep(2)
        self.driver.execute_script('arguments[0].click();', self.listitem)
        # self.listitem.click()
    def addManagerRole(self,mrole):
        self.select = Select(self.driver.find_element_by_id(self.listManagerRoles_id))
        all_options = [n.get_attribute('value') for n in self.select.options]
        for x in all_options:
            self.select.select_by_visible_text(mrole)


    def addAdminComment(self,comment):
        self.driver.find_element_by_id(self.textAdminComment_id).send_keys(comment)

    def saveCustomer(self):
        self.driver.find_element_by_xpath(self.buttonSave_xpath).click()









