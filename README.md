# Introduction

There are five obligatory assignments in INF3800 and INF4800. The assignments are a mix of pen-and-paper exercises and coding exercises. This document and this repository concerns the coding exercises.

The coding assignments assume basic familiarity with the Python language. At least version 3.6 will be assumed. If you are on an older version of Python you’re on your own, and you might have to backport code. You can use whatever development environment you want, but you will probably be more productive and have an easier time if you use a good IDE. We can recommend [PyCharm](https://www.jetbrains.com/pycharm/). You can use another set of tools if you want, but then don't expect help with solving challenges related to setup or tooling.

You will be provided with some "precode" or "starter code", i.e., a set of helper classes and functions that you can make use of so that you don't have to start the coding assignments completely from scratch. This precode also sets some structure on how you implement the assignments. Please familiarize yourself with what's available. The precode is commented and has some illustrative usage examples.

Common for the precode is that `NotImplementedError` is raised in places where you are meant to provide a working implementation. After having provided working implementations, the following should work and run without errors:

    >python3 assignments.py

The above invocation runs all tests for all assignments. If you want to only run the tests for, say, assignments A and C, you can pass this as command line arguments:

    >python3 assignments.py a c

If your code raises no exceptions and passes all the `assert` statements, you should see the following printed to the console:

    *************************
    *** ALL TESTS PASSED! ***
    *************************

All your implementations should be reasonably efficient. Please strive to create readable and modular code.

If your code is very slow and you want to measure where the time is spent, you can use the built-in `cProfile` module to do this:

    >python3 –m cProfile assignments.py

Output from `cProfile` can be visualized using, e.g., [SnakeViz](https://jiffyclub.github.io/snakeviz/).

# Assignment A

The purpose of this assignment is to build a simple in-memory inverted index and show how to merge posting lists.

Implementation notes:

* The `InMemoryInvertedIndex` class implements a simple inverted index. We create an inverted index from a corpus (i.e., a collection of documents) as represented by the `InMemoryCorpus` class.
* After having indexed the corpus (or at least a specified set of fields in the documents) and created an `InMemoryInvertedIndex` object, we will have created a dictionary of indexed terms as represented by the `InMemoryDictionary` class, and a posting list for each term. Each posting in a posting list should keep track of the document identifier and the number of times the term occurs in the identified document. The resulting posting lists must be sorted in ascending order by document identifiers.
* For text normalization and tokenization purposes, you can use the `BrainDeadNormalizer` and `BrainDeadTokenizer` classes.
* You might find the `Counter` class in the built-in `collections` module useful.

Your task is to:

* Familiarize yourself with the precode.
* Implement the missing indexing code in the `InMemoryInvertedIndex` class.
* Implement the missing code for merging two posting lists in the `PostingsMerger` class.
* Make all tests pass.

Some optional bonus challenges for the interested student:

* Above you implemented the `AND` and `OR` operators over posting lists. Extend this to also implement the `ANDNOT` operator.
* The implementations for the `AND` and `OR` operators take two posting lists as arguments. Can you generalize your implementations to be _n_-ary instead of binary, i.e., how would you efficiently traverse _n_ posting lists in "parallel"?
* Extend your posting list implementation to include skip lists, extend your indexing code to build these, and extend your merging code to make good use of this additional data structure.

