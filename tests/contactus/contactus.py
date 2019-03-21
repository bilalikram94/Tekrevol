import pytest
import unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData
from pages.ContactUs.contact_us import ContactUs


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class ContactTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.con = ContactUs(self.driver)

    @pytest.mark.run(order=1)
    def test_ContactSmoke(self):
        self.con.ContactSmoke()

    @pytest.mark.run(order=2)
    @data(*getCVSData("D:\\GitHub\\tekrevol\\Tekrevol\\tests\\contactus\\contactus.csv"))
    @unpack
    def test_ContactUs(self, name, designation, email, company, number, value):
        self.con.ContactTest(name, designation, email, company, number, value)
