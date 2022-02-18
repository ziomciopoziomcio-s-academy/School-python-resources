import requests
list_url = "https://raw.githubusercontent.com/ziomciopoziomcio-s-academy/School-python-resources/Launcher/launcher/programs.txt"
local = "lts.txt"
r = requests.get(list_url)
with open(local, 'wb') as file:
    file.write(r.content)
    file.close()

def programs_list():
    list = []
    with open(local, 'r') as file:
        for line in file:
            line = line.strip()
            list.append(line)
    return list

test = programs_list()