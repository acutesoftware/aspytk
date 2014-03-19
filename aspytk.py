# aspytk.py     written by Duncan Murray 8/8/2013 (C) Acute Software
# Acute Software PYthon ToolKit - Free to use for personal use.
# Misc. library of scripts / recipes used for managing files and data

import lib_file as fle      # file / folder functions
import lib_data as dat      # basic data processing functions
import lib_net as net       # network / web scraping functions
#import lib_image as img     # image processing utils
import lib_math as mth      # basic maths functions
#import lib_acute as acu     # sample applications using this lib
#import lib_time as tme      # timer utilities
#import lib_date as dte      # date calculation functions
#import lib_log as log       # standard logging 
#import lib_error as err     # error handling

import glob
import sys
import os
import time

def usage():
    print("Acute Software PYthon ToolKit - Free to use for personal use.")
    print("Collection of short python 3.3 recipes / functions written")
    print("and collected from various places [sources shown where known].")
    print("Sample Usage:")
    print("import lib_file as fle")
    print("fle.ConvertFileToCSV(txt_file, csv_file, delim)")
    print("")
    print("dat.split_CSV_by_Column_Values(ipFile, 16) # creates new file from each values of column 16 from ipFile "  )
    print("")


#fle.GetFolderSizes('S:\\DATA', 'S_DATA.csv', False)
#fle.GetFolderSizes('P:\\', 'P_photos.csv', False)

#fle.GetFolderSizes('P:\\__Downloads\\z', 'autodownload.csv', False)
#fle.GetFolderSizes('P:\\garden', 'garden_photos.csv', False)
#fle.GetFolderSizes('T:\\user\\dev\\src\\python', 'python_src.csv', False)
# works for one folder - fle.GetFileSizes('S://duncan//C//user//dev//src//python//ext-dl', False)
#stop
mth.TEST()    
dat.TEST()
net.TEST()
#lstFiles = img.TEST()
tmpFile = fle.TEST()    

ans = input("Press <Enter> to remove temp files, or <Ctrl><C> to leave files intact")
print ("Wiping temp files")
fle.deleteFile(tmpFile)
#fle.deleteListOfFiles(lstFiles)



