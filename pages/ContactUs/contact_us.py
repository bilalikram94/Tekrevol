from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class ContactUs(BasePage):
    log = cl.customLogger(logging.DEBUG)

    _name = "[action] [type='text']:nth-of-type(2)"  # By CSS
    _designation = "[action] [type='text']:nth-of-type(3)"  # By CSS
    _your_email = "[action] .field3:nth-of-type(4)"  # By CSS
    _your_company = "[action] [type='text']:nth-of-type(5)"  # By CSS
    _phone_number = "[action] [type='text']:nth-of-type(6)"  # By CSS
    _project_type = "//form[@id='contact_form']/select[@name='project_type']"  # By xpath
    _get_in_touch = "[onclick='submit_contact\(\)']"  # By CSS
    _get_a_quote = "GET A QUOTE"  # link
    _image = ".col17 p"  # CSS

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def SendkeysName(self, name):
        self.elementClick(self._name, locatorType='css')
        self.sendKeys(name, self._name, locatorType='css')

    def SendkeysDesignation(self, designation):
        self.elementClick(self._designation, locatorType='css')
        self.sendKeys(designation, self._designation, locatorType='css')

    def SendkeysYourEmail(self, email):
        self.elementClick(self._your_email, locatorType='css')
        self.sendKeys(email, self._your_email, locatorType='css')

    def SendkeysYourCompany(self, company):
        self.elementClick(self._your_company, locatorType='css')
        self.sendKeys(company, self._your_company, locatorType='css')

    def SendkeysPhoneNumber(self, number):
        self.elementClick(self._phone_number, locatorType='css')
        self.sendKeys(number, self._phone_number, locatorType='css')

    def SelectProjectType(self, value):
        self.dropDownList(self._project_type, locatorType='xpath', val=value)

    def clickGetInTouch(self):
        self.elementClick(self._get_in_touch, locatorType='css')

    def ContactSmoke(self):
        self.elementClick(self._get_a_quote, locatorType='link')
        self.scrollIntoView(self._image, locatorType='css')
        result1 = self.isElementPresent(self._designation, locatorType='css')
        self.stat.mark(result1, "Designation is present")
        result = self.isElementPresent(self._name, locatorType='css')
        self.stat.mark(result, "Name Is Present")
        result2 = self.isElementPresent(self._your_email, locatorType='css')
        self.stat.mark(result2, "Email is present")
        result3 = self.isElementPresent(self._your_company, locatorType='css')
        self.stat.mark(result3, "Company is present")
        result4 = self.isElementPresent(self._phone_number, locatorType='css')
        self.stat.mark(result4, "Phone Number IS Present")
        result5 = self.isElementPresent(self._project_type, locatorType='xpath')
        self.stat.mark(result5, "Project Type is present")
        result6 = self.isElementPresent(self._get_in_touch, locatorType='css')
        self.stat.markFinal("Contact Smoke Test", result6, "Get In Touch is Present")

    def ContactTest(self, name, designation, email, company, number, value):
        self.SendkeysName(name)
        time.sleep(2)
        self.SendkeysDesignation(designation)
        time.sleep(2)
        self.SendkeysYourEmail(email)
        time.sleep(2)
        self.SendkeysYourCompany(company)
        time.sleep(2)
        self.SendkeysPhoneNumber(number)
        time.sleep(2)
        self.SelectProjectType(value)
        time.sleep(2)
        self.clickGetInTouch()
