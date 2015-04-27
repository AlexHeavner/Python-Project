from Tkinter import *
from vocabquiz import *

def buildNoteCard():
	global note_card_message
	global note_card_text
	note_card_text = StringVar()
	note_card_text.set("Select a File")
	note_card_message = Message( root, textvariable=note_card_text, relief=RAISED, width = 500, bg='lightgreen', font=('times', 24), padx=250, pady=150 )
	note_card_message.pack()
	buildEntry()
	buildButton()

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

def buildEntry():
	global entry
	entry = Entry(root, bd =5)
	entry.pack(side=BOTTOM)

def buildButton():
	global button
	button = Button(root, text="Submit")
	button.pack()
	button.bind('<Button-1>', getText)

def selectFile():
	global vocab_dictionary

	selection = var.get()
	file_selected_label.config(text = file_list[selection])
	file_selected = file_list[selection]

	file = openFile(file_selected)

	#load words from file into vocab dictionary
	vocab_dictionary = storeVocabWords(file)
	vocab_dictionary = getShuffledDictionary(vocab_dictionary)

	#Start at first card
	global index
	index = 0

	#Reset Score
	global points
	points = 0

	global english_list
	english_list = list(vocab_dictionary.keys())

	print english_list[index]
	note_card_text.set( english_list[index] )

def getText(event):
    global index
    global english_list

    user_input = entry.get()
    print user_input

    scoreInput(user_input, index)
    
    #clear entry box
    entry.delete(0, len(user_input))
    nextWord()

def nextWord():
	global index
	if index < len(english_list) - 1:
		index += 1
		note_card_text.set( english_list[index] )
	else:
		note_card_text.set( getScore() )

def scoreInput(user_input, index):
	global points
	global english_list
	global vocab_dictionary

	#test
	print user_input + ' == ' + vocab_dictionary[ english_list[index] ]

	if user_input == vocab_dictionary[ english_list[index] ]:
		points += 1
	else:
		print getScore()

def getScore():
	global points
	global vocab_dictionary

	score = (points/len(vocab_dictionary))*100

	return str(points) + '/' + str(len(vocab_dictionary)) + '\n{0:.0f}%'.format( ((1.0)*points/len(vocab_dictionary))*100 )

global root
global file_list
global vocab_dictionary
global english_list
global next_word
global index
global points

root = Tk()
var = IntVar()
file_list = getFileList()

buildLabelFileSelected()
buildRadioButtonsFileNames()
buildNoteCard()


root.mainloop()