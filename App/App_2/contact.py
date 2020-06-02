#!/usr/bin/env python
# -*- coding: utf-8 -*-

from App.App_2.base_page import BasePage
from App.App_2.invite_by import InviteBy


class Contact(BasePage):

    def add_member(self):
        self.scroll_find("添加成员").click()
        return InviteBy(self._driver)
