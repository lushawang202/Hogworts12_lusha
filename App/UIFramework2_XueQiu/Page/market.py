#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from App.UIFramework2_XueQiu.Page.base_page import BasePage
from App.UIFramework2_XueQiu.Page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps('../Data/market.yaml')
        return Search(self._driver)
