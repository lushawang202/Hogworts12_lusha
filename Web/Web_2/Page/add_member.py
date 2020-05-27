#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Web.Web_2.Page.base_page import Base_Page


class AddMember(Base_Page):

    def add_member(self):
        self.wait_to_click((By.CSS_SELECTOR, "#username"))
        self.find_ele(By.ID, "username").send_keys("aaaaa")
        self.find_ele(By.ID, "memberAdd_english_name").send_keys("bbbbb")
        self.find_ele(By.ID, "memberAdd_phone").send_keys("13811111111")
        self.find_ele(By.ID, "memberAdd_acctid").send_keys("ab")
        self.wait_to_click((By.CSS_SELECTOR, ".js_btn_save"))
        self.find_ele(By.CSS_SELECTOR, ".js_btn_save").click()
