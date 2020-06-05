#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from App.UIFramework2_XueQiu.Page.base_page import BasePage
from App.UIFramework2_XueQiu.Page.market import Market
from App.UIFramework2_XueQiu.Page.search import Search


class Main(BasePage):
    def goto_market(self):
        # self.steps('../Data/search.yaml', )
        self.click(MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")
        return Market(self._driver)

    def goto_search(self):
        self.click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/tv_search']")
        return Search(self._driver)
