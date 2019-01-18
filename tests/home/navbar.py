import pytest
import unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData
from pages.home.navbar import NavBar


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class HomeTest(unittest.TestCase, NavBar):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hom = NavBar(self.driver)

    @pytest.mark.run(order=1)
    def test_NavBar(self):
        self.hom.verifyNavBar()

    @pytest.mark.run(order=2)
    @data(*getCVSData("D:\\tekrevol\\tests\\home\\textNavBar"))
    @unpack
    def test_TextNavbar(self, _text_home, _text_about, _text_portfolio, _text_contact_us, _text_services,
                        _text_get_a_quote):
        self.hom.verifyTextNavBar(_text_home, _text_about, _text_portfolio, _text_contact_us, _text_services,
                                  _text_get_a_quote)
