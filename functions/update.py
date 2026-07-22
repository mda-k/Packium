import subprocess
def winget_update():
    output = subprocess.run(["winget", "upgrade"], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW) #run winget upgrade in the background
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
                if not line.strip() or "upgrades available" in line: #stop after the app list
                    break
                if len(line) >= namestart:
                    app_name = line [namestart:idstart].strip() #grab the app name from the namestart character to the idstart character, and strip away the spaces at the end
                    print(f"found the following app name: {app_name}")
                    if app_name:
                        names.append(app_name) #add the app name to the list
    print(f"collected all the names: {names}")
    return(names)
                