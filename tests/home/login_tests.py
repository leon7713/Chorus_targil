from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        driverLocation = "C:\\Users\\Leonidus\\IdeaProjects\\testselenium\\drivers\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        baseURL = "https://learn.letskodeit.com/"
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")


        avatarIcon = driver.find_element(By.CLASS_NAME, "gravatar")
        if avatarIcon is not None:
            print("Login Successful")
        else:
            print("Login failed")

ff = LoginTests()
ff.test_validLogin()