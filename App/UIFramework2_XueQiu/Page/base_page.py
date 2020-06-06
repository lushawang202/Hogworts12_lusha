#!/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect
import json

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from App.UIFramework2_XueQiu.Page.wrapper import handle_black


class BasePage:
    _input_param = {}

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

    def steps(self, path):

        func_name = inspect.stack()[1].function
        with open(path, encoding='utf-8') as f:
            steps = yaml.safe_load(f)[func_name]
        yaml_str = json.dumps(steps)
        for key, value in self._input_param.items():
            yaml_str = yaml_str.replace(f'${{{key}}}', value)
        steps = json.loads(yaml_str)
        for step in steps:
            if 'action' in step.keys():
                action = step['action']
                if 'sendkeys' in action:
                    self.sendkeys(step['by'], step['value'], step['text'])
                if 'click' in action:
                    self.click(step['by'], step['value'])
                if 'if_elements' in action:
                    elements = self.finds(step['by'], step['value'])
                    return len(elements) > 0
                if 'find' in action:
                    self.find(step['by'], step['value'])
            else:
                print('没有找到步骤')

    def screenshot(self, filename):
        self._driver.save_screenshot(filename)
