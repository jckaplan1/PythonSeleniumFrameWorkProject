class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.link_logout_linkText = 'Logout'


    def click_logout(self):
        self.driver.find_element_by_link_text(self.link_logout_linkText).click()