from Tkinter import *
from vocabquiz import *

def selectFile():
	selection = var.get()
	file_selected_label.config(text = file_list[selection])
	file_selected = file_list[selection]

	file = openFile(file_selected)

	#load words from file into vocab dictionary
	vocab_dictionary = storeVocabWords(file)
	vocab_dictionary = getShuffledDictionary(vocab_dictionary)

	for i in vocab_dictionary:
		print i
		note_card_text.set(i)
		#note_card_message.pack()
		raw_input()
	root.mainloop()

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

def submitWord():
	print(entry.get())

def buildNoteCard():
	global note_card_message
	global note_card_text
	note_card_text = StringVar()
	note_card_text.set("Select a File")
	note_card_message = Message( root, textvariable=note_card_text, relief=RAISED, width = 500, bg='lightgreen', font=('times', 24), padx=250, pady=150 )
	note_card_message.pack()
	buildEntry()
	buildButton()

def buildEntry():
	global entry
	entry = Entry(root, bd =5)
	entry.pack(side=BOTTOM)

def buildButton():
	global button
	button = Button(root, text="Submit", command=submitWord)
	button.pack()

def listFileEntries(file_name):
	file = openFile(file_name)
	vocab_dictionary = storeVocabWords(file)
	vocab_dictionary = getShuffledDictionary(vocab_dictionary)

	note_card_window = Tk()
	
	for english in vocab_dictionary:
		msg = Message(note_card_window, text = english)
		msg.config(bg='lightgreen', font=('times', 24), borderwidth = 50)
		msg.pack()

global root
global file_list
global vocab_dictionary
global file_selected_flag

root = Tk()
var = IntVar()
file_list = getFileList()

buildLabelFileSelected()
buildRadioButtonsFileNames()
buildNoteCard()



root.mainloop()