#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Web.Web_2.Page.base_page import Base_Page
from Web.Web_2.Page.login import Login


class Index(Base_Page):
    _base_url = "https://work.weixin.qq.com/"

    def goto_login(self):
        self.find_ele(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)
