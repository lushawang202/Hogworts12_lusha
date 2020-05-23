#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def pytest_collection_modifyitems(session, config, items):
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
def info():
    print("Unittest starts： ")
    yield
    print("Unittest completes! ")
