#!/usr/bin/env python

import unittest
import perl

class TestPyPerlEval(unittest.TestCase):

    def test_eval(self):
        # FIXME:
        self.assertIsNone(perl.eval("""
Python::exec("
print 'ok 1'
n = 4
");

Python::eval("n/2"))
"""), 4);


def test_main():
    from test import test_support
    test_support.run_unittest(TestPyPerlEval)

if __name__ == "__main__":
    test_main()
