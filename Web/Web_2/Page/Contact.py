#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Web.Web_2.Page.add_member import AddMember
from Web.Web_2.Page.base_page import Base_Page


class Contact(Base_Page):

    def get_member(self):
        self.wait_to_click((By.CSS_SELECTOR, ".js_invite_member"))
        elements = self.find_eles(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        list = [element.get_attribute("title") for element in elements]
        return list
        # for element in elements:
        #     list.append(element.get_attribute("title"))

    def del_member(self, name):
        self.wait_to_click((By.CSS_SELECTOR, ".js_invite_member"))
        elements = self.find_eles(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        for element in elements:
            if element.get_attribute("title") == name:
                element.click()
                self.wait_to_click((By.CSS_SELECTOR, ".js_del_member"))
                self.find_ele(By.CSS_SELECTOR, ".js_del_member").click()
                self.wait_to_click((By.LINK_TEXT, "确认"))
                self.find_ele(By.LINK_TEXT, "确认").click()
        return Contact(self._driver)

    def goto_add_member(self):
        self.wait_to_click((By.CSS_SELECTOR, ".js_invite_member"))
        self.find_ele(By.CSS_SELECTOR, ".js_add_member:nth-child(2)").click()
        return AddMember(self._driver)
