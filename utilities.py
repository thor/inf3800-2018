#!/usr/bin/python
# -*- coding: utf-8 -*-

import heapq

def apply(function, iterable):
    """
    Applies the given function to each item in the given iterable.

    Similar to the built-in map/2, at least how map/2 used to work in Python 2.7.x. However,
    in Python 3.x map/2 returns an iterator that is evaluated lazily. This poses a problem
    if the return value from map/2 is never traversed and the intent of using of map/2 was
    really to trigger some side-effect from the function application. This utility method
    avoids that, and was written when porting Python 2.7.x code to Python 3.x.
    """
    for item in iterable:
        function(item)
