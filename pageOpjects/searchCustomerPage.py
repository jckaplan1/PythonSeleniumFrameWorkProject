import  selenium

class SearchCustomer():
    txtEmail_id = "SearchEmail"
    textFirstName = "SearchFirstName"
    textLastName = "SearchLastName"
    btnsearchCust_id = 'search-customers'
    table_xpath = "//table[@id='customers-grid']/tbody"
    tablerows_xpath  = "//table[@id='customers-grid']/tbody/tr"
    tablecolumn_xpath = "//table[@id='customers-grid']/tbody/tr/td"



    def __init__(self,driver):
        self.driver = driver


    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element_by_id(self.textFirstName).clear()
        self.driver.find_element_by_id(self.textFirstName).send_keys(fname)

    def setLasttName(self, lname):
            self.driver.find_element_by_id(self. textLastName).clear()
            self.driver.find_element_by_id(self. textLastName).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnsearchCust_id).click()


    def numberOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tablecolumn_xpath))


    def searchCustomerByEmail(self,email):
        try:
            flag = False
            for r in range(1, self.numberOfRows() + 1):
                table = self.driver.find_element_by_xpath(self.table_xpath)
                emailid = self.driver.find_element_by_xpath(
                    "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
                if emailid == email:
                    flag = True
                    break
            return flag
        except:
            print("This email is not in the list.")


    def searchCustomerByName(self,name):
        try:
            flag = False
            for r in range(1, self.numberOfRows() + 1):
                table = self.driver.find_element_by_xpath(self.table_xpath)
                nameid = self.driver.find_element_by_xpath(
                    "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
                if nameid == name:
                    flag = True
                    break

            return flag
        except:
            print("This name is not in the list")


