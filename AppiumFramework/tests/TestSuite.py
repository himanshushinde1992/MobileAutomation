# 1. Import the files
import unittest

# 2. Create the object of the class using unitTest
from AppiumFramework.tests.test_ap_login import test_user_login

cf = unittest.TestLoader().loadTestsFromTestCase(test_user_login)

# 3. Create TestSuite
regressionTest = unittest.TestSuite([cf])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=2).run(regressionTest)
