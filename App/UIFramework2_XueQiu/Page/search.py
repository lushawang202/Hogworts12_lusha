#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from App.UIFramework2_XueQiu.Page.base_page import BasePage


class Search(BasePage):
    _path = '../Data/search.yaml'

    def search(self):
        self.steps(self._path, 'search')
        # self.sendkeys(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']", 'alibaba')
        # self.click(MobileBy.XPATH, "//*[@text='BABA']")
        return self

    def add_favorate(self):
        self.steps(self._path, 'add_favorate')
        # self.click(MobileBy.XPATH, '//*[@text="BABA"]/../../..//*[@text="加自选"]')
        return self

    def is_favorate(self):
        # elements = self.finds(MobileBy.XPATH, '//*[@text="BABA"]/../../..//*[@text="已添加"]')
        self.steps(self._path, 'is_favorate')
        # return elements

    def remove_favorate(self):
        self.steps(self._path, 'remove_favorate')
        # self.click(MobileBy.XPATH, '//*[@text="BABA"]/../../..//*[@text="已添加"]')
        return self
