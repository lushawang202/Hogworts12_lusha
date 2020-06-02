#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from App.App_2.base_page import BasePage


class InviteBy(BasePage):

    def invite_manual(self):
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        from App.App_2.manual_add import ManualAdd
        return ManualAdd(self._driver)

    def get_toast(self):
        Toast = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
        return Toast.text
