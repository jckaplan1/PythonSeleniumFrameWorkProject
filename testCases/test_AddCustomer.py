import string
import random
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from  pageOpjects.loginPage import Login
from pageOpjects.addCustommerPage import AddCustomer
import time
import pytest

class Test_003_AddCustomer():
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("*************Test_003_AddCustomer*********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        time.sleep(3)
        self.lp = Login(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.login_button()
        self.logger.info("*************login successful*********")

        self.logger.info("************Starting Add Customer*********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clcikCustomerMenu()
        self.addcust.clcikCustomerMenuItem()
        self.addcust.clickAddCustomer()

        self.logger.info("************Providing Customer Information*********")
        self.email = random_generator()+ '@gmail.com'
        self.fname = random_generator()
        self.password = random_generatorn()+random_generator()
        self.addcust.addEmail(self.email)
        self.addcust.addPassword(self.password)

        self.addcust.addFirstName(self.fname)
        self.addcust.addLastName('Jiyre')
        self.addcust.selectGender('male')
        self.addcust.addDob('05/15/1990')
        self.addcust.addCompanyName('Apple')
        self.addcust.addCustomerRoles('Guests')
        self.addcust.addManagerRole('Vendor 1')
        self.addcust.addAdminComment('This hybrid frame work very useful')
        time.sleep(3)
        self.addcust.saveCustomer()
        self.logger.info("************Saving Customer Information*********")

        self.logger.info("************Verifying Customer validation*********")
        self.msg = self.driver.find_element_by_tag_name("body").text

        if 'The new customer has been added successfully.' in self.msg:
            assert True ==True
            self.logger.info("************Add Customer Passed*********")
        else:
            self.driver.save_screenshot(".\\Screenshots"+"test_addCustomer.png")
            self.logger.info("************Add Customer Failed*********")
            assert True == False



        self.driver.close()



#Generating string character

def random_generator(size =8,chars = string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))

#Generating integer number
def random_generatorn(size =8,int = string.digits):
    return ''.join(random.choice(int) for x in range(size))