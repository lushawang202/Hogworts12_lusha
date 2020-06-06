#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from App.UIFramework2_XueQiu.Page.base_page import BasePage
from App.UIFramework2_XueQiu.Page.market import Market



class Main(BasePage):
    def goto_market(self):
        self.steps('../Data/main.yaml')
        return Market(self._driver)

    def goto_search(self):
        self.steps('../Data/main.yaml')
        from App.UIFramework2_XueQiu.Page.search import Search
        return Search(self._driver)
