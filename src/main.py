from copy_files import copy_from_source_to_target, generate_page, generate_pages_recursive
def main():
    home_dir="/home/pederreiff/workspace/github.com/reiffle/website"
    copy_from_source_to_target()
    #generate_page(f"{home_dir}/content", f"{home_dir}/template.html", f"{home_dir}/public/", "index.md")
    generate_pages_recursive(f"{home_dir}/content", f"{home_dir}/template.html", f"{home_dir}/public/")





main()
