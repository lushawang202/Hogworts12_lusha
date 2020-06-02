#!/usr/bin/env python
# -*- coding: utf-8 -*-
from App.App_2.app import App


class TestContact:
    def setup(self):
        self.main = App().start().main()

    def teardown(self):
        pass

    def test_contact(self):
        assert "成功" in self.main.goto_contact().add_member().invite_manual().input_name().set_gender().input_tel().click_save(). \
            get_toast()
