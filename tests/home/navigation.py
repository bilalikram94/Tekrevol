import pytest
import unittest
from pages.home.navigation import Navigation


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class NavigationTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.nav = Navigation(self.driver)

    @pytest.mark.run(order=1)
    def test_Navigation(self):
        self.nav.NavigationTest()
