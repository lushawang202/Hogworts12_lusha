#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from App.UIFramework1_XueQiu.Page.wrapper import handle_black


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @handle_black
    def find(self, locator, value=None):
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    def finds(self, locator, value=None):
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    def click(self, locator, value=None):
        if isinstance(locator, tuple):
            do = self.find(*locator).click()
        else:
            do = self.find(locator, value).click()
        return do

    def sendkeys(self, locator, value=None, text=''):
        if isinstance(locator, tuple):
            do = self.find(*locator).send_keys(text)
        else:
            do = self.find(locator, value).send_keys(text)
        return do

    def wait_to_click(self, locator):
        WebDriverWait(self._driver, 5).until(expected_conditions.element_to_be_clickable(locator))
