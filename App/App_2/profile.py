#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from App.App_2.base_page import BasePage
from App.App_2.edit_profile import EditProfile


class Profile(BasePage):
    def goto_edit(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/gvr").click()
        self.find(MobileBy.ID, "com.tencent.wework:id/azn").click()
        return EditProfile(self._driver)
