import urllib   # URL Library	
import os		#Operation System Library
from sys import argv	# Args
import re 				# Regular Expressions
import sys


def Help():
	print "Secure Checker"
	print "---------------------"
	print "Link Giving Types"
	print " -u\t-> Give Url"
	print " -l\t-> To give a url file INFO: If link file fails in last link\ntry to give a blank line in the end."
	print "\nRequire Types"
	print " -a\t-> Show all found urls."
	print " -g\t-> Make group of Secure and Insecure links."
	print " -o\t-> To get txt output file of insecure urls."
	print "  \t->(To use it you have to use -g too.)\n"
	print "-s\t-> You can add your safe links in a file.\n"
	print "INFO: You can't use -a argument with -g.\n"

def SearchArgs():
	
	links = []
	if ("-l" in argv):
		print "File Called."
		try:
			f = open(argv[argv.index("-l")+1],"r").readlines()
			for i in f:
				if ("\n" in i):
					url =  i[:-1]
				else:
					url = i
				links.append(url)
		except:
			print "File Couldn't opened."
	elif ("-u" in argv):
		try:
			links.append(argv[argv.index("-u")+1])
		except:
			print "Url Couldn't uploaded."

	All = []
	All.append(links)


	if ("-a" in argv):
		All.append(1)
	elif ("-g" in argv):
		All.append(2)
	else:
		print "Require type couldn't determined."
		sys.exit(1)


	if ("-o" in argv):
		All.append(True)
	else():
		All.append(False)


	if ("safe.txt" in os.listdir()):
		All.append(True)
	else():
		All.append(False)




SearchArgs()
