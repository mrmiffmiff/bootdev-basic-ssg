import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_title_extraction(self):
        md = """
# Hello

Thanks everyone
"""
        extracted = extract_title(md)
        self.assertEqual(extracted, "Hello")
    
    def test_no_title(self):
        md = """
weewooweewoo

weeweewoirfjweoifjewq
"""
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_strange_case(self):
        md = """
# Hello
more text

thanks
"""
        extracted = extract_title(md)
        self.assertEqual(extracted, "Hello")