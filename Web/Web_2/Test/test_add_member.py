#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

from Web.Web_2.Page.base_page import Base_Page
from Web.Web_2.Page.index import Index


class Test_AddMember:
    # def __init__(self):
    #     self.index = Index()

    def setup(self):
        self.index = Index()

    def test_add_member(self, name="aaaaa"):
        goto_contact = self.index.goto_login().goto_main().goto_contact()
        list = goto_contact.get_member()
        if name in list:
            goto_contact.del_member(name)
        goto_contact.goto_add_member().add_member()
        final_list = goto_contact.get_member()
        if name in final_list:
            print("测试通过")
            assert True
        else:
            print("测试未通过")
            assert False

# if __name__ == '__main__':
#     Test_AddMember().test_add_member()
