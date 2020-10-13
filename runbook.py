#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pylint: disable=too-few-public-methods, invalid-name, missing-docstring

"""
runbook library - runs a "do nothing" script

Inspired by:
https://blog.danslimmon.com/2019/07/15/do-nothing-scripting-the-key-to-gradual-automation/

Rewritten from the original version to avoid the need for callers to to subclass and pass
a module filename, and also to avoid the need to parse the calling module using regex.

This new version accepts a class name (e.g., MyRunBook) and uses inspect.getmembers() to
identify the class methods to run.

Note: To get the class methods to run in the order given, the list of methods from
inspect.getmembers() must be sorted by source file line number because class members
are held by Python in a dict, which does not guarantee sort order.

This library can be invoked with either
    RunBook.run(MyRunBook)
or
    RunBook(MyRunBook)

September 2019
"""

import inspect


class RunBook:
    def __init__(self, runbook_class):
        RunBook.run(runbook_class)

    @staticmethod
    def run(runbook_class):
        rb = runbook_class()
        methods = [(name, method) for name, method in inspect.getmembers(rb, inspect.ismethod)]
        # sort by source code line number
        for method in sorted(methods, key=lambda item: item[1].__code__.co_firstlineno):
            getattr(runbook_class, method[0])(rb)
            input("Press Enter to continue: ")

        print("Finished.")
