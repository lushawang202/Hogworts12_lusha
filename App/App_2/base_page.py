#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _black_list = [
        (MobileBy.XPATH, "//*[@text='确认']"),
        (MobileBy.XPATH, "//*[@text='下次再说']"),
        (MobileBy.XPATH, "//*[@text='确定']"),
    ]
    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value=None):
        logging.info(locator)
        logging.info(value)
        try:
            element = self._driver.find_element(*locator) if isinstance(locator,
                                                                        tuple) else self._driver.find_element(
                locator, value)
            self._error_num = 0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            for ele in self._black_list:
                logging.info(ele)
                self._driver.implicitly_wait(1)
                locators = self._driver.find_elements(*ele)
                if len(locators) > 0:
                    locators[0].click()
                    return self.find(locator, value)

    def finds(self, locator, value=None):
        return self._driver.find_elements(*locator) if isinstance(locator, tuple) else self._driver.find_elements(
            locator, value)

    def scroll_find(self, value: str):
        return self._driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(' + '"' + value + '"' + ').instance(0));')

    def wait_to_click(self, locator):
        WebDriverWait(self._driver, 5).until(expected_conditions.element_to_be_clickable(locator))
