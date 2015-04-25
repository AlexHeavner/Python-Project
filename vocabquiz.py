#Create a vocabulary quiz GUI program that requests the name of a vocab file in the current dricetory, 
#quizzes the user on a subset of the words in the vocabulary file, and then gives the user the option to write 
#out any missed words to a new vocabulary file.

#1. Check if there are any vocabulary files in the directory, which by convention are files that end in .txt. 
#Print the list of files found. If there aren't files ending in .txt, display an error message and quit.
import os, inspect, random

def printFiles():
	#directory containing this python file
	current_directory = os.getcwd()

	#all files in current directory
	files_in_current_directory = os.listdir(current_directory)

	for file in files_in_current_directory:
		if file[-4:] == '.txt' :
			print file

#2. Have the user select which vocabulary file he or she would like to use. Error check to make sure that they select a valid file (i.e., one of the files listed in step 1).

def openFile():

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

#Demo
print 'Enter which vocab file you would like to use: '
printFiles()
file = openFile()
vocab_dictionary = storeVocabWords(file)
vocab_dictionary = getShuffledDictionary(vocab_dictionary)
print vocab_dictionary
for english in vocab_dictionary:
	print english + ' => ' + vocab_dictionary[english]

num_of_english_words = getNumOfEnglishWords(vocab_dictionary)

print num_of_english_words


#6. If the user missed any questions, give the option to output the missed words to a new word list file.
#7. Print the number of words and scores that the user missed.