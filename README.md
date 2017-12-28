# Introduction

There are five obligatory assignments in INF3800 and INF4800. The assignments are a mix of pen-and-paper exercises and coding exercises. This document and this repository concerns the coding exercises.

The coding assignments assume basic familiarity with the Python language. At least version 3.6 will be assumed. If you are on an older version of Python you’re on your own, and you might have to backport code. You can use whatever development environment you want, but you will probably be more productive and have an easier time if you use a good IDE. We can recommend [PyCharm](https://www.jetbrains.com/pycharm/). You can use another set of tools if you want, but then don't expect help with solving challenges related to setup or tooling.

You will be provided with some "precode" or "starter code", i.e., a set of helper classes and functions that you can make use of so that you don't have to start the coding assignments completely from scratch. This precode also sets some structure on how you implement the assignments. Please familiarize yourself with what's available. The precode is commented and has some illustrative usage examples.

Common for the precode is that `NotImplementedError` is raised in places where you are meant to provide a working implementation. After having provided working implementations, the following should work and run without errors:

    >python3 assignments.py

The above invocation runs all tests for all assignments. If you want to only run the tests for, say, assignments A and C, you can pass this as command line arguments:

    >python3 assignments.py a c

Making tests pass for one assignment should not result in tests breaking for previous assignments.

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

Expected output:

```
>python3 assignments.py a
*** ASSIGNMENT A ***
prøve
{'document_id': 1, 'term_frequency': 1}
wtf
test
{'document_id': 0, 'term_frequency': 1}
{'document_id': 1, 'term_frequency': 2}
{'this': [{'document_id': 0, 'term_frequency': 1}], 'is': [{'document_id': 0, 'term_frequency': 1}], 'a': [{'document_id': 0, 'term_frequency': 1}], 'test': [{'document_id': 0, 'term_frequency': 1}, {'document_id': 1, 'term_frequency': 2}], 'prøve': [{'document_id': 1, 'term_frequency': 1}]}
hydrogen
{'document_id': 11634, 'term_frequency': 1}
{'document_id': 11635, 'term_frequency': 1}
{'document_id': 11636, 'term_frequency': 1}
{'document_id': 11637, 'term_frequency': 1}
{'document_id': 11638, 'term_frequency': 1}
{'document_id': 11639, 'term_frequency': 1}
{'document_id': 19011, 'term_frequency': 1}
{'document_id': 22229, 'term_frequency': 1}
hydrocephalus
{'document_id': 11622, 'term_frequency': 1}
{'document_id': 11623, 'term_frequency': 1}
HIV AND pROtein
{'document_id': 11316, 'fields': {'body': 'hiv core protein p24', 'meta': '20'}}
{'document_id': 11319, 'fields': {'body': 'hiv envelope protein gp120', 'meta': '26'}}
{'document_id': 11320, 'fields': {'body': 'hiv envelope protein gp160', 'meta': '26'}}
{'document_id': 11321, 'fields': {'body': 'hiv envelope protein gp41', 'meta': '25'}}
water OR Toxic
{'document_id': 3078, 'fields': {'body': 'body water', 'meta': '10'}}
{'document_id': 8138, 'fields': {'body': 'epidermal necrolysis, toxic', 'meta': '27'}}
{'document_id': 8635, 'fields': {'body': 'extravascular lung water', 'meta': '24'}}
{'document_id': 9379, 'fields': {'body': 'fresh water', 'meta': '11'}}
{'document_id': 14472, 'fields': {'body': 'megacolon, toxic', 'meta': '16'}}
{'document_id': 18572, 'fields': {'body': 'plants, toxic', 'meta': '13'}}
{'document_id': 23234, 'fields': {'body': 'tar-water', 'meta': '9'}}
{'document_id': 23985, 'fields': {'body': 'toxic actions', 'meta': '13'}}
{'document_id': 25265, 'fields': {'body': 'water', 'meta': '5'}}
{'document_id': 25266, 'fields': {'body': 'water deprivation', 'meta': '17'}}
{'document_id': 25267, 'fields': {'body': 'water intoxication', 'meta': '18'}}
{'document_id': 25268, 'fields': {'body': 'water loss, insensible', 'meta': '22'}}
{'document_id': 25269, 'fields': {'body': 'water microbiology', 'meta': '18'}}
{'document_id': 25270, 'fields': {'body': 'water movements', 'meta': '15'}}
{'document_id': 25271, 'fields': {'body': 'water pollutants', 'meta': '16'}}
{'document_id': 25272, 'fields': {'body': 'water pollutants, chemical', 'meta': '26'}}
{'document_id': 25273, 'fields': {'body': 'water pollutants, radioactive', 'meta': '29'}}
{'document_id': 25274, 'fields': {'body': 'water pollution', 'meta': '15'}}
{'document_id': 25275, 'fields': {'body': 'water pollution, chemical', 'meta': '25'}}
{'document_id': 25276, 'fields': {'body': 'water pollution, radioactive', 'meta': '28'}}
{'document_id': 25277, 'fields': {'body': 'water purification', 'meta': '18'}}
{'document_id': 25278, 'fields': {'body': 'water softening', 'meta': '15'}}
{'document_id': 25279, 'fields': {'body': 'water supply', 'meta': '12'}}
{'document_id': 25280, 'fields': {'body': 'water-electrolyte balance', 'meta': '25'}}
{'document_id': 25281, 'fields': {'body': 'water-electrolyte imbalance', 'meta': '27'}}
*************************
*** ALL TESTS PASSED! ***
*************************
```

