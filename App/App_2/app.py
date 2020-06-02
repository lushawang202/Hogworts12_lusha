#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver

from App.App_2.main import Main
from App.App_2.base_page import BasePage


class App(BasePage):
    def start(self):
        if self._driver == None:
            caps = {}
            caps["platform"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["noReset"] = "true"
            caps["dontStopAppOnReset"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        return Main(self._driver)
