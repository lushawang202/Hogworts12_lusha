#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from App.App_2.base_page import BasePage


class ManualAdd(BasePage):

    def input_name(self, name):
        self.wait_to_click((MobileBy.ID, 'com.tencent.wework:id/b65'))
        self.find(MobileBy.XPATH,
                  '//*[@resource-id="com.tencent.wework:id/dwa"]//*[@text="必填"]').send_keys(name)
        return self

    def set_gender(self, gender):
        if gender == "男":
            self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/dvu"]//*[@text="男"]').click()
            self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b_9"]//*[@text="男"]').click()

        if gender == "女":
            self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/dvu"]//*[@text="男"]').click()
            self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b_9"]//*[@text="女"]').click()

        return self

    def input_tel(self, tel):
        self.find(MobileBy.ID, 'com.tencent.wework:id/er6').send_keys(tel)
        return self

    def click_save(self):
        from App.App_2.invite_by import InviteBy
        self.find(MobileBy.ID, 'com.tencent.wework:id/gvy').click()
        return InviteBy(self._driver)
