#import the libs
from tkinter import *
from tkinter import ttk

#all the command functions to make them run
def calculate(*args):
    print("This is a command!")

#setup the window
root = Tk()
root.title("Feet to Meters")

#define the windows parameters
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, E, S, W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

#define the buttons and the layout
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#setup the padding
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

#close the ui
root.mainloop()



#########################################################################################################
#   A command to remember!																				#
#   root.destroy() - a function that can close the tk window with the name "root"						#
#																										#
#																										#
#   Something you should know.....																		#
#   HINT, to make a new window, on a new line type: newWindowRoot = TopLevel()  to make a new window!	#
#########################################################################################################
