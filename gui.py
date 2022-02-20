#Initial configuration
from appJar import gui
app = gui()
from Launcher.updater import *
version = "0.0.1 PA"
update()

#Update
available_programs = programs_list()
lts_ver = version_check()
print(lts_ver)
app.startSubWindow("Update available!")
app.addLabel("l1", "Your program version:")
app.addLabel("l2", version)
app.addLabel("l3", "Latest version of the program:")
app.addLabel("l4", lts_ver)
app.addLabel("l5", "Update your program {{here}}") #TO DO
app.stopSubWindow()
if version != lts_ver:
    app.showSubWindow("Update available!")

#Title
app.addLabel("title", "Welcome in the School Python Resources")

#Buttons definition
def press(btn):
    if btn == "Delta":
        print("Delta")
    else:
        pass #TO DO
#Buttons GUI
app.startLabelFrame("Available programs")

for x in available_programs:
    app.addButton(x, press)
app.stopLabelFrame()

#App start
app.go()