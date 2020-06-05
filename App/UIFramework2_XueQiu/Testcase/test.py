#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from App.UIFramework2_XueQiu.Page.App import App


class Test:
    def setup_class(self):
        self.main = App().start().main()

    def test_search(self):
        search = self.main.goto_market().goto_search().search()
        print(search.is_favorate())
        # if search.is_favorate() is True:
        #     search.remove_favorate()
        # assert search.add_favorate().is_favorate() is True
