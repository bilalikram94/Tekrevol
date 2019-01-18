"""
@package base

Base Page Class Implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base.selenium_drivers import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
from utilities.teststatus import Status
from pages.home.navigation import Navigation


class BasePage(SeleniumDriver):
    def __init__(self, driver):
        """
        Inits BasePage class
        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()
        self.stat = Status(driver)
        self.nav = Navigation(driver)

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title
        Parameters:
             titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("### Failed to get page title !!!")
            print_stack()
            return False
