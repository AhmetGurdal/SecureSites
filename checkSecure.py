# http://cse.akdeniz.edu.tr/
import urllib   # URL Library	
import os		#Operation System Library
from sys import argv	# Args
import re 				# Regular Expressions
import sys

def Help():
	print "Secure Checker"
	print "---------------------"
	print "-u\t-> Give Url"
	print "-a\t-> Show all found urls."
	print "-g\t-> Make group of Secure and Insecure links."
	print "-l\t-> To give a url file INFO: If link file fails in last link\ntry to give a blank line in the end."
	print "-o\t-> To get txt output file of insecure urls."
	print "  \t->(To use it you have to use -g too.)\n"
	print "INFO: You can add your safe links in 'safe.txt' \n(which have to in the same directory.)\n"

def ShowAll():
	httpl = []
	httpsl = []
	ftpl = []
	ftpsl = []

	for i in links:
		if "https" in i[:6]:
			httpsl.append(i)
		elif "http" in i[:6]:
			httpl.append(i)
		elif "ftps" in i[:6]:
			ftpsl.append(i)
		elif "ftp" in i[:6]:
			ftpl.append(i)

	if len(httpl) >0:
		print "\nHTTP LINKS"
		print "------------"
		for i in httpl:
			print i

	if len(httpsl) >0:
		print "\nHTTPS LINKS"
		print "------------"
		for i in httpsl:
			print i
		
	if len(ftpsl) >0:
		print "\nFTPS LINKS"
		print "------------"
		for i in ftpsl:
			print i
		
	if len(ftpl) >0:
		print "\nFTP LINKS"
		print "------------"
		for i in ftpl:
			print i
		
	if len(ftpl) + len(ftpsl) + len(httpl) + len(httpsl) < len(links):
		print "Other Links"
		print "--------------"
		for i in links:
			if (i not in ftpl and i not in ftpsl and i not in httpsl and i not in httpl):
				print i

def ShowSecure(domain):
	secure = []
	insecure = []
	for  i in links:
		if domain in i:
			secure.append(i)
		else:
			insecure.append(i)
	if (len(secure)>0 and "-i" not in argv):

		print "\nSecure Links"
		print "-----------------"
		for  i in secure:
			print i

	if (len(insecure)>0):
		print "\nInsecure Links"
		print "----------------"
		for  i in insecure:
			print i

	return insecure

def Search(url):

	src = urllib.urlopen(url).read()


	ulinks = re.findall(r"(http|ftp|ftps|https|gother|mailto|mid|cid|news|nntp|prospero|telnet|rlogin|tn3270|wais):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?",src)
	links = []
	for i in ulinks:
		link = ""
		
		for j in i:
			link += j
			if j == "http" or j == "https":
				link += "://"
		
		links.append(link)
	return links

if ("-u" in argv):
	try:
		url = argv[argv.index("-u")+1]
		links = Search(url)
		if("-a" in argv):
			ShowAll()

		if ("-g" in argv):
			secure = []
			insecure = []
			domain = re.findall(r"([A-Z|a-z|0-9]+\.)(com|org|net|edu|gov|blogspot)(\.\w+)?",url)
			domain = str(domain[0])[1:-1].replace("'","").replace(",","").replace(" ","")
			insecure = ShowSecure(domain)
			if ("-o" in argv):	
				name = re.sub(r"(http|ftp|ftps|https|gother|mailto|mid|cid|news|nntp|prospero|telnet|rlogin|tn3270|wais):\/\/","",url)
				name = re.sub(r"\/.*","",name)
				print name
				out = file (str(name) + ".txt","w")
				out.close()
				out = file(str(name) + ".txt","a")
				try:
					safe = file("safe.txt","r").readlines()

					for  i in insecure:
						issafe = False
						for j in safe:
							if "\n" in j:
								j = j[:-1]
							if (j in i):
								print i + " -> True"
								issafe = True
								break
						if (issafe == False):
							out.write(i + "\n")
				except:
					for  i in insecure:
						out.write(i + "\n")
					out.close()
	except:
		Help()
		sys.exit(1)


elif ("-l" in argv):
	try:
		f = open(argv[argv.index("-l")+1],"r").readlines()
		for i in f:
			if ("\n" in i):
				url =  i[:-1]
			else:
				url = i
			print "* Searching for " + url
			print "----------------------------"
			links = Search(url)
			
			if("-a" in argv):
				ShowAll()

			if ("-g" in argv):
				secure = []
				insecure = []
				
				domain = re.findall(r"([A-Z|a-z|0-9]+\.)(com|org|net|edu|gov|blogspot)(\.\w+)?",url)

				domain = str(domain[0])[1:-1].replace("'","").replace(",","").replace(" ","")
				insecure = ShowSecure(domain)
				
				if ("-o" in argv):
					
					name = re.sub(r"(http|ftp|ftps|https|gother|mailto|mid|cid|news|nntp|prospero|telnet|rlogin|tn3270|wais):\/\/","",url)
					name = re.sub(r"\/.*","",name)
					print "\n***File Name: " + name + ".txt"
					print "----------------------"
					out = file (str(name) + ".txt","w")
					out.close()
					out = file(str(name) + ".txt","a")
					
					try:
						safe = file("safe.txt","r").readlines()

						for  i in insecure:
							issafe = False
							for j in safe:
								if "\n" in j:
									j = j[:-1]
								if (j in i):
									print i + " -> True"
									issafe = True
									break
							if (issafe == False):
								out.write(i + "\n")
						out.close()
						
					except:
						for  i in insecure:
							out.write(i + "\n")
						out.close()


			print "----------------------------"
			print "* Completed searching for " + url
	except:
		Help()



else:
	Help()





