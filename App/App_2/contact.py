#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from App.App_2.base_page import BasePage
from App.App_2.invite_by import InviteBy


class Contact(BasePage):

    def add_member(self):
        self.scroll_find("添加成员").click()
        return InviteBy(self._driver)

    def get_member(self, name):
        try:
            self.wait_to_click((MobileBy.XPATH, name))
            self.scroll_find(name).click()
            return True
        except NoSuchElementException:
            return True
        except:
            return False

    def goto_profile(self, name):
        from App.App_2.profile import Profile
        self.scroll_find(name).click()
        return Profile(self._driver)

    def goto_message(self):
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/drh']//*[@text='消息']").click()
