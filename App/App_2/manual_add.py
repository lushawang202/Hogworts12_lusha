#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from App.App_2.base_page import BasePage


class ManualAdd(BasePage):

    def input_name(self):
        WebDriverWait(self._driver, 5).until(
            expected_conditions.element_to_be_clickable((MobileBy.ID, 'com.tencent.wework:id/b65')))
        self.find(MobileBy.XPATH,
                  '//*[@resource-id="com.tencent.wework:id/dwa"]//*[@text="必填"]').send_keys("aaa")
        return self

    def set_gender(self):
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/dvu"]//*[@text="男"]').click()
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b_9"]//*[@text="女"]').click()
        return self

    def input_tel(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/er6').send_keys("15831212858")
        return self

    def click_save(self):
        from App.App_2.invite_by import InviteBy
        self.find(MobileBy.ID, 'com.tencent.wework:id/gvy').click()

        return InviteBy(self._driver)
