from base.selenium_drivers import SeleniumDriver
import utilities.custom_logger as cl
import logging


class Navigation(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    _home = ".menu-header .menu:nth-child(4) [href='https\:\/\/www\.tekrevol\.com']"  # css
    _about = ".menu-header .menu:nth-child(4) .current_page_item .nav"  # css
    _portfolio = ".menu-header .menu:nth-child(4) > li:nth-of-type(3)"  # css
    _services = ".has-dropdown-menu\.html .nav"  # css
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
    _contact_us = ".menu-header .menu:nth-child(4) li:nth-of-type(6) .nav"  # css

    def Home(self):
        self.elementClick(self._home, locatorType='css')

    def About(self):
        self.elementClick(self._about, locatorType='css')

    def Portfolio(self):
        self.elementClick(self._portfolio, locatorType='css')

    def AppDevelopment(self):
        self.mouseHover(self._services, locatorType='css')
        self.mouseClick(self._app_development, locatorType='css')

    def AndroidDevelopment(self):
        self.mouseHover(self._services, locatorType='css')
        self.mouseClick(self._android_development, locatorType='css')

    def IphoneDevelopment(self):
        self.mouseHover(self._services, locatorType='css')
        self.mouseClick(self._iphone_development, locatorType='css')

    def WebDevelopment(self):
        self.mouseHover(self._services, locatorType='css')
        self.mouseClick(self._web_development, locatorType='css')

    def GameDevelopment(self):
        self.mouseHover(self._services, locatorType='css')
        self.mouseClick(self._game_development, locatorType='css')

    def WearableDevelopment(self):
        self.mouseHover(self._services, locatorType='css')
        self.mouseClick(self._wearable_development, locatorType='css')

    def MobileAppSupport(self):
        self.mouseHover(self._services, locatorType='css')
        self.mouseClick(self._mobile_app_support, locatorType='css')

    def StartupPrototype(self):
        self.mouseHover(self._services, locatorType='css')
        self.mouseClick(self._startup_prototype, locatorType='css')

    def SupportMaintenance(self):
        self.mouseHover(self._services, locatorType='css')
        self.mouseClick(self._support_maintenance, locatorType='css')

    def IpProtection(self):
        self.mouseHover(self._services, locatorType='css')
        self.mouseClick(self._ip_protection, locatorType='css')

    def Blog(self):
        self.elementClick(self._blog, locatorType='link')

    def ContactUs(self):
        self.elementClick(self._contact_us, locatorType='css')