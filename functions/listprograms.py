import subprocess
def winget_list():
    output = subprocess.run(["winget", "list", "--accept-source-agreements"], stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="replace", creationflags=subprocess.CREATE_NEW_CONSOLE) #run winget upgrade in the background
    lines = output.stdout.splitlines() #turn it into separate lines by rows
    print(f"turned output into separate lines: {lines}")
    ids = []
    names = []
    versions = []
    for i, line in enumerate(lines):
        print(f"enumerating line {i}: {line}")
        if "Name" in line and "Id" in line and "Version" in line: #find header
            headerline = i
            print(f"the line that the header is in is {headerline}")
        if headerline == i:
            header = lines[headerline] #grab header
            print(f"header grabbed: {header}")
            namestart = header.find("Name") 	#find at what character the name field starts at
            print(namestart)
            idstart = header.find("Id")			#same for id
            print(idstart)
            versionstart = header.find("Version")#same for version
            print(versionstart)
            for line in lines[headerline + 2:]: #skip all the nonsense decorative lines
                if not line.strip(): #stop after the app list
                    break
                if len(line) >= namestart:
                    app_name = line[namestart:idstart].strip() #grab the app name from the namestart character to the idstart character, and strip away the spaces at the end
                    print(f"found the following app name: {app_name}")
                    if app_name:
                        names.append(app_name) #add the app name to the
                    app_id = line[idstart:versionstart].strip()
                    print(f"found the following app id: {app_id}")
                    if app_id:
                          ids.append(app_id)
                        
    print(f"collected all the names: {names}")
    print(f"collected all ids: {ids}")
    name_id_dict = dict(zip(names, ids))
    print(name_id_dict)
    return(name_id_dict)