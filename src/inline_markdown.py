from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]
    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes=[]
        sections=node.text.split(delimiter) #split text with delimiter
        if len(sections)%2==0:#Delimiter only closed if odd number of sections
            raise ValueError(f"Delimiter {delimiter} is not closed")
        for i in range (len(sections)):
            if sections[i]=="":#Don't add empty string
                continue
            if i%2==0:#By def, split delimiter is odd, so this is plain text
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else: #This is delimited text
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
  
def split_nodes_image(old_nodes):
    new_nodes=[]
    for old_node in old_nodes:
        if old_node.text_type!=TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images=extract_markdown_images(old_node.text) #Get the exact image text and link
        original_text=old_node.text
        if len(images)==0: #Just add text if no image present
            new_nodes.append(old_node)
            continue
        for image in images:
            sections=original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections)!=2:
                raise ValueError("invalid markdown, image section not closed") #split text with delimiter
            if sections[0]!="":
                new_nodes.append(TextNode(sections[0], TextType.TEXT)) #Add the text before the image. must explicity add TextType.TEXT
            new_nodes.append( #Add the image - This part was where I got stuck
                TextNode(
                    image[0],
                    TextType.IMAGE, #I needed to explicitly state this part
                    image[1],
                ) 
            )
            original_text=sections[1] #Add the text after the image
        if original_text !="":
            new_nodes.append(TextNode(original_text, TextType.TEXT)) #Add final text
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):

    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
