#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from App.UIFramework1_XueQiu.Page.base_page import BasePage
from App.UIFramework1_XueQiu.Page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        return Search(self._driver)
