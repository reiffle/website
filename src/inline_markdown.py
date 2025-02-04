from textnode import TextNode, TextType

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
  
