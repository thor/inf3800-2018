#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from abc import ABC, abstractmethod
from typing import List, Tuple


class Tokenizer(ABC):
    """
    Simple abstract base class for tokenizers, with some default implementations.
    """

    @abstractmethod
    def ranges(self, buffer: str) -> List[Tuple[int, int]]:
        pass

    def strings(self, buffer: str) -> List[str]:
        """
        Return the strings that make up the tokens in the given buffer.
        """
        return [buffer[r[0]:r[1]] for r in self.ranges(buffer)]

    def tokens(self, buffer: str) -> List[Tuple[str, Tuple[int, int]]]:
        """
        Returns the (string, range) pairs that make up the tokens in the given buffer.
        """
        return [(buffer[r[0]:r[1]], r) for r in self.ranges(buffer)]


class BrainDeadTokenizer(Tokenizer):
    """
    A dead simple tokenizer for testing purposes. A real tokenizer
    wouldn't be implemented this way. Kids, don't do this at home.
    """

    _pattern = re.compile("(\w+)", re.UNICODE | re.MULTILINE | re.DOTALL)

    def __init__(self):
        pass

    def ranges(self, buffer: str) -> List[Tuple[int, int]]:
        return [(m.start(), m.end()) for m in self._pattern.finditer(buffer)]


def main():
    """
    Example usage. A tiny unit test, in a sense.
    """
    tokenizer = BrainDeadTokenizer()
    buffer = "Dette  er en\nprøve!"
    strings = tokenizer.strings(buffer)
    print(strings)
    assert strings == ["Dette", "er", "en", "prøve"]
    tokens = tokenizer.tokens(buffer)
    print(tokens)


if __name__ == "__main__":
    main()
