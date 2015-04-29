from Tkinter import *
from vocabquiz import *

class VocabGui:

	global root
	global file_list
	global vocab_dictionary
	global english_list
	global next_word
	global index
	global points

	def __init__(self):
		global root
		global file_list
		global vocab_dictionary
		global english_list
		global next_word
		global index
		global points

		self.root = Tk()
		self.var = IntVar()
		self.file_list = getFileList()

		self.buildLabelFileSelected()
		self.buildRadioButtonsFileNames()
		self.buildNoteCard()


		self.root.mainloop()

	def buildLabelFileSelected(self):
		global file_selected_label
		self.file_selected_label = Label(self.root)
		self.file_selected_label.pack()

	def buildNoteCard(self):
		global note_card_message
		global note_card_text
		self.note_card_text = StringVar()
		self.note_card_text.set("Select a File")
		self.note_card_message = Message( self.root, textvariable=self.note_card_text, relief=RAISED, width = 500, bg='lightgreen', font=('times', 24), padx=250, pady=150 )
		self.note_card_message.pack()
		self.buildEntry()
		self.buildButtonSave()
		self.buildButtonSkip()
		self.buildButtonSubmit()

	def buildRadioButtonsFileNames(self):
		if self.file_list:
			count = 0
			for file_name in self.file_list:
				Radiobutton(
					self.root, text=file_name,
					padx = 20,
					variable = self.var,
					value = count, 
					command = self.selectFile).pack(anchor=W)
				count+=1
		else:
			Label(
				root, "No Files found.", 
				justify = LEFT, 
				padx = 20).pack()

	def buildEntry(self):
		global entry
		self.entry = Entry(self.root, bd =5)
		self.entry.pack(side=BOTTOM)

	def buildButtonSubmit(self):
		global button
		self.button = Button(self.root, text="Submit")
		self.button.pack()
		self.button.bind('<Button-1>', self.getText)

	def buildButtonSave(self):
		global buttonSave
		self.buttonSave = Button(self.root, text="Save", state="disabled")
		self.buttonSave.pack()
		self.buttonSave.bind('<Button-1>', self.saveCard)

	def buildButtonSkip(self):
		global buttonSkip
		self.buttonSkip = Button(self.root, text="Skip", state="disabled")
		self.buttonSkip.pack()
		self.buttonSkip.bind('<Button-1>', self.next)

	def selectFile(self):
		global vocab_dictionary

		selection = self.var.get()
		self.file_selected_label.config(text = self.file_list[selection])
		self.file_selected = self.file_list[selection]

		file = openFile(self.file_selected)

		#load words from file into vocab dictionary
		self.vocab_dictionary = storeVocabWords(file)
		self.vocab_dictionary = getShuffledDictionary(self.vocab_dictionary)

		#Start at first card
		global index
		self.index = 0

		#Reset Score
		global points
		self.points = 0

		#Reset Missed Words
		global missed_words
		self.missed_words = {}

		global english_list
		self.english_list = list(self.vocab_dictionary.keys())

		print self.english_list[self.index]
		self.note_card_text.set( self.english_list[self.index] )

	def getText(self, event):
	    global index
	    global english_list

	    user_input = self.entry.get()
	    print user_input
		
		#clear entry box
	    self.entry.delete(0, len(user_input))
	    
	    self.scoreInput(user_input, self.index)

	def saveCard(self, event):
		global missed_words
		global index
		global english_list
		global vocab_dictionary

		missed_words[ english_list[self.index] ] = vocab_dictionary[ english_list[self.index] ]
		next(event)

	def next(self, event):
		global button
		global buttonSave
		global buttonSkip

		self.button.config(state='active')
		self.buttonSave.config(state='disabled')
		self.buttonSkip.config(state='disabled')

		self.nextWord()

	def nextWord(self):
		global index
		global note_card_message
		global missed_words

		self.note_card_message.config(bg='lightgreen')
		if self.index < len(self.english_list) - 1:
			self.index += 1
			self.note_card_text.set( self.english_list[self.index] )
		else:
			self.note_card_text.set( self.getScore() )
			if len(missed_words) > 0:
				self.writeMissedFile(self.missed_words)


	def scoreInput(self, user_input, index):
		global points
		global english_list
		global vocab_dictionary
		
		#test
		print user_input + ' == ' + self.vocab_dictionary[ self.english_list[self.index] ]

		if user_input == self.vocab_dictionary[ self.english_list[self.index] ]:
			self.points += 1
			self.nextWord()
		else:
			self.wrongTry()

	def wrongTry(self):
		global note_card_message
		global note_card_text
		global button
		global buttonSave
		global buttonSkip

		self.button.config(state='disabled')
		self.note_card_message.config(bg='red')
		self.note_card_text.set( 'Incorrect\nSave this card?' )

		#prompt to save
		self.buttonSave.config(state='active')
		self.buttonSkip.config(state='active')

	def getScore(self):
		global points
		global vocab_dictionary

		return str(self.points) + '/' + str(len(self.vocab_dictionary)) + '\n{0:.0f}%'.format( ((1.0)*self.points/len(self.vocab_dictionary))*100 )