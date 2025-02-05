import unittest
from extract_markdown import *

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_image(self):
        text1="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        mtext=extract_markdown_images(text1)

    def test_extract_links(self):
        text2="This is text with a [link](https://www.google.com) and [another link](https://www.youtube.com)"
        ltext=extract_markdown_links(text2)
        self.assertEqual(ltext, [('link', 'https://www.google.com'), ('another link', 'https://www.youtube.com')])
