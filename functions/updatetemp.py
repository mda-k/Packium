import subprocess
def winget_update():
    output = subprocess.run(
        ["winget", "upgrade"],
        capture_output=True,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
    updateinfo = output.stdout
    lines = output.stdout.splitlines()
    print(updateinfo)
    print(lines)
    ids = []
    header_idx = -1 				#index of the header, line where the headers sit (name, version, blah blah)
    for i, line in enumerate(lines):	#enumerate the lines, get the index of the lines and the text too
        print(line)
        if "Name" in line and "Id" in line and "Version" in line: #rest is self explanatory i think
            header_idx = i
            break
    if header_idx != -1: #if it found the top headers line
        header = lines[header_idx] #save header line into a variable
        print(header)
        name_start = header.find("Name")
        print(name_start)
        id_start = header.find("Id") #find the id in the header
        print(id_start)
        version_start = header.find("Version") #version field
        print(version_start)
        for line in lines[header_idx + 2:]: #skip the ---------
            if not line.strip() or "upgrades available" in line or "package(s)" in line: #safety
                break
            if len(line) >= id_start:
                app_idr = line[id_start:version_start].strip() #grab everything from the line
                app_id = app_idr.strip()
                print(app_idr)
                print(app_id)
                if app_id:
                    ids.append(app_id)
    print(f"found the following ids: {ids}")
    return ids