#!/usr/bin/python
# -*- coding: utf-8 -*-

class PostingsMerger:

    def __init__(self):
        pass

    def intersection(self, p1, p2):
        """
        A generator that yields a simple AND of two posting lists, given
        iterators over these.

        The posting lists are assumed sorted in increasing order according
        to the document identifiers.
        """
        raise NotImplementedError

    def union(self, p1, p2):
        """
        A generator that yields a simple OR of two posting lists, given
        iterators over these.

        The posting lists are assumed sorted in increasing order according
        to the document identifiers.
        """
        raise NotImplementedError
