#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

from Web.Web_2.Page.base_page import Base_Page
from Web.Web_2.Page.index import Index


class Test_AddMember:
    # def __init__(self):
    #     self.index = Index()
    _name = 'aaaaa'

    def setup(self):
        self.index = Index()

    def teardown(self):
        self.index.quit_browser()

    def test_add_member(self):
        goto_contact = self.index.goto_login().goto_main().goto_contact()
        flag = goto_contact.get_member(self._name)
        if flag:
            print("已使用")
            goto_contact.del_member(self._name)
        goto_contact.goto_add_member().add_member()
        assert goto_contact.get_member(self._name)
# #
# if __name__ == '__main__':
#     Test_AddMember().test_add_member()
