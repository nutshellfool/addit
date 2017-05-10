from unittest import TestCase
import addit.addit as addit


class TestAddIt(TestCase):
    def test_get_file_url(self):
        url = addit.get_file_url('java')
        self.assertIsNone(url)
