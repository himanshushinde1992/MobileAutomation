from appium import webdriver


class Driver:

    def getDriver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'WK8DWSMJAASGLREM'
        desired_caps['app'] = ("J:\\appium\\Appium tuts\\General-Store.apk")
        desired_caps['appPackage'] = 'com.androidsample.generalstore'
        desired_caps['appActivity'] = 'com.androidsample.generalstore.SplashActivity'
        # desired_caps['FullReset'] = False

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver
