#Create a vocabulary quiz GUI program that requests the name of a vocab file in the current dricetory, 
#quizzes the user on a subset of the words in the vocabulary file, and then gives the user the option to write 
#out any missed words to a new vocabulary file.

#1. Check if there are any vocabulary files in the directory, which by convention are files that end in .txt. 
#Print the list of files found. If there aren't files ending in .txt, display an error message and quit.
import os, inspect

#this python file name
current_python_file = inspect.getfile(inspect.currentframe())

#file path of this python file
current_python_file_path = os.path.abspath(current_python_file)

#directory containing this python file
vocab_directory = os.path.dirname(current_python_file_path)



#2. Have the user select which vocabulary file he or she would like to use. Error check to make sure that they select a valid file (i.e., one of the files listed in step 1).

def getFile():

	found_file = False

	while(not found_file):

		file_name = raw_input()

		try:
			file_object = open(file_name, 'r')
			found_file = True
		except IOError:
			print '\'' + file_name + '\' does not exist. Enter a valid file name.'




getFile()

#3. Store the contents of the vocabulary file into a dictionary data structure.
#4. Print the number of English words in the dictionary.
#5. Quiz the user by using a randomly generated list of English words from the dictionary.
#6. If the user missed any questions, give the option to output the missed words to a new
#word list file.
#7. Print the number of words and scores that the user missed.