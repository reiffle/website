from textnode import *
from extract_markdown import *

t_type=TextType.BOLD
def main():
    test_node= TextNode("My Name Is Lucca", t_type, "http://www.wtf.com")
    print (test_node)


main()
