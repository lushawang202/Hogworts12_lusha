#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from App.UIFramework2_XueQiu.Page.main import Main


class App:
    _driver: WebDriver

    def start(self):
        caps = dict()
        caps["platform"] = 'Android'
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = " com.xueqiu.android"
        caps["appActivity"] = ".common.MainActivity"
        caps["noReset"] = "true"
        caps['newCommandTimeout'] = 6000
        # caps["dontStopAppOnReset"] = True
        self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self._driver.implicitly_wait(10)
        return self

    def main(self) -> Main:
        return Main(self._driver)

    def stop(self):
        self._driver.close_app()

    def reset(self):
        self._driver.reset()

    def back(self):
        self._driver.back()
