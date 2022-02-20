import requests
list_url = "https://raw.githubusercontent.com/ziomciopoziomcio-s-academy/School-python-resources/Launcher/launcher/programs.txt"
local_prg = "lts_prg.txt"
r = requests.get(list_url)
with open(local_prg, 'wb') as file:
    file.write(r.content)
    file.close()

def programs_list():
    list = []
    with open(local_prg, 'r') as file:
        for line in file:
            line = line.strip()
            list.append(line)
    return list
