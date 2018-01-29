#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import abstractmethod
import collections.abc


class Dictionary(collections.abc.Iterable):
    """
    Anstract base class for dictionaries that map vocabulary terms to integer codes.
    It's often easier and more efficient to work with integers than strings, e.g., so
    that we can use the integers as direct indexes into arrays and other lookup structures.
    With N strings in total we want to map these to the integer set {0, .., N - 1}, i.e.,
    a perfect hash.
    """

    def __len__(self):
        return self.size()

    def __getitem__(self, term: str) -> int:
        return self.get_term_id(term)

    @abstractmethod
    def size(self) -> int:
        """
        Returns the size of the dictionary, i.e., the number of unique terms added
        to the dictionary.
        """
        pass

    @abstractmethod
    def add_if_absent(self, term: str) -> int:
        """
        Adds a new term to the dictionary. If the term already exists in the dictionary,
        the dictionary is left unchanged. The associated term identifier is returned.
        """

    @abstractmethod
    def get_term_id(self, term: str) -> int:
        """
        Looks up the given term in the dictionary and returns the term's corresponding
        integer code. If the term is not present in the dictionary, -1 is returned.
        """
        pass


class InMemoryDictionary(Dictionary):
    """
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

    def size(self) -> int:
        return len(self._terms)

    def add_if_absent(self, term) -> int:
        term_id = self.get_term_id(term)
        if term_id < 0:
            term_id = self.size()
            self._terms[term] = term_id
        return term_id

    def get_term_id(self, term: str) -> int:
        return self._terms.get(term, -1)


def main():
    """
    Example usage. A tiny unit test, in a sense.
    """
    vocabulary = InMemoryDictionary()
    vocabulary.add_if_absent("foo")
    vocabulary.add_if_absent("bar")
    vocabulary.add_if_absent("foo")
    assert len(vocabulary) == 2
    assert vocabulary.size() == 2
    assert vocabulary.get_term_id("foo") == 0
    assert vocabulary.get_term_id("bar") == 1
    assert vocabulary["bar"] == 1
    assert vocabulary.get_term_id("wtf") == -1
    print(vocabulary)


if __name__ == "__main__":
    main()
