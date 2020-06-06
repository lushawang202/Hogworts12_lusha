#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shlex
import subprocess

import pytest
import yaml

from App.UIFramework2_XueQiu.Page.App import App


class Test:
    def setup_class(self):
        self.market = App().start().main().goto_market()

    def teardown(self):
        self.search.click_cancel()

    @pytest.mark.parametrize("name, code", yaml.safe_load(open('../Data/test_data.yaml', encoding='utf-8')))
    def test_search(self, name, code):
        self.search = self.market.goto_search()
        search = self.search.search(name, code)
        if search.is_favorate(code) is True:
            search.remove_favorate(code)
        assert search.add_favorate(code).is_favorate(code) is True
