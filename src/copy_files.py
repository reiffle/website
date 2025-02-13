import os
import shutil

from block_markdown import markdown_to_blocks
from block_markdown import markdown_to_html_node

def copy_from_source_to_target(source="/home/pederreiff/workspace/github.com/reiffle/website/static", target="/home/pederreiff/workspace/github.com/reiffle/website/public"):
    #check if source and target exist
    if not os.path.exists(source):
        raise Exception (f"The source path: {source} does not exist")
    if os.path.exists(target):#if target exists, delete contents
        shutil.rmtree(target)
    os.mkdir(target) #if target does not exist, create it
    content_tree=os.listdir(source)#copy contents from source to target
    for content in content_tree:
        source_file=f"{source}/{content}"
        dest_file= f"{target}/{content}"
        if os.path.isfile(source_file):
            shutil.copy(source_file, dest_file)
        else:
            copy_from_source_to_target(source_file, dest_file)

def extract_title(markdown):
    markdown_list=markdown_to_blocks(markdown)
    for line in markdown_list:
        if not line.startswith("# "):
            continue
        else:
            return line.lstrip("# ").strip()
    raise ValueError ("No H1 heading present")

def generate_page(from_path, template_path, dest_path):
    if not os.path.exists(from_path):
        raise ValueError("Source directory does not exist")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    file=open(from_path, "r") #Have to open before you can read
    markdown_content=file.read()
    file.close() #Must close file after done
    file=open(template_path, "r")
    template_content=file.read()
    file.close()
    html_node=markdown_to_html_node(markdown_content) #This might need to be split up
    print ("Node Created")
    html_string=html_node.to_html()
    print ("Extracting title")
    title = extract_title(markdown_content)
    print ("Replacing template content with title and html string")
    template_content=template_content.replace("{{ Title }}", title)
    template_content=template_content.replace("{{ Content }}", html_string)
    os.makedirs(dest_path, exist_ok=True) #Make sure destination path exists or create it of it doesn't
    filepath=f"{dest_path}/index.html"
    with open(filepath, "w") as file:
        file.write(template_content)


