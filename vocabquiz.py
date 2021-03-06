#Create a vocabulary quiz GUI program that requests the name of a vocab file in the current dricetory, 
#quizzes the user on a subset of the words in the vocabulary file, and then gives the user the option to write 
#out any missed words to a new vocabulary file.

#1. Check if there are any vocabulary files in the directory, which by convention are files that end in .txt. 
#Print the list of files found. If there aren't files ending in .txt, display an error message and quit.
import os, inspect, random, datetime, time

def getFileList():
	#directory containing this python file
	current_directory = os.getcwd()

	#all files in current directory
	files_in_current_directory = os.listdir(current_directory)

	text_files = []

	for file in files_in_current_directory:
		if file[-4:] == '.txt' :
			text_files.append(file)

	return text_files
def printFiles():
	files_in_current_directory = getFileList()

	for file in files_in_current_directory:
		print file

#2. Have the user select which vocabulary file he or she would like to use. Error check to make sure that they select a valid file (i.e., one of the files listed in step 1).

def openFileTest():
	found_file = False
	while(not found_file):
		file_name = raw_input()
		try:
			file_object = open(file_name, 'r')
			found_file = True
			return file_object
		except IOError:
			print '\'' + file_name + '\' does not exist. Enter a valid file name.'
			printFiles()

def openFile(file_name):
	file_object = open(file_name, 'r')
	found_file = True
	return file_object

#3. Store the contents of the vocabulary file into a dictionary data structure.
def storeVocabWords(file):
	vocab_dictionary = {}
	for line in file:
		english_and_spanish = line.split()
		vocab_dictionary[ english_and_spanish[0] ] = english_and_spanish[2]
	return vocab_dictionary

#4. Print the number of English words in the dictionary.
def getNumOfEnglishWords(vocab_dictionary):
	return len(vocab_dictionary)

#5. Quiz the user by using a randomly generated list of English words from the dictionary.
def getShuffledDictionary(vocab_dictionary):
	shuffled_dictionary = {}
	while len(vocab_dictionary) > 0 :
		random.seed()
		#get random number
		index = random.randint(0, len(vocab_dictionary)-1)

		#key associated with that index
		english_word = getKeyByIndex(vocab_dictionary, index)

		#add element at that random index to the shuffled dictionary
		shuffled_dictionary[english_word] = vocab_dictionary[english_word]

		#remove element from dictionary
		del vocab_dictionary[english_word]
	return shuffled_dictionary

def getKeyByIndex(vocab_dictionary, index):
	count = 0
	for key in vocab_dictionary:
		if count == index :
			return key
		count+=1

#6. If the user missed any questions, give the option to output the missed words to a new word list file.
def quizUser(vocab_dictionary):
	missed_words = {}
	num_wrong = 0
	print 'Enter the corresponding spanish word'
	
	for english in vocab_dictionary:
		print english
		user_attempt = raw_input()
		if user_attempt == vocab_dictionary[english]:
			print 'Correct!'
		else:
			print 'Incorrect, press w to save this word'
			num_wrong+=1
			if raw_input() == 'w':
				missed_words[ english ] = vocab_dictionary[english]
	printScore(num_wrong, len(vocab_dictionary))
	return missed_words

#7. Print the number of words and scores that the user missed.
def printScore(num_missed, num_words):
	print 'You scored ' + str((num_words-num_missed)) + '/' + str(num_words)
	print 'You missed ' + str(num_missed) + ' words'
	print 'You scored {0:.2g}%'.format((num_words-num_missed)/num_words)

#write the missed dictionary to a file with the name missed-'currentdate'_'currenttime'
def writeMissedFile(missed_dictionary):
	
	#save the file as missed and the current date and time
	file_name = 'missed-' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S') + '.txt'

	file_writer = open(file_name, 'w')

	for english in missed_dictionary:
		file_writer.write(english + ' = ' + missed_dictionary[english] + '\n')
	file_writer.close()

#Demo
'''
print 'Enter which vocab file you would like to use: '
printFiles()
file = openFileTest()
vocab_dictionary = storeVocabWords(file)
num_of_english_words = getNumOfEnglishWords(vocab_dictionary)
vocab_dictionary = getShuffledDictionary(vocab_dictionary)

missed_words = quizUser(vocab_dictionary)

writeMissedFile(missed_words)
'''