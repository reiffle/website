class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props==None:
            return ""
        starter=""
        for value in self.props:
            starter+=f' {value}="{self.props[value]}"'
        return starter
    
    def __eq__(self, other_node):
        return (
            isinstance(other_node, HTMLNode)
            and self.tag==other_node.tag
            and self.value==other_node.value
            and self.children==other_node.children
            and self.props==other_node.props
            )
    
    def __repr__(self):
        return f"HTMLNode:({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None): #tag is the property (paragraph, bold, etc), value is the text inside it
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value==None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag==None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode:({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None): #tag is the property (paragraph, bold, etc), children is a LIST!!! of HTMLNodes
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag==None:
            raise ValueError("All parent nodes must have a tag")
        if self.children==None:
            raise ValueError("All parent nodes must have children")
        children="".join(child.to_html()for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>" #This returns the actual html code of the markdown file


    def __repr__(self):
        return f"ParentNode:({self.tag}, children: {self.children}, {self.props})"
    