from tkinter import *
from functions import*


root = Tk()
v = IntVar()

file_list = avaliableLibraries()

if file_list:
	for file_path in file_list:
		Radiobutton(root, 
            		text=file_path,
            		padx = 20, 
            		variable=v, 
            		value=1).pack(anchor=W)
else:
	Label(root, 
      	text="""No libraries found.""",
      	justify = LEFT,
      	padx = 20).pack()

root.mainloop()
