from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class NavBar(BasePage):
    log = cl.customLogger(logging.DEBUG)

    # Locators
    _home = "//body[@id='home']//div[@role='toolbar']/header[@class='header']//nav[@class='nav']/div/ul" \
            "[@class='menu']//a[@href='https://www.tekrevol.com']"  # Xpath
    _about = "//body[@id='home']//div[@role='toolbar']/header//nav[@class='nav']/div/ul[@class='menu']" \
             "//a[@href='https://www.tekrevol.com/about']"  # Xpath
    _portfolio = "PORTFOLIO"  # Link Text
    _services = "/html//body[@id='home']//div[@role='toolbar']/header//nav[@class='nav']/div/ul[@class='menu']" \
                "//a[@href='https://www.tekrevol.com/services']"  # Xpath
    _contact_us = "//body[@id='home']//div[@role='toolbar']/header//nav[@class='nav']" \
                  "/div/ul[@class='menu']//a[@href='https://www.tekrevol.com/contact']"  # Xpath
    _get_a_quote = "GET A QUOTE"  # Link Text
    _title = "Innovative Web & Mobile Solutions | Tekrevol"
    _app_development = ".has-dropdown-menu\.html [href='https\:\/\/www\.tekrevol\.com\/app-development']"  # CSS
    _android_development = ".has-dropdown-menu\.html [href='https\:\/\/www\.tekrevol\.com\/android-app-development']"  # CSS
    _iphone_development = ".has-dropdown-menu\.html [href='https\:\/\/www\.tekrevol\.com\/iphone-app-development']"  # CSS
    _web_development = ".has-dropdown-menu\.html [href='https\:\/\/www\.tekrevol\.com\/web-development']"  # CSS
    _game_development = ".has-dropdown-menu\.html [href='https\:\/\/www\.tekrevol\.com\/game-development']"  # CSS
    _wearable_development = ".has-dropdown-menu\.html [href='https\:\/\/www\.tekrevol\.com\/wearable-app-development']"  # CSS
    _mobile_app_support = ".has-dropdown-menu\.html [href='https\:\/\/www\.tekrevol\.com\/mobile-app-support']"  # CSS
    _startup_prototype = ".has-dropdown-menu\.html [href='https\:\/\/www\.tekrevol\.com\/startup-prototype']"  # CSS
    _support_maintenance = ".has-dropdown-menu\.html [href='https\:\/\/www\.tekrevol\.com\/support-maintenance']"  # CSS
    _ip_protection = ".has-dropdown-menu\.html [href='https\:\/\/www\.tekrevol\.com\/ip-protection']"  # CSS

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verifyHome(self):
        result = self.isElementPresent(self._home, locatorType="xpath")
        return result

    def verifyAbout(self):
        result = self.isElementPresent(self._about, locatorType="xpath")
        return result

    def verifyPortfolio(self):
        result = self.isElementPresent(self._portfolio, locatorType="link")
        return result

    def verifyContactUs(self):
        result = self.isElementPresent(self._contact_us, locatorType="xpath")
        return result

    def verifyServices(self):
        result = self.isElementPresent(self._services, "xpath")
        return result

    def verifyAppDevelopment(self):
        self.mouseHover(self._services, locatorType='xpath')
        result = self.isElementPresent(self._app_development, locatorType='css')
        return result

    def verifyAndroidDevelopment(self):
        self.mouseHover(self._services, locatorType='xpath')
        result = self.isElementPresent(self._android_development, locatorType='css')
        return result

    def verifyIphoneDevelopment(self):
        self.mouseHover(self._services, locatorType='xpath')
        result = self.isElementPresent(self._iphone_development, locatorType='css')
        return result

    def verifyWebDevelopment(self):
        self.mouseHover(self._services, locatorType='xpath')
        result = self.isElementPresent(self._web_development, locatorType='css')
        return result

    def verifyGameDevelopment(self):
        self.mouseHover(self._services, locatorType='xpath')
        result = self.isElementPresent(self._game_development, locatorType='css')
        return result

    def verifyWearableDevelopment(self):
        self.mouseHover(self._services, locatorType='xpath')
        result = self.isElementPresent(self._wearable_development, locatorType='css')
        return result

    def verifyMobileAppSupport(self):
        self.mouseHover(self._services, locatorType='xpath')
        result = self.isElementPresent(self._mobile_app_support, locatorType='css')
        return result

    def verifyStartupPrototype(self):
        self.mouseHover(self._services, locatorType='xpath')
        result = self.isElementPresent(self._startup_prototype, locatorType='css')
        return result

    def verifySupportMaintenance(self):
        self.mouseHover(self._services, locatorType='xpath')
        result = self.isElementPresent(self._support_maintenance, locatorType='css')
        return result

    def verifyIpProtection(self):
        self.mouseHover(self._services, locatorType='xpath')
        result = self.isElementPresent(self._ip_protection, locatorType='css')
        return result

    def verifyGetaQuote(self):
        result = self.isElementPresent(self._get_a_quote, locatorType="link")
        return result

    def verifyTextHome(self, _text_home):
        result = self.util.verifyTextContains(self.getText(self._home, locatorType="xpath"), _text_home)
        return result

    def verifyTextAbout(self, _text_about):
        result = self.util.verifyTextContains(self.getText(self._about, locatorType="xpath"), _text_about)
        return result

    def verifyTextPortfolio(self, _text_portfolio):
        result = self.util.verifyTextContains(self.getText(self._portfolio, locatorType="link"), _text_portfolio)
        return result

    def verifyTextContactUs(self, _text_contact_us):
        result = self.util.verifyTextContains(self.getText(self._contact_us, locatorType="xpath"), _text_contact_us)
        return result

    def verifyTextServices(self, _text_services):
        result = self.util.verifyTextContains(self.getText(self._services, locatorType="xpath"), _text_services)
        return result

    def verifyTextGetaQuote(self, _get_a_quote):
        result = self.util.verifyTextContains(self.getText(self._get_a_quote, locatorType='link'), _get_a_quote)
        return result

    def verifyTextNavBar(self, _text_home, _text_about, _text_portfolio, _text_contact_us, _text_services,
                         _text_get_a_quote):
        result = self.verifyTextHome(_text_home)
        self.stat.mark(result, "Verify Text Home")
        result1 = self.verifyTextAbout(_text_about)
        self.stat.mark(result1, "Verify Text About")
        result2 = self.verifyTextPortfolio(_text_portfolio)
        self.stat.mark(result2, "Verify Text Portfolio")
        result3 = self.verifyTextContactUs(_text_contact_us)
        self.stat.mark(result3, "Verify Text Contact Us")
        result4 = self.verifyTextServices(_text_services)
        self.stat.mark(result4, "Verify Text Services")
        result5 = self.verifyTextGetaQuote(_text_get_a_quote)
        self.stat.markFinal("Verify Text Home Page", result5, "Verify Text Get A Quote")

    def verifyNavBar(self):
        self.verifyPageTitle(self._title)
        result = self.verifyHome()
        self.stat.mark(result, "Verify Home")
        result1 = self.verifyAbout()
        self.stat.mark(result1, "Verify About")
        result2 = self.verifyContactUs()
        self.stat.mark(result2, "Verify Contact Us")
        result3 = self.verifyGetaQuote()
        self.stat.mark(result3, "Verify Get a Quote")
        result4 = self.verifyPortfolio()
        self.stat.mark(result4, "Verify Portfolio")
        result5 = self.verifyServices()
        self.stat.mark(result5, "Verify Services")
        result6 = self.verifyAppDevelopment()
        self.stat.mark(result6, "Verify App Development")
        result7 = self.verifyAndroidDevelopment()
        self.stat.mark(result7, "Verify Android Development")
        result8 = self.verifyIphoneDevelopment()
        self.stat.mark(result8, "Verify Iphone Development")
        result9 = self.verifyWebDevelopment()
        self.stat.mark(result9, "Verify Web Development")
        result10 = self.verifyGameDevelopment()
        self.stat.mark(result10, "Verify Game Development")
        result11 = self.verifyWearableDevelopment()
        self.stat.mark(result11, "Verify Wearable Development")
        result12 = self.verifyMobileAppSupport()
        self.stat.mark(result12, "Verify Mobile App Support")
        result13 = self.verifyStartupPrototype()
        self.stat.mark(result13, "Verify Startup Prototype")
        result14 = self.verifySupportMaintenance()
        self.stat.mark(result14, "Verify Support Maintenance")
        result15 = self.verifyIpProtection()
        self.stat.markFinal("Verify Nav Bar", result15, "Verify IP Protection")
