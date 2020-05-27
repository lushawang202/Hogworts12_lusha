#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Web.Web_2.Page.Contact import Contact
from Web.Web_2.Page.add_member import AddMember
from Web.Web_2.Page.base_page import Base_Page


class Main(Base_Page):
    def goto_add_member(self):
        self.wait_to_click((By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)"))
        self.find_ele(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMember(self._driver)

    def goto_contact(self):
        self.find_ele(By.LINK_TEXT, "通讯录").click()
        return Contact(self._driver)
