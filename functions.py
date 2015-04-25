from os import listdir,getcwd
from os.path import isfile, join

def avaliableLibraries():
	path = getcwd()
	onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]

	librarie_files = []
	for files in onlyfiles:
		tokens = files.split(".")

		if tokens[-1] == ".txt":
			librarie_files.append("files")

	return librarie_files
