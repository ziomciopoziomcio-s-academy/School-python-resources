import requests
list_url = "https://raw.githubusercontent.com/ziomciopoziomcio-s-academy/School-python-resources/Launcher/launcher/programs.txt"
local = "lts.txt"
r = requests.get(list_url)
with open(local, 'wb')as file:
    file.write(r.content)


