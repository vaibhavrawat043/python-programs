def group_by_owners(files):
    output = {}
    for fileName, fileOwner in files.items():
        output[fileOwner] = output.get(fileOwner, []) + [fileName] 
    return output

files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 

print(group_by_owners(files))
