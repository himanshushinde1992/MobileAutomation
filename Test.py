from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from AppiumFramework.Base.BasePage import BasePage

"""
Desired capabilites: 
Desired Capabilities are keys and values encoded in a JSON object, 
sent by Appium clients to the server when a new automation session is requested. 
They tell the Appium drivers all kinds of important things about how you want your test to work. 
Each Appium client builds capabilities in a way specific to the client's language, 


# """
# Desired_cap = {
#     "platformName": "Android",
#     "platformVersion": "7.0",
#     "deviceName": "WK8DWSMJAASGLREM",
#     # "app": "J:\\yotubevideo\\Appium tuts\\NoBroker6.8.211.apk",
#     "app": "C:\\Users\\user\\Downloads\\Invoice pro.apk",
#     "automationName": "UiAutomator2",
#     "appPackage": "com.sohmware.invoice",
#     # "appActivity": "com.sohmware.invoice.ui.SplashScreen"
#
#
# }

# Part 1 "Desired Capabilities"

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'WK8DWSMJAASGLREM'
desired_caps['app'] = ("J:\\copied docus\\Chess Free.apk")
# desired_caps['appPackage'] = 'com.androidsample.generalstore'
# desired_caps['appActivity'] = 'com.androidsample.generalstore.SplashActivity'

"""
Creating driver instance
"""
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.activate_app()
print("current activity", driver.current_activity)
print("check the app type ,", driver.current_context)
print("orentiation", driver.orientation)
print("device state", driver.is_locked())
time.sleep(30)
text = "India"
# # Entering the name in the text field
# # country_selection = driver.find_elements_by_id("com.androidsample.generalstore:id/spinnerCountry")
# uiSelector = "new UiSelector().textMatches("\"" + text + "\")";
#
# command = "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView("
# + uiSelector +")
#
#
# driver.find_element_by_android_uiautomator(command);
#
# driver.find_element_by_id("com.androidsample.generalstore:id/nameField").send_keys("Himanshu Shinde")
# driver.find_element_by_id("com.androidsample.generalstore:id/radioFemale").is_enabled()
# driver.find_element_by_id("com.androidsample.generalstore:id/btnLetsShop").click()
# print("Moaved to next page")
# # scroll script
# wait = WebDriverWait(driver, 25, poll_frequency=1,
#                      ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
#                                          NoSuchElementException])
# ele = wait.until(lambda x: x.find_element_by_android_uiautomator('text("ScrollView")'))
# ele.click()
# wait.until(lambda x: x.find_element_by_android_uiautomator(
#     'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))')).click()
# driver.scro
driver.find_elements_by_class_name()
driver.find_element_by_android_uiautomator("UiSelector().index(2)")
driver.