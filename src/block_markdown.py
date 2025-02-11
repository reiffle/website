from htmlnode import ParentNode #don't need leaf
from inline_markdown import text_to_textnodes #take raw text and turn it into text, bold, italic, code, url, and image
from textnode import text_node_to_html_node #take text nodes and convert into inline html node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):

    block_holder=markdown.split("\n\n")
    culled_list=[]
    for row in block_holder:
        if row == "":
            continue
        row=row.strip()
        if row!="":
            culled_list.append(row)
    return culled_list

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown) #Type of block (paragraph, inline, etc)
    children = [] #Need a list for parentnode children
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

        

def block_to_html_node (block): #convert block text to htmlnode
        block_type=block_to_block_type(block) #Get type of block
        if block_type==block_type_paragraph:
            return paragraph_to_html_node(block)
        elif block_type==block_type_heading:
            return heading_to_html_node(block)
        elif block_type==block_type_code:
            return code_to_html_node(block)
        elif block_type==block_type_quote:
            return quote_to_html_node(block)
        elif block_type==block_type_ulist:
            return ulist_to_html_node(block)
        elif block_type==block_type_olist:
            return olist_to_html_node(block)
        else:
            raise ValueError ("Invalid block type")
        
def text_to_children(text):
    text_nodes=text_to_textnodes(text) #Split text into individual nodes of text, bold, image, etc
    children = [] #Need to return a list of nodes
    for text_node in text_nodes:
        html_node=text_node_to_html_node(text_node) #Creating inline code to be put between block markings
        children.append(html_node) #Put together everything that is going to go between block markings
    return children #Return all of the marked-up text in html format

def paragraph_to_html_node(block):
    lines=block.split("\n")
    paragraph=" ".join(lines)
    children=text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == '#':
            level+=1
        else:
            break
    if level +1 >= len(block):
        raise ValueError (f"invalid heading level: {level}")
    text=block[level+1:] #This is where the preceeding characters are stripped out
    children=text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or block.endswith("```"):
        raise ValueError ("invalid code block")
    text=block[4:-3] #Strip extra characters
    children = text_to_children(text)
    code=ParentNode("code", children)
    return ParentNode ("pre", [code]) #why is "code" a list?

def olist_to_html_node(block):
    items=block.split("\n")
    html_items=[]
    for item in items:
        text = item[3:] #This assume the ordered list is only one digit long
        children=text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_html_node(block):
    items=block.split("\n")
    html_items=[]
    for item in items:
        text= item[2:]
        children=text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_node(block):
    lines=block.split("\n")
    new_lines=[]
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip()) #Is this stripping the > and blank space?
    content = " ". join(new_lines)
    children=text_to_children(content)
    return ParentNode("blockquote", children)
            
        