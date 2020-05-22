#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import Decimal

import allure
import pytest
from dev_code.Calculator import Calc
import yaml


def fetch_data(data_name):
    with open('../data/CalcData.yml', encoding='utf-8') as f:
        data = yaml.safe_load(f)[data_name]
        return data


steps = yaml.dump(yaml.safe_load(open('../data/CalcMethod.yml')))


@allure.feature("计算器模块")
class Test_Calc:
    def setup(self):
        self.calc = Calc()

    @allure.story("加法：数字型")
    @pytest.mark.parametrize('a, b, expect', fetch_data("Add_alnum"))
    def calc_add_num(self, a, b, expect):
        if 'add' in steps:
            with allure.step("读取所有数据'Add_alnum'并运行程序计算结果a+b"):
                result = self.calc.add(a, b)
            with allure.step("四舍五入保留计算结果15位小数"):
                result = round(result, 15)
            with allure.step("对比计算结果与预期结果"):
                assert result == round(expect, 15)
        else:
            raise UserWarning

    @allure.story("加法：字符型")
    @pytest.mark.parametrize('a, b, expect', fetch_data("Add_str"))
    def calc_add_str(self, a, b, expect):
        if 'add' in steps:
            with allure.step("读取所有数据'Add_str'并运行程序计算结果a+b"):
                result = self.calc.add(a, b)
            with allure.step("对比计算结果与预期结果"):
                assert result == expect
        else:
            raise UserWarning

    @allure.story("除法：数字型（非0）")
    @pytest.mark.parametrize('a, b, expect', fetch_data("Div_num"))
    def calc_div_num(self, a, b, expect):
        if 'div' in steps:
            with allure.step("读取所有数据'Div_num'并运行程序计算结果a/b"):
                result = self.calc.div(a, b)
            with allure.step("四舍五入保留计算结果15位小数"):
                result = round(result, 15)
            with allure.step("对比计算结果与预期结果"):
                assert result == round(expect, 15)
        else:
            raise UserWarning

    @allure.story("除法：数字型（0）")
    @pytest.mark.parametrize('a, b, expect', fetch_data("Div_0exc"))
    def calc_div_0exc(self, a, b, expect):
        if 'div' in steps:
            with allure.step("读取所有数据'Div_0exc'并运行程序计算结果a/b"):
                result = self.calc.div(a, b)
            with allure.step("对比计算结果与预期结果"):
                assert result == expect
        else:
            raise UserWarning

    @allure.story("除法：字符型")
    @pytest.mark.xfail
    @pytest.mark.parametrize('a, b, expect', fetch_data("Div_str"))
    def calc_div_str(self, a, b, expect):
        if 'div' in steps:
            with allure.step("读取所有数据'Div_str'并运行程序计算结果a/b"):
                result = self.calc.div(a, b)
            with allure.step("对比计算结果与预期结果"):
                assert result == expect
        else:
            raise UserWarning

    @allure.story("减法：数字型")
    @pytest.mark.parametrize('a, b, expect', fetch_data("Sub_alnum"))
    def calc_sub_num(self, a, b, expect):
        if 'sub' in steps:
            with allure.step("读取所有数据'Sub_alnum'并运行程序计算结果a-b"):
                result = self.calc.sub(a, b)
            with allure.step("四舍五入保留计算结果15位小数"):
                result = round(result, 15)
            with allure.step("对比计算结果与预期结果"):
                assert result == round(expect, 15)
        else:
            raise UserWarning

    @allure.story("减法：字符型")
    @pytest.mark.parametrize('a, b, expect', fetch_data("Sub_str"))
    def calc_sub_str(self, a, b, expect):
        if 'sub' in steps:
            with allure.step("读取所有数据'Sub_str'并运行程序计算结果a-b"):
                result = self.calc.sub(a, b)
            with allure.step("对比计算结果与预期结果"):
                assert result == expect
        else:
            raise UserWarning

    @allure.story("乘法：数字型")
    @pytest.mark.parametrize('a, b, expect', fetch_data("Mul_alnum"))
    def calc_mul_num(self, a, b, expect):
        if 'mul' in steps:
            with allure.step("读取所有数据'mul_alnum'并运行程序计算结果a*b"):
                result = self.calc.mul(a, b)
            with allure.step("四舍五入保留计算结果15位小数"):
                result = round(result, 15)
            with allure.step("对比计算结果与预期结果"):
                assert result == round(expect, 15)
        else:
            raise UserWarning

    @allure.story("乘法：字符型")
    @pytest.mark.parametrize('a, b, expect', fetch_data("Mul_str"))
    def calc_mul_str(self, a, b, expect):
        if 'mul' in steps:
            with allure.step("读取所有数据'Mul_str'并运行程序计算结果a*b"):
                result = self.calc.mul(a, b)
            with allure.step("对比计算结果与预期结果"):
                assert result == expect
        else:
            raise UserWarning
