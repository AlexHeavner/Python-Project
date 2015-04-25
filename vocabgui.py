from vocabquiz import *
from Tkinter import *

def selectFile():
	selection = var.get()
	file_selected_label.config(text = file_list[selection])

def buildLabelFileSelected():
	global file_selected_label
	file_selected_label = Label(root)
	file_selected_label.pack()

def buildRadioButtonsFileNames():
	if file_list:
		count = 0
		for file_name in file_list:
			Radiobutton(
				root, text=file_name,
				padx = 20,
				variable = var,
				value = count, 
				command = selectFile).pack(anchor=W)
			count+=1
	else:
		Label(
			root, "No Files found.", 
			justify = LEFT, 
			padx = 20).pack()



root = Tk()
var = IntVar()
file_list = getFileList()

buildLabelFileSelected()
buildRadioButtonsFileNames()


root.mainloop()