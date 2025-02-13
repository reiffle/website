import unittest

from copy_files import extract_title

class test_copy_files(unittest.TestCase):
    def test_extract_header(self):
        heading=extract_title("# Hello World")
        self.assertEqual(heading, "Hello World")

    def test_extract_header2(self):
        block="""
# This is a header

But This Isn't
"""
        heading=extract_title(block)
        self.assertEqual(heading, "This is a header")

    def test_extract_header3(self):
        block="""
This is a header

#       But This Isn't     
"""
        heading=extract_title(block)
        self.assertEqual(heading, "But This Isn't")
    
    def test_extract_header4(self):
        block="""
This is a header

#But This Isn't     
"""
        with self.assertRaises(ValueError):
            extract_header(block)