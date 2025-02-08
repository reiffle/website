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
