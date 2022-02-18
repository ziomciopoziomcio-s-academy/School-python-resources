#Initial configuration
from appJar import gui
app = gui()
from Launcher.updater import *

#Available programs list creation
available_programs = programs_list()

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