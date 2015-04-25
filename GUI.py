rom tkinter import *
from functions import*

class GUI:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		choice = IntVar()
		choice.set(1)

		file_list = avaliableLibraries()

		count = 1
		if file_list:
			for file_path in file_list:
				Radiobutton(root, 
            				text=file_path,
            				padx = 20, 
            				variable=choice, 
            				value=count).pack(anchor=W)
				count += 1

			button = Button(root, text='Select', width=25, command=selectAction)
			button.pack()


		else:
			Label(root, 
      			text="""No libraries found.""",
      			justify = LEFT,
      			padx = 20).pack()


	def selectAction():
		print(choice.get())

root = Tk()
gui = GUI(root)
root.mainloop()
