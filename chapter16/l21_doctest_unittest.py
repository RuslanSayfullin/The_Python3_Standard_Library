import doctest
import unittest

import l1_doctest_simple

suite = unittest.TestSuite()
suite.addTest(doctest.DocTestSuite(l1_doctest_simple))
suite.addTest(doctest.DocFileSuite('doctest_in_help.txt'))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
