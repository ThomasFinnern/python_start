#!/usr/bin/python

import os
import getopt
import sys

from datetime import datetime

HELP_MSG = """
_emptyPy supports ...

usage: _emptyPy.py -? nnn -? xxxx -? yyyy  [-h]
	-? nnn
	-? 

	
	-h shows this message
	
	-1 
	-2 
	-3 
	-4 
	-5 
	
	
	example:
	
	
------------------------------------
ToDo:
ToDo:
  * 
  * 
  * 
  * 
  * 
  
"""

#-------------------------------------------------------------------------------
LeaveOut_01 = False
LeaveOut_02 = False
LeaveOut_03 = False
LeaveOut_04 = False
LeaveOut_05 = False

#-------------------------------------------------------------------------------

# ================================================================================
# _emptyPy
# ================================================================================

def _emptyPy (LeftPath, RightPath):
	try:
		print ('*********************************************************')
		print ('_emptyPy')
		print ('LeftPath: ' + LeftPath)
		print ('RightPath: ' + RightPath)
		print ('---------------------------------------------------------')
		
		#---------------------------------------------
		# check input
		#---------------------------------------------
		
		if LeftPath == '' :
			print ('***************************************************')
			print ('!!! Source folder (LeftPath) name is mandatory !!!')
			print ('***************************************************')
			print (HELP_MSG)
			Wait4Key ()
			sys.exit(1)
			
			
		if not testDir(LeftPath):
			print ('***************************************************')
			print ('!!! Source folder (LeftPath) path not found !!! ? -l ' + LeftPath + ' ?')
			print ('***************************************************')
			print (HELP_MSG)
			Wait4Key ()
			sys.exit(2)
			
			
		#--------------------------------------------------------------------
		
		if RightPath == '' :
			print ('***************************************************')
			print ('!!! Destination folder (RightPath) name is mandatory !!!')
			print ('***************************************************')
			print (HELP_MSG)
			Wait4Key ()
			sys.exit(1)
			
			
		if not testDir(RightPath):
			print ('***************************************************')
			print ('!!! Destination folder (RightPath) path not found !!! ? -r ' + RightPath + ' ?')
			print ('***************************************************')
			print (HELP_MSG)
			Wait4Key ()
			sys.exit(2)
			
		#--------------------------------------------------------------------
		# ToDo: exchange left <-> right if left is not on N:
		#--------------------------------------------------------------------
		

		#print ('LeftPath: ' + LeftPath)
		#print ('RightPath: ' + RightPath)
		#print ('---------------------------------------------------------')
		
		#--------------------------------------------------------------------
		# determine build ID
		#--------------------------------------------------------------------
		
		ZZZ = determineZZZ (LeftPath)
		print ('ZZZ: ' + ZZZ)
		
		
		#--------------------------------------------------------------------
		# create base folder
		#--------------------------------------------------------------------
		
		installPath = os.path.join (RightPath, ZZZ)
		print ('installPath: ' + installPath)
		if not os.path.exists(installPath):
			os.makedirs(installPath)
		
		#--------------------------------------------------------------------
		# copy cexecuter folder
		#--------------------------------------------------------------------
		
		copyCexecuterFolder (LeftPath, installPath)
		
		#--------------------------------------------------------------------
		# copy Macro folder
		#--------------------------------------------------------------------
		
		copyMacroFolder (LeftPath, installPath)
		
		#--------------------------------------------------------------------
		# Create 02 export install folder
		#--------------------------------------------------------------------
		
		dstPath = os.path.join(installPath, '02.' + ZZZ + '_export')
		if not os.path.exists(dstPath):
			os.makedirs(dstPath)
		
		#--------------------------------------------------------------------
		# Create 01 install folder
		#--------------------------------------------------------------------
		
		dstPath = os.path.join(installPath, '01.' + ZZZ)
		if not os.path.exists(dstPath):
			os.makedirs(dstPath)
		
		#--------------------------------------------------------------------
		# copy 7z Files
		#--------------------------------------------------------------------
		
		copy7zFiles (LeftPath, installPath)
		
		#--------------------------------------------------------------------
		# 
		#--------------------------------------------------------------------
		
		
		
		#--------------------------------------------------------------------
		# 
		#--------------------------------------------------------------------
		
		
		#--------------------------------------------------------------------
		# 
		#--------------------------------------------------------------------


	except Exception as ex:
		print(ex, inspect.stack()[1][3])

	finally:
		print ('exit _emptyPy')

