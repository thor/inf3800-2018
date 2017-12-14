#!/usr/bin/python
# -*- coding: utf-8 -*-

from dictionary import InMemoryDictionary
from collections import Counter

class Posting:
    """
    A very simple posting entry in a non-positional inverted index.
    """

    def __init__(self, document_id, term_frequency):
        self.document_id = document_id
        self.term_frequency = term_frequency

    def __repr__(self):
        return str({"document_id": self.document_id, "term_frequency": self.term_frequency})

class InMemoryInvertedIndex:
    """
    A simple in-memory implementation of an inverted index, suitable for small corpora.

    In a serious application we'd have configuration to allow for field-specific NLP,
    scale beyond current memory constraints, have a positional index, and so on.
    """

    def __init__(self, corpus, fields, normalizer, tokenizer):
        self._corpus = corpus
        self._normalizer = normalizer
        self._tokenizer = tokenizer
        self._posting_lists = []
        self._dictionary = InMemoryDictionary()
        self._build_index(fields)

    def __repr__(self):
        return str({term: self._posting_lists[term_id] for (term, term_id) in self._dictionary})

    def _build_index(self, fields):
        """
        Builds a simple inverted index from the named fields in the document
        collection. The dictionary implementation is assumed to produce term
        identifiers in the range {0, ..., N - 1}.
        """
        raise NotImplementedError

    def get_terms(self, buffer):
        """
        Processes the given text buffer and returns the sequence of normalized
        terms as they are indexed. Both query strings and documents need to be
        identically processed.
        """
        return [self._normalizer.normalize(t) for t in self._tokenizer.strings(self._normalizer.canonicalize(buffer))]

    def get_postings_iterator(self, term):
        """
        Returns an iterator that can be used to iterate over the term's associated
        posting list. For out-of-vocabulary terms we associate empty posting lists.

        In a serious application a postings list would be stored as a contiguous buffer
        storing compressed integers, and the iterator would facilitate loading this buffer
        from somewhere and decompressing the integers.
        """
        term_id = self._dictionary.get_term_id(term)
        if term_id < 0:
            return iter([])
        return iter(self._posting_lists[term_id])

    def get_document_frequency(self, term):
        """
        Returns the number of documents in the indexed corpus that contains the given term.
        """

        # In a serious application we'd store this number explicitly, e.g., as part of the dictionary.
        # That way, we can look up the document frequency without having to access the posting lists
        # themselves. Imagine if the posting lists don't even reside in memory!
        term_id = self._dictionary.get_term_id(term)
        if term_id < 0:
            return 0
        return len(self._posting_lists[term_id])


