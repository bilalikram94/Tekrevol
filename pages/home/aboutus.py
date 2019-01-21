from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class AboutUs(BasePage):
    log = cl.customLogger(logging.DEBUG)
    about_us = ".journey-main .heading-rotated div"  # CSS
    our_vision = ".journey h3"  # CSS
    our_vision_text = ".journey p"  # CSS
    more_about_us = "MORE ABOUT US"  # Link Text
    why_tekrevol = ".our-expertise h2"  # CSS
    guaranteed_client = "headingOne"  # id
    integrated_solutions = "headingTwo"  # id
    dynamic_web = "headingFour"  # id
    mobile_responsive = "headingFive"  # id
    customized_solutions = "Customized Solutions"  # link
    app_support = "App Support Services"  # link
    guaranteed_client_text = ".panel-default:nth-of-type(1) [class='col-xs-12 info']"  # CSS
    integrated_solutions_text = ".panel-default:nth-of-type(2) [class='col-xs-12 info']"  # CSS
    dynamic_web_text = ".panel-default:nth-of-type(3) [class='col-xs-12 info']"  # CSS
    mobile_responsive_text = ".panel-default:nth-of-type(4) [class='col-xs-12 info']"  # CSS
    customized_solutions_text = ".panel-default:nth-of-type(5) [class='col-xs-12 info']"  # CSS
    app_support_text = ".panel-default:nth-of-type(6) [class='col-xs-12 info']"  # CSS

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verifyAboutUs(self):
        self.scrollIntoView(self.about_us, locatorType="css")
        result = self.isElementPresent(self.about_us, locatorType='css')
        return result

    def verifyOurVision(self):
        result = self.isElementPresent(self.our_vision, locatorType='css')
        return result

    def verifyMoreAboutUs(self):
        self.waitForElement(self.more_about_us, locatorType='link')
        result = self.isElementPresent(self.more_about_us, locatorType='link')
        return result

    def verifyWhyTekrevol(self):
        result = self.isElementPresent(self.why_tekrevol, locatorType='css')
        return result

    def verifyGuaranteedClient(self):
        result = self.isElementPresent(self.guaranteed_client)
        return result

    def verifyIntegratedSolutions(self):
        result = self.isElementPresent(self.integrated_solutions)
        return result

    def verifyDynamicWeb(self):
        result = self.isElementPresent(self.dynamic_web)
        return result

    def verifyMobileResponsive(self):
        result = self.isElementPresent(self.mobile_responsive)
        return result

    def verifyCustomizedSolutions(self):
        result = self.isElementPresent(self.customized_solutions, locatorType='link')
        return result

    def verifyAppSupport(self):
        result = self.isElementPresent(self.app_support, locatorType='link')
        return result

    def AboutUsAll(self):
        result = self.verifyAboutUs()
        self.stat.mark(result, "Verify About Us")
        result2 = self.verifyOurVision()
        self.stat.mark(result2, "Verify Our Vision")
        result3 = self.verifyMoreAboutUs()
        self.stat.mark(result3, "Verify More About Us")
        result4 = self.verifyWhyTekrevol()
        self.stat.mark(result4, "Verify Why Tekrevol")
        result5 = self.verifyGuaranteedClient()
        self.stat.mark(result5, "Verify Guaranteed Clients")
        result6 = self.verifyIntegratedSolutions()
        self.stat.mark(result6, "Verify Integrated Solutions")
        result7 = self.verifyDynamicWeb()
        self.stat.mark(result7, "Verify Dynamic Web")
        result8 = self.verifyMobileResponsive()
        self.stat.mark(result8, "Verify Mobile Responsive")
        result9 = self.verifyCustomizedSolutions()
        self.stat.mark(result9, "Verify Customized Solutions")
        result10 = self.verifyAppSupport()
        self.stat.markFinal("Verify About Us All", result10, "Verify App Support")
