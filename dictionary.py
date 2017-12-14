#!/usr/bin/python
# -*- coding: utf-8 -*-

class InMemoryDictionary:
    """
    A simple lexicon that maps a vocabulary term to an integer code. Sometimes
    it's easier and more efficient to work with integers than strings, e.g., so
    that we can use the integers as direct indexes into lists/arrays and other
    lookup structures. With N strings in total we want to map these to the integer
    set {0, .., N - 1}, i.e., a perfect hash.

    A simple in-memory implementation for demonstration purposes, suitable for
    small vocabularies.
    """

    def __init__(self):
        self._terms = {}

    def __iter__(self):
        for item in self._terms.items():
            yield item

    def __repr__(self):
        return str(self._terms)

    def size(self):
        """
        Returns the size of the lexicon, i.e., the number of unique terms added
        to the lexicon.
        """
        return len(self._terms)

    def add_if_absent(self, term):
        """
        Adds a new term to the lexicon. If the term already exists in the lexicon,
        the lexicon is left unchanged. The associated term identifier is returned.
        """
        term_id = self.get_term_id(term)
        if term_id < 0:
            term_id = self.size()
            self._terms[term] = term_id
        return term_id

    def get_term_id(self, term):
        """
        Looks up the given term in the lexicon and returns the term's corresponding
        integer code. If the term is not present in the lexicon, -1 is returned.
        """
        return self._terms.get(term, -1)

if __name__ == "__main__":
    vocabulary = InMemoryDictionary()
    vocabulary.add_if_absent("foo")
    vocabulary.add_if_absent("bar")
    vocabulary.add_if_absent("foo")
    assert vocabulary.size() == 2
    assert vocabulary.get_term_id("foo") == 0
    assert vocabulary.get_term_id("bar") == 1
    assert vocabulary.get_term_id("wtf") == -1
    print(vocabulary)
