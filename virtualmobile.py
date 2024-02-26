from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

desired_caps = {
    "deviceName": "Galaxy S21 5G",
    "platformName": "Android",
    "platformVersion": "11",
    "isRealMobile": False,
    "build": "Python Vanilla Android",
    "name": "Sample Test - Python",
    "network": False,
    "visual": True,
    "video": True,
    "tunnel":True
}


def startingTest():

    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  "shubhamr"+":"+"dl8Y8as59i1YyGZZUeLF897aCFvIDmaKkUU1e6RgBmlgMLIIhh"+"@hub.lambdatest.com/wd/hub")

        driver.get("https://demo.playwright.dev/api-mocking/")

        time.sleep(15)

        driver.quit()
    except:
        driver.quit()


startingTest()