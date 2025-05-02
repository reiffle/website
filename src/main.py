import sys
from copy_files import copy_from_source_to_target, generate_page, generate_pages_recursive
def main():
    if len(sys.argv)==0:
        basepath = "/"
    else: basepath = sys.argv[0]
    home_dir="/home/pederreiff/workspace/github.com/reiffle/website"
    copy_from_source_to_target()
    #generate_page(f"{home_dir}/content", f"{home_dir}/template.html", f"{home_dir}/public/", "index.md")
    generate_pages_recursive(basepath, f"{home_dir}/content", f"{home_dir}/template.html", f"{home_dir}/public/")





main()
