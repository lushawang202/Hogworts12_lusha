#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy


def handle_black(func):
    def wrapper(*args, **kwargs):
        _black_list = [(MobileBy.XPATH, "//*[@text='下次再说']"),
                       (MobileBy.XPATH, "//*[@text='确定']"),
                       (MobileBy.XPATH, "//*[@text='确认']"),
                       ]
        error_num = 1
        error_max = 3
        from App.UIFramework1_XueQiu.Page.base_page import BasePage
        instance: BasePage = args[0]
        while True:
            try:
                element = func(*args, **kwargs)
                error_num = 0
                instance._driver.implicitly_wait(10)
                return element
            except Exception as e:
                if error_num > error_max:
                    raise e
                instance._driver.implicitly_wait(1)
                _black_try = 0
                for ele in _black_list:
                    elements = instance.finds(*ele)
                    if len(elements) > 0:
                        elements[0].click()
                        break
                    if len(elements) == 0:
                        _black_try += 1
                if _black_try == len(_black_list):
                    raise e
                error_num += 1

    return wrapper
