# lib_data.py 
# functions written and collected from github and python tutorials
# to work on datasets
import base64
import csv
import sys
import collections
import random
import re
import time

def TEST():
	print(" \n --- Testing Data functions --- ")
	print(" ------------------------------ ")
	print("Basic Text hiding (not encryption)")
	visible_text = 'password'
	poorly_hidden_text = encode(visible_text)  #
	print("Visible text  = ", visible_text)
	print("'hidden' text = ", poorly_hidden_text)
	print("Restored text = ", decode(poorly_hidden_text) )
	print("json time string : 1340578800000" , json_timestamp_as_string("1340578800000"))

def dict2list(dct, keylist): return [dct[i] for i in keylist]
def list2dict(L, keylist): return {k:v for (k,v) in zip(keylist, L)}
def List2String(l):
	res = ""
	for v in l:
		res = res + v
	return res

def Dict2String(d):
	res = ","
	for k, v in d: # .iteritems():
		res = res + k + str(v) + ','
	return res

def Dict2String_ORIG(d):
	res = ","
	for k, v in d: # .iteritems():
		res = res + k + ',' + str(v) + ','
	return res

def ForceToString(unknown):
	result = ''
	if type(unknown) is str:
		result = unknown
	if type(unknown) is int:
		result = str(unknown)
	if type(unknown) is dict:
		result = Dict2String(unknown)
	if type(unknown) is list:
		result = List2String(unknown)
	
	return result
	
def encode(visible_text): return base64.b64encode(bytes(visible_text, 'utf-8')).decode('utf-8')
def decode(poorly_hidden_text): return base64.b64decode(poorly_hidden_text).decode('utf-8')

def StriptHTMLtags(txt):
    return re.sub('<[^<]+?>', '', txt)

def GetCountUniqueValues(fname, colNum, colText, topN_values, opFile):
	cols = collections.Counter()
	with open(fname) as input_file:
		for row in csv.reader(input_file, delimiter=','):
			cols[row[colNum]] += 1
	print (colText, Dict2String(cols.most_common()[0:topN_values]))
	addSampleData(opFile, colText + ',' +  Dict2String(cols.most_common()[0:topN_values]))
	
def GetColumnCounts(fname, colNum, colText, opFile):
	cols = collections.Counter()
	with open(fname) as input_file:
		for row in csv.reader(input_file, delimiter=','):
			cols[row[colNum]] += 1
	print (colText, ': %s' % cols[row[colNum]])  # this is wrong
	addSampleData(opFile, colText + ': ' + str(cols[row[colNum]]))
	

def unix_head(ipFile, opFile, numLines):
	numRows = 0
	op = open(opFile, 'w')
	for line in open(ipFile,'r'):
		op.write(line)
		numRows = numRows + 1
		if numRows > numLines:
			break

def GetColumnList(csvFile):
	with open(csvFile, 'rt') as inf:
		inrd = csv.reader(inf)
		names = next(inrd)
	inf.close()
	return names
	
	
def getPercentRandomRecords(ipFile, opFile, percent):
    # Return a 'percent' of random lines from ipFile
	totRows = 0
	numRows = 0
	op = open(opFile, 'w')
	
	for line in open(ipFile,'r'):
		totRows = totRows + 1
		if totRows == 1:	# write header to output
			op.write(line)
		if random.randint(0,100) < percent :
			op.write(line)
			numRows = numRows + 1
	print("Wrote ",numRows, " out of ", totRows)

			
def createSampleFile(fname, header):
	wr = csv.writer(open(fname, 'wt'), quoting=csv.QUOTE_ALL, lineterminator='\n')
	wr.writerow(header)
	 
def addSampleData(fname, content):
	wr = csv.writer(open(fname, 'at'), quoting=csv.QUOTE_ALL, lineterminator='\n')
	wr.writerow(content)


def remove_duplicates(l):
    new_list = []
    for elem in l:
        if elem not in new_list:
            new_list.append(elem)

    return new_list
    #return list(set(l))   # this is pythonic way to do it for non nested list
	
	
