#Create a vocabulary quiz GUI program that requests the name of a vocab file in the current dricetory, 
#quizzes the user on a subset of the words in the vocabulary file, and then gives the user the option to write 
#out any missed words to a new vocabulary file.

getFile()

def getFile():

	found_file = False

	while(not found_file):

		file_name = raw_input()
		
		try:
			file_object = open(file_name, 'r')
			found_file = True
		except IOError:
			print '\'' + file_name + '\' does not exist. Enter a valid file name.'



