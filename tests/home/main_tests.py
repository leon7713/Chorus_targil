from pages.home.main_page import MainPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.mp = MainPage(self.driver)
        self.ts = TestStatus(self.driver)

    # @pytest.mark.run(order=2)
    # def test_validLogin(self):
    #     self.mp.login("test@email.com", "abcabc")
    #     result1 = self.mp.verifyLoginTitle()
    #     self.ts.mark(result1, "Title verified")
    #     result2 = self.mp.verifyLoginSuccessful()
    #     self.ts.markFinal("test_validLogin", result2, "Login was not successful")
    #
    # @pytest.mark.run(order=1)
    # def test_invalidLogin(self):
    #     self.mp.login("", "abcabc7")
    #     result = self.mp.verifyLoginFailed()
    #     assert result == True

    @pytest.mark.run(order=1)
    def test_validMainPage(self):
        result = self.mp.verifyMainPage()
        self.ts.mark(result, "Title verified")