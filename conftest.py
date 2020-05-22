#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from test_code.test_Calc import Test_Calc


def pytest_collection_modifyitems(session, config, items):
    print(items)
    for item in items:
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        elif 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)


@pytest.fixture(autouse=True)
def init():
    print("Unittest starts： ")
    yield
    print("Unittest completes! ")
