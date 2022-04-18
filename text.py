#!/usr/bin/env python
# -*- coding: utf-8 -*-
import log2file
import logging

# from multiprocessing import Pool
from multiprocessing.dummy import Pool
import time
import random

log2file.init(console=True)
trace = log2file.trace


@trace("test")
def s():
    time.sleep(0.1 + random.randint(0, 100) / 1000)


@trace("debug")
def s2():
    time.sleep(0.1 + random.randint(0, 100) / 1000)


def fun(t):
    log = logging.getLogger(name=str(t))
    for i in range(100):
        s()
        log.debug("this is a test [{0}]-[{1}]".format(t, i))
        s2()


p = Pool(10)
p.map(fun, range(20))
p.close()
p.join()
