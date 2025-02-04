import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.ign.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://www.ign.com")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, "http://www.ign.com")
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node too", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("b", "This is a text node"))

    def test_text_node_to_html_node2(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("i", "This is a text node"))

    def test_text_node_to_html_node3(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("code", "This is a text node"))

    def test_text_node_to_html_node4(self):
        node = TextNode("This is a text node", TextType.LINK, "http://www.ign.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("a", "This is a text node", {"href": "http://www.ign.com"}))

    def test_text_node_to_html_node5(self):
        node = TextNode("This is a text node", TextType.IMAGE, "http://www.ign.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("img", None, {"src": "http://www.ign.com", "alt": "This is a text node"}))
        
    def test_text_node_to_html_node6(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode(None, "This is a text node"))