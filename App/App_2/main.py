#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from App.App_2.base_page import BasePage
from App.App_2.contact import Contact


class Main(BasePage):

    def goto_contact(self):
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/ggq']//*[@text='通讯录']").click()
        return Contact(self._driver)
