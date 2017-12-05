#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logger import Logger
import logging
#from multiprocessing import Pool
from multiprocessing.dummy import Pool
import time
import random

logger = Logger()
trace = logger.trace


@trace()
def s():
    time.sleep(0.1 + random.randint(0, 100) / 1000)


def fun(t):
    log = logging.getLogger(name=str(t))
    for i in range(100):
        s()
        log.debug('this is a test [{0}]-[{1}]'.format(t, i))


p = Pool(10)
p.map(fun, range(20))
p.close()
p.join()
