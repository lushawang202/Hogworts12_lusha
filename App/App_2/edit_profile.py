#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from App.App_2.base_page import BasePage


class EditProfile(BasePage):
    def del_member(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/dvn").click()
        self.find(MobileBy.ID, "com.tencent.wework:id/b_d").click()
        # print(self._driver.page_source)
        self.wait_to_click((MobileBy.XPATH, "//*[@text='通讯录']"))
        print(self._driver.page_source)

        from App.App_2.contact import Contact
        return Contact(self._driver)
