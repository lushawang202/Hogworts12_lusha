#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

# from Web.Web_2.Page.index import Index
from Web.Web_2.Page.base_page import Base_Page
from Web.Web_2.Page.main import Main


class Login(Base_Page):
    def goto_main(self):
        with shelve.open("cookies") as db:
            # db['cookies'] = self._driver.get_cookies()
            cookies = db['cookies']
            for cookie in cookies:
                if "expiry" in cookie.keys():
                    cookie.pop("expiry")
                self._driver.add_cookie(cookie)
        self._driver.refresh()
        return Main(self._driver)
