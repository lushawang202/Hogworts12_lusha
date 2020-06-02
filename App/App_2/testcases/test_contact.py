#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml

from App.App_2.app import App


class TestContact:
    def setup_class(self):
        self.app = App()
        self.contact = self.app.start().main().goto_contact()

    @pytest.mark.parametrize("name, gender, tel",
                             yaml.safe_load(open("../data/data.yml", encoding='utf-8'))['add_data'])
    def test_add_contact(self, name, gender, tel):
        assert "成功" in self.contact.add_member().invite_manual().input_name(name).set_gender(
            gender).input_tel(tel).click_save().get_toast()

    @pytest.mark.parametrize("name", yaml.safe_load(open("../data/data.yml", encoding='utf-8'))['del_data'])
    def test_del_member(self, name):
        assert self.contact.goto_profile(name).goto_edit().del_member().get_member(name) is False
