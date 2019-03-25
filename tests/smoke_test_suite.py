import unittest
from tests.home.navbar import HomeTest
from tests.home.navigation import NavigationTest
from tests.home.aboutus import AboutUsTest
from tests.contactus.contactus import ContactTest

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(HomeTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(NavigationTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(AboutUsTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(ContactTest)


# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4])

unittest.TextTestRunner(verbosity=2).run(smokeTest)