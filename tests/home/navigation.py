import pytest
import unittest
from pages.home.navigation import Navigation


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class HomeTest(unittest.TestCase, Navigation):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.navigation = Navigation(self.driver)

    @pytest.mark.run(order=1)
    def test_Navigation(self):
        self.NavigationTest()
