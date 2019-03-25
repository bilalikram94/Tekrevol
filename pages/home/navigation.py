from base.selenium_drivers import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


class Navigation(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    _home = ".menu-header .menu:nth-child(4) [href='https//:www.tekrevol.com']"  # css
    _about = "/html[1]/body[1]/main[1]/div[1]/header[1]/div[1]/div[2]/div[3]/nav[1]/div[1]/ul[1]/li[2]/a[1]"  # css
    _portfolio = "PORTFOLIO"  # link-text
    _text = "[class='col-sm-6 text-col'] h1"  # CSS
    _services = ".has-dropdown-menu\.html [href='https\:\/\/www\.tekrevol\.com\/services']"  # xpath
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
    _blog = "BLOG"  # link text
    _contact_us = "CONTACT US"  # link
    _get_a_quote = "GET A QUOTE"  # link

    def Home(self):
        self.elementClick(self._home, locatorType='css')

    def About(self):
        self.elementClick(self._about, locatorType='xpath')

    def Portfolio(self):
        self.elementClick(self._portfolio, locatorType='link')

    def Services(self):
        self.mouseHover(self._services, locatorType='css')

    def AppDevelopment(self):
        self.Services()
        self.mouseClick(self._app_development, locatorType='css')

    def AndroidDevelopment(self):
        self.Services()
        self.mouseClick(self._android_development, locatorType='css')

    def IphoneDevelopment(self):
        self.Services()
        self.mouseClick(self._iphone_development, locatorType='css')

    def WebDevelopment(self):
        self.Services()
        self.mouseClick(self._web_development, locatorType='css')

    def GameDevelopment(self):
        self.Services()
        self.mouseClick(self._game_development, locatorType='css')

    def WearableDevelopment(self):
        self.Services()
        self.mouseClick(self._wearable_development, locatorType='css')

    def MobileAppSupport(self):
        self.Services()
        self.mouseClick(self._mobile_app_support, locatorType='css')

    def SupportMaintenance(self):
        self.Services()
        self.mouseClick(self._support_maintenance, locatorType='css')

    def Blog(self):
        self.elementClick(self._blog, locatorType='link')

    def ContactUs(self):
        self.elementClick(self._contact_us, locatorType='link')

    def GetAQuote(self):
        self.elementClick(self._get_a_quote, locatorType='link')

    def NavigationTest(self):
        self.About()
        time.sleep(2)
        self.Portfolio()
        time.sleep(2)
        self.AppDevelopment()
        time.sleep(2)
        self.AndroidDevelopment()
        time.sleep(2)
        self.IphoneDevelopment()
        time.sleep(2)
        self.WebDevelopment()
        time.sleep(2)
        self.GameDevelopment()
        time.sleep(2)
        self.WearableDevelopment()
        time.sleep(2)
        self.MobileAppSupport()
        time.sleep(2)
        self.SupportMaintenance()
        time.sleep(2)
        self.Blog()
        time.sleep(2)
        self.Home()