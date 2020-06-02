#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to, equal_to
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup_class(self):
        caps = {}
        caps["platform"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = "true"
        caps["dontStopAppOnReset"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    def setup(self):
        print("测试开始：")

    def teardown(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()

    @pytest.mark.parametrize('name, code, expected_price', [('alibaba', 'BABA', 200),
                                                            ('xiaomi', '01810', 12)])
    def test_search(self, name, code, expected_price):
        el2 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search")
        el2.click()
        el3 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text")
        el3.click()
        el3.send_keys(name)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((MobileBy.XPATH, f'//*[@text="{code}"]/../..')))
        el4 = self.driver.find_element(MobileBy.XPATH, f'//*[@text="{code}"]/../..')
        el4.click()
        price_ele = self.driver.find_element(MobileBy.XPATH,
                                             f'//*[@text="{code}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
        current_price = float(price_ele.text)
        assert_that(current_price, close_to(expected_price, expected_price * 0.1))
