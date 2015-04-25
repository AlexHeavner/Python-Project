#Create a vocabulary quiz GUI program that requests the name of a vocab file in the current dricetory, 
#quizzes the user on a subset of the words in the vocabulary file, and then gives the user the option to write 
#out any missed words to a new vocabulary file.

#1. Check if there are any vocabulary files in the directory, which by convention are files that end in .txt. 
#Print the list of files found. If there aren't files ending in .txt, display an error message and quit.
import os, inspect

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
	for line in file:
		print line

#Demo
print 'Enter which vocab file you would like to use: '
printFiles()
file = openFile()
storeVocabWords(file)




#4. Print the number of English words in the dictionary.
#5. Quiz the user by using a randomly generated list of English words from the dictionary.
#6. If the user missed any questions, give the option to output the missed words to a new
#word list file.
#7. Print the number of words and scores that the user missed.