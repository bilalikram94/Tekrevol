import pytest
import unittest
from ddt import ddt, data, unpack
from pages.home.aboutus import AboutUs


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AboutUsTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.about = AboutUs(self.driver)

    @pytest.mark.run(order=1)
    def test_AboutUs(self):
        self.about.AboutUsAll()
