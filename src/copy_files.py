import os
import shutil

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