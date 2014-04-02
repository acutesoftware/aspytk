# -*- coding: utf-8 -*-

# lib_excel.py		written by Duncan Murray  11/2/2014

import xlrd
import csv
import os
import sys
from collections import namedtuple
import glob
from random import randint

import collections

fldr = os.getcwd() + '//..//aspytk'
print('startup folder = ' + fldr)
sys.path.append(fldr)
import lib_file as fle
import lib_data as dat

import sys
print(sys.version)

def csv_from_excel(excel_file, pth):
	opFname = ''
	print('converting file ' + excel_file + '  to folder ' + pth)
	workbook = xlrd.open_workbook(pth + '\\' + excel_file)
	all_worksheets = workbook.sheet_names()
	for worksheet_name in all_worksheets:
		print('converting - ' + worksheet_name)
		worksheet = workbook.sheet_by_name(worksheet_name)
		opFname = pth + '\\' + os.path.splitext(excel_file)[0] + '_' + worksheet_name + '.csv'
		print('SAVING - ' + opFname)
		csv_file = open(opFname, 'wb')
		#csv_file = open(pth + ''.join([worksheet_name,'.csv']), 'wb')
		wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

		for rownum in xrange(worksheet.nrows):
			wr.writerow([unicode(entry).encode("utf-8") for entry in worksheet.row_values(rownum)])
		csv_file.close()

def Step1_Convert_XLS_toCSV(fldr):			
	fl = fle.GetFileList(fldr, ['*.xlsx'], [".CSV"], True)
	for f in fl:
		print(f)
		csv_from_excel(os.path.basename(f) , os.path.dirname(f))

def Step2_AnalyseFiles(opFolder, fldr):
	fl_CSV = fle.GetFileList(fldr, ['*.CSV'], [".XLSX"], True)
	print(fl_CSV)
	numRecs = 0
	opFileName = os.getcwd() + '\\_opList.csv'
	fle.deleteFile(opFileName)
	for csvFileName in fl_CSV:
		numRecs = dat.countLinesInFile(csvFileName)
		print(csvFileName)
		fle.AppendToFile(opFileName, csvFileName + ',' + str(numRecs) + '\n')
		AnalyseCSV_File(csvFileName, opFolder)
		#os.system('analyseCSV.py "' + csvFileName + '" "' + csvFileName_RES + '"')	

		
def AnalyseCSV_File(datafile, opFolder):
	baseName = opFolder + '\\' + os.path.basename(datafile).split('.')[0]
	tmpfile = baseName + '.txt'
	colHeaders = dat.GetColumnList(datafile)
	colNum = 0
	for col in colHeaders:
		colText = "".join(map(str,col))    #prints JUST the column name in the list item
		print(colText)
		dat.GetCountUniqueValues(datafile, colNum, colText, 10, baseName + '_COL_VALUES.csv')
		dat.GetColumnCounts(datafile, colNum, colText, baseName + '_COL_COUNTS.csv')
		colNum = colNum + 1
		
		
		
######################
##   Main Program   ##
######################
print('\n lib_excel.py - importing source data\n')
Step1_Convert_XLS_toCSV(os.getcwd())	
Step2_AnalyseFiles(os.getcwd(), [os.getcwd()])

print('Done..')


	
	
