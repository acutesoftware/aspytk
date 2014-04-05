# lib_file.py   written by Duncan Murray 6/7/2013  (C) Acute Software
import os
import shutil
import csv
import glob
import fnmatch
import time
from datetime import datetime
import lib_net as net 

def TEST():
    print(" \n --- Testing File functions --- ")
    print(" ------------------------------ ")
    tmpFile = "list_of_files.csv"
    fl = GetFileList([os.getcwd()], ['*.py'], ["__pycache__", ".git"], True)
    SaveFileList(fl, tmpFile, ["name", "path", "size", "date"])
    net.FormatCsvAsHtml(tmpFile, tmpFile + ".html")
    LaunchFile(tmpFile + ".html")
    return tmpFile
    
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
        
def AppendToFile(fname, txt):
    with open(fname, "a") as myfile:
        myfile.write(txt)

		
import inspect

def GetModuleName(skip=2):
	"""Get a name of a caller in the format module.class.method

	   `skip` specifies how many levels of stack to skip while getting caller
	   name. skip=1 means "who calls me", skip=2 "who calls my caller" etc.
	   
	   An empty string is returned if skipped levels exceed stack height
	   
	   credit - http://code.activestate.com/recipes/578352-get-full-caller-name-packagemodulefunction/
	"""
	stack = inspect.stack()
	start = 0 + skip
	if len(stack) < start + 1:
	  return ''
	parentframe = stack[start][0]    

	name = []
	module = inspect.getmodule(parentframe)
	# `modname` can be None when frame is executed directly in console
	# TODO(techtonik): consider using __main__
	if module:
		name.append(module.__name__)
	# detect classname
	if 'self' in parentframe.f_locals:
		# I don't know any way to detect call from the object method
		# XXX: there seems to be no way to detect static method call - it will
		#      be just a function call
		name.append(parentframe.f_locals['self'].__class__.__name__)
	codename = parentframe.f_code.co_name
	if codename != '<module>':  # top level usually
		name.append( codename ) # function or a method
	del parentframe
	return ".".join(name)		
		
		
def log(fname, txt, prg=''):
	# logs an entry to fname along with standard date and user details
	delim = ','
	q = '"'
	dte = TodayAsString()
	usr = net.GetUserName()
	hst = net.GetHostName()
	if prg == '':
		prg = GetModuleName()  # note - if you do this here it always returns 'AIKIF_utils.LogCommand'
	logEntry = q + dte + q + delim + q + usr + q + delim + q + hst + q + delim + q + prg + q + delim + q + txt + q + delim + '\n'
	with open(fname, "a") as myfile:
		myfile.write(logEntry)
	

def ConvertFileToCSV(txt_file, csv_file, delim):
    # function to simply convert the diary files to csv - testing
    in_txt = csv.reader(open(txt_file, "r"), delimiter = delim)
    #out_csv = csv.writer(open(csv_file, 'w')
    ofile  = open(csv_file, 'w', newline='')
    out_csv = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    #print (in_txt)
    if in_txt != "":
        out_csv.writerows(in_txt)

def LaunchFile(filename):
    os.system("start "+filename)    

def wipe_dir(d):
    if d == "" or len(d) < 4:
        print("ERROR - are you sure you want to wipe all the files from " + d )
    else:
        shutil.rmtree(d)

def GetShortFileName(filePath):
	return os.path.basename(filePath)

def GetFileSize(filePath):
	return os.path.getsize(filePath)

def GetPath(fileName):
	return os.path.dirname(fileName)
	
def deleteFile(f):
    if f == "":
        pass
    else:
        try:
            os.remove(f)
        except:
            print("Cant delete ",f)

def deleteListOfFiles(fl):
    for f in fl:
        print("Deleting ", f)
        #deleteFile(f)

            
def LoadFileToList(fname):
    f = open(fname, 'r')
    l = f.read()
    return l
            
def LoadFileToDict(fname):
	d = {}
	with open(fname) as f:
		for line in f:
			print (line)
			(key, val) = line.split()
			d[int(key)] = val
	return d
            
            
def _glob(path, *exts):
    #Glob for multiple file extensions (stackoverflow)
    #Parameters
    #path : str =     A file name without extension, or directory name
    #exts : tuple =   File extensions to glob for
    #Returns   files : list =   list of files matching extensions in exts in path
    path = os.path.join(path, "*") if os.path.isdir(path) else path + "*"
    return [f for files in [glob.glob(path + ext) for ext in exts] for f in files]

    
