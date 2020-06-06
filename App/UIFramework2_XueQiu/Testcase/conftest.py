#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shlex
import signal
import subprocess
import pytest


@pytest.fixture(scope='module', autouse=True)
def record():
    cmd = shlex.split('scrcpy --record test.mp4')
    p = subprocess.Popen(cmd)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
