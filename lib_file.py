# lib_file.py   written by Duncan Murray 6/7/2013  (C) Acute Software
import os
import shutil
import csv
import glob
import fnmatch
import time
from datetime import datetime

def TEST():
    print(" --- Testing File functions --- ")
    print("TODO")
 
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

def AppendToFile(fname, txt):
    with open(fname, "a") as myfile:
        myfile.write(txt)
        
def ConvertFileToCSV(txt_file, csv_file, delim):
    # function to simply convert the diary files to csv - testing
    in_txt = csv.reader(open(txt_file, "r"), delimiter = delim)
    #out_csv = csv.writer(open(csv_file, 'w')
    ofile  = open(csv_file, 'w', newline='')
    out_csv = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    #print (in_txt)
    if in_txt != "":
        out_csv.writerows(in_txt)
    

def wipe_dir(d):
    if d == "" or len(d) < 4:
        print("ERROR - are you sure you want to wipe all the files from " + d )
    else:
        shutil.rmtree(d)

def deleteFile(f):
    if f == "":
        pass
    else:
        try:
            os.remove(f)
        except:
            print("Cant delete ",f)

def LoadFileToList(fname):
    f = open(fname, 'r')
    l = f.read()
    return l
            
            
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
                        
    print("Found ", numFiles, " files")
    return opFileList

def TestFileList():
    # function to test the file list functions
    lstPaths = [r"C:\user\dev\src\python\AI", r"C:\user\dev\src\python\gfx" ]
    lstXtn = ["*.py", "*.csv"]
    lstExcluded = ["\bk", "\backup", "\z_bk"]
    fl = GetFileList(lstPaths, lstXtn, lstExcluded, True)
    SaveFileList(fl, "filelist-test.csv", ["name", "path", "size", "date"])
    
def GetDateAsString(t):
    return str(datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S"))
        
    
    
def SaveFileList(filelist, opFile, opFormat, delim=','):
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
            line = f + ","
            for fld in opFormat:
                if fld == "name":
                    line = line + os.path.basename(f) + delim
                if fld == "date":
                    line = line + GetDateAsString(os.path.getmtime(f)) + delim # str(datetime.fromtimestamp(modifiedTime).strftime("%Y%m%b %H:%M:%S"))
                if fld == "size":
                    line = line + str(os.path.getsize(f)) + delim
                if fld == "path":
                    line = line + os.path.dirname(f) + delim
                    
            #line = os.path.basename(f) + ',' + str(os.path.getsize(f)) + ',' + f + '\n'
            fout.write (line + '\n')
        print ("Finished saving " , opFile)






  