#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from App.UIFramework1_XueQiu.Page.base_page import BasePage


class Search(BasePage):
    def search(self):
        self.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys('alibaba')
        self.click(MobileBy.XPATH, "//*[@text='BABA']")
        return self

    def add_favorate(self):
        self.click(MobileBy.XPATH, '//*[@text="BABA"]/../../..//*[@text="加自选"]')
        return self

    def is_favorate(self):
        elements = self.finds(MobileBy.XPATH, '//*[@text="BABA"]/../../..//*[@text="已添加"]')
        return len(elements) > 0
