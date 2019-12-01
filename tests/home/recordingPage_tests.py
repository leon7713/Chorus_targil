from pages.home.recording_page import RecordingPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RecordingPageTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rp = RecordingPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_login(self):
        result = self.rp.loginPageHandle()
        self.ts.mark(result, "Title verified")

    @pytest.mark.run(order=2)
    def test_play_call(self):
        self.rp.playCall()

    @pytest.mark.run(order=3)
    def test_verify_search_field(self):
        self.rp.searchTranscript()