def split_CSV_by_Column_names(inputfilename):  # TOK
	with open(inputfilename, 'rb') as inf:
		inrd = csv.reader(inf)
		names = next(inrd)
		outfiles = [open(n+'.csv', 'wb') for n in names]
		ouwr = [csv.writer(w) for w in outfiles]
		for w, n in zip(ouwr, names):
			w.writerow([n])
		for row in inrd:
			for w, r in zip(ouwr, row):
				w.writerow([r])
		for o in outfiles: o.close()

def split_CSV_by_Column_Values(ipFile, colName):  
	with open(ipFile, 'rb') as inf:
		inrd = csv.reader(inf)
		names = next(inrd)
		for row in csv.reader(inf):
			opName = os.path.basename(ipFile)[:-4] + '_' + row[colName] + '.csv'
			if not os.path.exists(opName):
				createSampleFile(opName, names)
			#print("Appending to ", opName)
			addSampleData(opName, row)


def countLinesInFile(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def ReadFileToList(fname, dataStartsAtRow = 2):
    lines = []
    try:
        f = open(fname, "rt")
        lines = f.readlines()[dataStartsAtRow-1:]  # starts at 0 so to user should start at line 1
    except:
        print ("Error - cant read file " , fname)
    #print ("Length of file = ", len(lines))
    #print (lines)
    return lines

def SaveListToFile(L, fname):
    f = open(fname, 'w')
    for item in L:
        f.write("%s\n" % item)
    f.close()
   
def print_no_newline(string):
	sys.stdout.write(string)
	sys.stdout.flush()  

    
def load_csv(fname, header_row=0, first_data_row=None,
             types=None, **kwargs):
    """Load a CSV file into a dictionary.

    The strings from the header row are used as dictionary keys.

    **Arguments:**

    - *fname*: Path and name of the file

    - *header_row*: Row that contains the keys (uses zero-based indexing)

    - *first_data_row*: First row of data (uses zero-based indexing)

         If *first_data_row* is not provided, then it is assumed that the data
         starts just after the header row.

    - *types*: List of data types for each column

         :class:`int` and :class:`float` data types will be cast into a
         :class:`numpy.array`.  If *types* is not provided, attempts will be
         made to cast each column into :class:`int`, :class:`float`, and
         :class:`str` (in that order).

    - *\*\*kwargs*: Additional arguments for :meth:`csv.reader`

    **Example:**

    >>> from modelicares import *
    >>> data = load_csv("examples/load-csv.csv", header_row=2)
    >>> print("The keys are: %s" % data.keys())
    The keys are: ['Price', 'Description', 'Make', 'Model', 'Year']
    """
    import csv

    try:
        reader = csv.reader(open(fname), **kwargs)
    except IOError:
        print('Unable to load "%s".  Check that it exists.' % fname)
        return

    # Read the header row and create the dictionary from it.
    for i in range(header_row):
        next(reader)
    keys = next(reader)
    data = dict.fromkeys(keys)
    print("The keys are: ")
    print(keys)

    # Read the data.
    if first_data_row:
        for row in range(first_data_row - header_row - 1):
            next(reader)
    if types:
        for i, (key, column, t) in enumerate(zip(keys, zip(*reader), types)):
            # zip(*reader) groups the data by columns.
            try:
                if isinstance(t, basestring):
                    data[key] = column
                elif isinstance(t, (float, int)):
                    data[key] = np.array(map(t, column))
                else:
                    data[key] = map(t, column)
            except ValueError:
                print("Could not cast column %i into %i." % (i, t))
                return
    else:
        for key, column in zip(keys, zip(*reader)):
            try:
                data[key] = np.array(map(int, column))
            except:
                try:
                    data[key] = np.array(map(float, column))
                except:
                    data[key] = map(str, column)

    return data

def json2dict(json_file):
	import json
	with open(json_file) as data_file:    
		data = json.load(data_file)
	return data

def json_pprint(json_file):
	import json
	from pprint import pprint
	with open(json_file) as data_file:    
		data = json.load(data_file)
	pprint(data)
	
def json_timestamp_as_string(ts):
	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(ts)/1000))

	
	
TEST()