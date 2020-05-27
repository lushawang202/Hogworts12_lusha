#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        # options = Options()
        # options.debugger_address = "127.0.0.1:9222"
        if driver is not None:
            self._driver = driver
        else:
            self._driver = webdriver.Chrome()
            # self._driver = webdriver.Chrome(options=options)
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find_ele(self, by, value):
        return self._driver.find_element(by, value)

    def find_eles(self, by, value):
        return self._driver.find_elements(by, value)

    def wait_to_click(self, locator, time=10):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))
