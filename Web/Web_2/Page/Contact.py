#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from Web.Web_2.Page.add_member import AddMember
from Web.Web_2.Page.base_page import Base_Page


class Contact(Base_Page):
    def get_page_number(self):
        page_ele = self.find_ele(By.CSS_SELECTOR, ".ww_pageNav_info_text")
        page_number: str = page_ele.text
        return [int(a) for a in page_number.split('/', 1)]

    def get_member(self, _name):
        self.wait_to_click((By.CSS_SELECTOR, ".js_invite_member"))
        page_elements = self.find_eles(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        page_member = [element.get_attribute("title") for element in page_elements]
        ele = self.find_ele(By.CSS_SELECTOR, ".ww_pageNav ")
        if _name in page_member:
            return True
        elif ele.is_displayed():
            cur_page, total_page = self.get_page_number()
            while True:
                self.find_ele(By.CSS_SELECTOR, ".js_next_page").click()
                page_elements = self.find_eles(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
                for element in page_elements:
                    if _name == element.get_attribute("title"):
                        return True
                cur_page = self.get_page_number()[0]
                if cur_page == total_page:
                    return False
        else:
            return False

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
        print("删除成功")

    def goto_add_member(self):
        self.wait_to_click((By.CSS_SELECTOR, ".js_invite_member"))
        self.find_ele(By.CSS_SELECTOR, ".js_add_member:nth-child(2)").click()
        return AddMember(self._driver)
