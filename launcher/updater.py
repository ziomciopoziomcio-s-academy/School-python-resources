import requests
list_url = "https://raw.githubusercontent.com/ziomciopoziomcio-s-academy/School-python-resources/Launcher/launcher/programs.txt"
local_prg = "lts_prg.txt"
ver_list = "https://raw.githubusercontent.com/ziomciopoziomcio-s-academy/School-python-resources/Launcher/launcher/version.txt"
local_ver = "lts_ver.txt"
l = requests.get(list_url)
v = requests.get(ver_list)
def update():
    with open(local_prg, 'wb') as file:
        file.write(l.content)
        file.close()
    with open(local_ver, 'wb') as file:
        file.write(v.content)
        file.close()

def programs_list():
    update()
    list = []
    with open(local_prg, 'r') as file:
        for line in file:
            line = line.strip()
            list.append(line)
    return list

def version_check():
    update()
    with open(local_ver, 'r') as file:
        ver = file.read().strip()
    return ver