def GetFileList(lstPaths, lstXtn, lstExcluded, VERBOSE = False):
	# written by Duncan Murray 7/8/2013 (C) Acute Software
	# builds a list of files and returns as a list 
	if VERBOSE:
		print("Generating list of Files...")
		print("Paths = ", lstPaths)
		print("Xtns  = ", lstXtn)
		print("exclude = ", lstExcluded)
	numFiles = 0    
	opFileList = []
	for rootPath in lstPaths:
		if VERBOSE:
			print(rootPath)
		for root, dirs, files in os.walk(rootPath):
			for basename in files:
				for xtn in lstXtn:
					if fnmatch.fnmatch(basename, xtn):
						filename = os.path.join(root, basename)
						includeThisFile = "Y"
						#print ("filename = ", filename, " Exlude = ", lstExcluded)
						if len(lstExcluded) > 0:
							for exclude in lstExcluded:
								if filename.find(exclude) != -1:
									includeThisFile = "N"
						if includeThisFile == "Y":
							if VERBOSE:
								print(os.path.basename(filename), '\t', os.path.getsize(filename))
							numFiles = numFiles + 1
							opFileList.append( filename)
	if VERBOSE:
		print("Found ", numFiles, " files")
	return opFileList

def GetFolderSizes(rootPath, opFile, printDetails = True):
    numFiles = 0
    numPaths = 0
    totSize = 0
    fileSize = 0
    deleteFile(opFile)
    print('\n Checking folder - ', rootPath, '\n')
    for root, subFolders, baseNames in os.walk(rootPath):
        for folder in subFolders:
            filePath = os.path.join(root, folder)
            #print (" -- %s" % ( filePath))
            numPaths = numPaths + 1
            res = GetFileSizes(filePath, False)
            AppendToFile(opFile, res)
    res = GetFileSizes(rootPath, False)  # now get the root files and total size
    AppendToFile(opFile, res)
    
def GetFileSizes(rootPath, printDetails = True):
    numFiles = 0
    numPaths = 0
    totSize = 0
    fileSize = 0
    for root, subFolders, baseNames in os.walk(rootPath):
        for folder in subFolders:
            #print ("%s has subdirectory %s" % (root, folder))
            numPaths = numPaths + 1
            #GetFileSizes(rootPath, False)
        for shortNames in baseNames:
            filename = os.path.join(root, shortNames) 
            filePath = os.path.join(root, filename)
            fileSize = os.path.getsize(filename)
            #print('baseNames= ' ,baseNames)
            #print('filename = ' + filename)
            #print('fileSize = ' + str(fileSize))
            if printDetails:
                print(filename, '\t', fileSize)
            numFiles = numFiles + 1
            totSize = totSize + fileSize
            
    #print ('Total Paths = ', str(numPaths))
    result = rootPath + ',' + str(numPaths) + ',' + str(numFiles) + ',' + str(totSize) + '\n'       
    print (result)
    return result
    
def TestFileList():
    # function to test the file list functions
    lstPaths = [r"C:\user\dev\src\python\AI", r"C:\user\dev\src\python\gfx" ]
    lstXtn = ["*.py", "*.csv"]
    lstExcluded = ["\bk", "\backup", "\z_bk"]
    fl = GetFileList(lstPaths, lstXtn, lstExcluded, True)
    SaveFileList(fl, "filelist-test.csv", ["name", "path", "size", "date"])
    
def GetDateAsString(t):
	res = ''
	try:
		res = str(datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S"))
	except:
		pass
	return res     
	
def TodayAsString():	# returns current date and time like oracle
#	return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	
    
    
def SaveFileList(filelist, opFile, opFormat, delim=',', qu='"'):
    # written by Duncan Murray 7/8/2013 (C) Acute Software
    # uses a List of files and collects meta data on them and saves 
    # to an text file as a list or with metadata depending on opFormat.
    with open(opFile,'w', encoding='utf-8') as fout:
        #Print header
        fout.write("fullFilename" + delim)
        for colHeading in opFormat:
            fout.write(colHeading + delim)
        fout.write('\n')    
        #Print all file data
        for f in filelist:
            line = qu + f + qu + delim
            for fld in opFormat:
                if fld == "name":
                    line = line + qu + os.path.basename(f) + qu + delim
                if fld == "date":
                    line = line + qu + GetDateAsString(os.path.getmtime(f)) + qu + delim # str(datetime.fromtimestamp(modifiedTime).strftime("%Y%m%b %H:%M:%S"))
                if fld == "size":
                    line = line + qu + str(os.path.getsize(f)) + qu + delim
                if fld == "path":
                    line = line + qu + os.path.dirname(f) + qu + delim
                    
            #line = os.path.basename(f) + ',' + str(os.path.getsize(f)) + ',' + f + '\n'
            fout.write (line + '\n')
            #print(line)
        print ("Finished saving " , opFile)



def DownloadFileFromSharepoint(url, local_file_name):
	# from http://stackoverflow.com/questions/2149496/downloading-a-file-protected-by-ntlm-sspi-without-prompting-for-credentials-usin
	# you need to run this on Windows probably, and import ctypes
	ctypes.windll.urlmon.URLDownloadToFileA(0,url,local_file_name,0,0)
	print("Finished downloading ", local_file_name)



  