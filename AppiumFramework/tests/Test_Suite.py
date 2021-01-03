# 1. Import the files
import unittest

from AppiumFramework.tests import Selection_form
from AppiumFramework.tests.Selection_form import selection_form
from AppiumFramework.tests import product

# 2. Create the object of the class using unitTest
sf = unittest.TestLoader().loadTestsFromTestCase(Selection_form)
pp = unittest.TestLoader().loadTestsFromTestCase(product)

#  3. Create TestSuite
regressionTest = unittest.TestSuite([sf, pp])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)