#-------------------------------------------------------------------------------
#
def yyy (XXX):
	print ('    >>> Enter yyy: ')
	print ('       XXX: "' + XXX + '"')
	
	ZZZ = ""
	
	try:
		pass

	except Exception as ex:
		printEx(ex, inspect.stack()[1][3])

print ('    <<< Exit yyy: ' + ZZZ)
	return ZZZ

##-------------------------------------------------------------------------------
##
# def yyy (XXX):
# 	print ('    >>> Enter yyy: ')
# 	print ('       XXX: "' + XXX + '"')
#
# 	ZZZ = ""
#
# 	try:
# 		pass
#
# 	except Exception as ex:
# 		print ('yyy: ' + ex)
#
# 	print ('    <<< Exit yyy: ' + ZZZ)
# 	return ZZZ
#


# ================================================================================
# standard functions
# ================================================================================

# -------------------------------------------------------------------------------
# read all lines of a file into an text array without '\n'
def readLinesOfFile(FileName):
    print('    >>> Enter readLinesOfFile: ')
    print('       FileName: "' + FileName + '"')

    lines = []

    try:
        with open(FileName, 'r') as f:
            # lines = f.readlines()
            lines = [line.strip() for line in f.readlines()]
    except Exception as ex:
        printEx(ex, inspect.stack()[1][3])

    print('    <<< Exit readLinesOfFile: ' + str(len(lines)))
    return lines

def printEx(ex, functionName):
    print('\r\n\r\n!!! Exception caught in : ' + functionName + '\r\n' + str(ex) + '\r\n\r\n')
    return

def Wait4Key():
	try:
		input("Press enter to continue")
	except SyntaxError:
		pass		
			

def testFile(file):
	exists = os.path.isfile(file)
	if not exists:
		print ("Error: File does not exist: " + file)
	return exists

def testDir(directory):
	exists = os.path.isdir(directory)
	if not exists:
		print ("Error: Directory does not exist: " + directory)
	return exists

def print_header(start):

	print ('------------------------------------------')
	print ('Command line:', end='')
	for s in sys.argv:
		print (s, end='')
	
	print ('')
	print ('Start time:   ' + start.ctime())
	print ('------------------------------------------')

def print_end(start):
	now = datetime.today()
	print ('')
	print ('End time:               ' + now.ctime())
	difference = now-start
	print ('Time of run:            ', difference)
	#print ('Time of run in seconds: ', difference.total_seconds())

# ================================================================================
#   main (used from command line)
# ================================================================================
   
if __name__ == '__main__':

	start = datetime.today()

	optlist, args = getopt.getopt(sys.argv[1:], 'l:r:12345h')
	
	LeftPath = ''
	RightPath = ''
	
	for i, j in optlist:
		if i == "-l":
			LeftPath = j
		if i == "-r":
			RightPath = j
			
		if i == "-h":
			print (HELP_MSG)
			sys.exit(0)

		if i == "-1":
			LeaveOut_01 = True
			print ("LeaveOut_01")
		if i == "-2":
			LeaveOut_02 = True
			print ("LeaveOut__02")
		if i == "-3":
			LeaveOut_03 = True
			print ("LeaveOut__03")
		if i == "-4":
			LeaveOut_04 = True
			print ("LeaveOut__04")
		if i == "-5":
			LeaveOut_05 = True
			print ("LeaveOut__05")
	
	
	print_header(start)
	
	_emptyPy (LeftPath, RightPath)
	
	print_end(start)
	
