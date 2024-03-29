#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Singleton(type):
    """
    Dark Magic
    Class meta as Singleton will have only one instance forever.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Cls:
    __metaclass__ = Singleton

    def __init__(self):
        pass
