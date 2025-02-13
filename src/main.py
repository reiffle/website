from copy_files import copy_from_source_to_target, generate_page
def main():
    home_dir="/home/pederreiff/workspace/github.com/reiffle/website"
    copy_from_source_to_target()
    generate_page(f"{home_dir}/content/index.md", f"{home_dir}/template.html", f"{home_dir}/public/")





main()
