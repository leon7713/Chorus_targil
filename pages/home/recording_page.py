import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class RecordingPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    emailData = "leonid.ushar@chorus-auto.com"
    passwordData = "V>q9U-a6Q5"

    # Locators
    _email_field = "input[name *= email]"
    _password_field = "input[name *= password]"
    _login_button = "//*[text() = 'Log In']"
    _continueToChorus_button = "//*[text() = 'Continue to Chorus.ai']"
    _meeting_title = "h2[title *= Meeting]"
    _play_icon_player = ".icon.fa.fa-lg.white.fa-play"
    _pause_icon_player = ".icon.fa.fa-lg.white.fa-pause"
    _search_meeting_transcript = "//div/span/input"
    _search_button = "//button[text() = 'Search']"
    _show_result = "//*[text() = 'show']"

    def loginPageHandle(self):
        self.sendKeys(self.emailData, self._email_field, "css")
        self.elementClick(self._login_button, "xpath")
        self.sendKeys(self.passwordData, self._password_field, "css")
        self.elementClick(self._continueToChorus_button, "xpath")
        result = self.isElementPresent(self._meeting_title, "css")
        return result

    def playCall(self):
        self.elementClick(self._play_icon_player, "css")
        result = self.isElementPresent(self._pause_icon_player, "css")
        assert result == True

    def searchTranscript(self):
        self.sendKeys("show", self._search_meeting_transcript, "xpath")
        self.elementClick(self._search_button, "xpath")
        result = self.isElementPresent(self._show_result, "xpath")
        assert result == True
        time.sleep(3)
