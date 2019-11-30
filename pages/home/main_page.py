import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class MainPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    # _login_link = "Login"
    # _email_field = "user_email"
    # _password_field = "user_password"
    # _login_button = "[name = commit]"

    _eurosport_main_title = ".nav__logo"
    _main_items = "categorylist__item"
    _hamburger = ".hamburger"

    # def clickLoginLink(self):
    #     self.elementClick(self._login_link, locatorType="link")
    #
    # def enterEmail(self, email):
    #     self.sendKeys(email, self._email_field, locatorType="id")
    #
    # def enterPassword(self, password):
    #     self.sendKeys(password, self._password_field, locatorType="id")
    #
    # def clickOnLoginButton(self):
    #     self.elementClick(self._login_button, locatorType="css")
    #
    # def login(self, email="", password=""):
    #     self.clickLoginLink()
    #     self.enterEmail(email)
    #     self.enterPassword(password)
    #     self.clickOnLoginButton()
    #
    # def verifyLoginSuccessful(self):
    #     result = self.isElementPresent("gravatar", locatorType="class")
    #     return result
    #
    # def verifyLoginFailed(self):
    #     result = self.isElementPresent(".alert.alert-danger", locatorType="css")
    #     return result
    #
    # def verifyLoginTitle(self):
    #     return self.verifyPageTitle("Let's Kode It")

    def verifyMainPage(self):
        result = self.isElementPresent(self._eurosport_main_title, "css")
        self.elementClick(self._hamburger, "css")
        time.sleep(2)
        return result