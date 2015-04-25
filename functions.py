from os import listdir
from os.path import isfile, join

def avaliableLibraries():
	path = "/home/alexander/Documents/Python/Python Project"
	onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]

	librarie_files = []
	for files in onlyfiles:
		tokens = files.split(".")

		if tokens[-1] == ".txt":
			librarie_files.append("files")

	return librarie_files
