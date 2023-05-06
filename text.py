#!/usr/bin/env python
# -*- coding: utf-8 -*-
import log2file
import logging

# from multiprocessing import Pool
from multiprocessing.dummy import Pool
import time
import random

log2file.init(console=True, name="test")

# for root logger, don't use this or you will get many many logs,and all other loggers will be shadowed by root logger
# log2file.init(console=True)

trace_test = log2file.trace(name="test")
# this is the trace for root logger, don't use this if you have not init root logger
trace_root = log2file.trace()


for i in range(20):
    log2file.init(console=True, name=str(i))

for i in range(20):
    log2file.init(console=True, name=str(i))


@trace_test("test_test111")
def s():
    time.sleep(0.1 + random.randint(0, 100) / 1000)


@trace_root("root_debug")
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
