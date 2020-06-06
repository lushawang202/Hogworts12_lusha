#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from App.UIFramework2_XueQiu.Page.base_page import BasePage


class Search(BasePage):
    _path = '../Data/search.yaml'

    def search(self, search_name, search_code):
        self._input_param['search_name'] = search_name
        self._input_param['search_code'] = search_code
        self.steps(self._path)
        return self

    def add_favorate(self, search_code):
        self._input_param['search_code'] = search_code
        self.steps(self._path)
        return self

    def is_favorate(self, search_code):
        self._input_param['search_code'] = search_code
        return self.steps(self._path)

    def remove_favorate(self, search_code):
        self._input_param['search_code'] = search_code
        self.steps(self._path)
        return self

    def click_cancel(self):
        self.steps(self._path)
        from App.UIFramework2_XueQiu.Page.main import Main
        return Main(self._driver)
