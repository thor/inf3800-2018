#!/usr/bin/python
# -*- coding: utf-8 -*-

class BrainDeadNormalizer:
    """
    A dead simple normalizer for simple testing purposes.
    """

    def __init__(self):
        pass

    def canonicalize(self, buffer):
        """
        Normalizes a larger text buffer, so that downstream NLP can assume some kind of
        standardized text representation.

        In a serious application we might normalize the encoding and do Unicode canonicalization
        here, and perhaps nothing else.
        """
        return buffer

    def normalize(self, token):
        """
        Normalizes a token to produce an actual index term.

        In a serious application we might do transliteration, accent removal, lemmatization or
        stemming, or other stuff here, in addition to simple case folding.
        """
        return token.lower()

if __name__ == "__main__":
    normalizer = BrainDeadNormalizer()
    buffer = "Dette ER en\nprØve!"
    print(normalizer.canonicalize(buffer))
    token = "grØnnFustaSJEOpphengsForKOBling"
    print(normalizer.normalize(token))
    assert normalizer.normalize(token) == "grønnfustasjeopphengsforkobling"
