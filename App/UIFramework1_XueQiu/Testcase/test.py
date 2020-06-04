#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from App.UIFramework1_XueQiu.Page.App import App


class Test:
    def setup_class(self):
        self.main = App().start().main()

    def test_search(self):
        assert self.main.goto_market().goto_search().search().add_favorate().is_favorate() is True
