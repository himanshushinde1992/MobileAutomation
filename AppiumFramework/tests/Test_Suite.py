# 1. Import the files
import unittest

from AppiumFramework.tests.product import product_page_Test

# 2. Create the object of the class using unitTest

pp = unittest.TestLoader().loadTestsFromTestCase(product_page_Test)

#  3. Create TestSuite
smokeTest = unittest.TestSuite([pp])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(smokeTest)