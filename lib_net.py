# as_util_html.py  written by Duncan Murray 7/8/2013   (C) Acute Software
# utility functions for HTML work, mainly from udacity course

import csv
import urllib.request

def main():
	TEST()
	
def TEST():
	print(" \n --- Testing Net functions  --- ")
	print(" ------------------------------ ")
	print(escape_html("hi there"))
	print(escape_html("hi <t>here"))
	print('downloading file http://gdeltproject.org/data/lookups/CAMEO.country.txt to test_country.txt')
	DownloadFile('http://gdeltproject.org/data/lookups/CAMEO.country.txt', 'test_country.txt')
	print('done')
	
def DownloadFile(url, filename):
	output = open(filename,'wb')
	output.write(urllib.request.urlopen(url).read())
	output.close()
	
def CreateCssString(fontFamily, baseFontSize):
    css = "<STYLE>"
    css = css + "BODY {      font-size:" + baseFontSize + "; FONT-FAMILY:" + fontFamily + "; }"
    css = css + "A:link {    font-size:" + baseFontSize + "; COLOR: blue;TEXT-DECORATION:none}"
    css = css + "A:visited { color: #003399; font-size:" + baseFontSize + ";TEXT-DECORATION:none }"
    css = css + "A:hover {   color:#FF3300;TEXT-DECORATION:underline}"
    css = css + "TD {        font-size:" + baseFontSize + "; valign=top; FONT-FAMILY:Verdana; padding: 1px 2px 2px 1px;  }"
    css = css + "H1 {        font-size:200%; padding: 1px 0px 0px 0px; margin:0px; }"
    css = css + "H2 {        font-size:160%; FONT-WEIGHT:NORMAL; margin:0px 0px 0px 0px; padding:0px; }"
    css = css + "H3 {        font-size:100%; FONT-WEIGHT:BOLD; padding:1px; letter-spacing:0.1em; }"
    css = css + "H4 {        font-size:140%; FONT-WEIGHT:NORMAL; margin:0px 0px 0px 0px; padding:1px; }"
    css = css + "</STYLE>"
    return css
    
def escape_html(s):
    res = s
    res = res.replace('&', "&amp;")
    res = res.replace('>', "&gt;")
    res = res.replace('<', "&lt;")
    res = res.replace('"', "&quot;")
    return res

def BuildHTMLHeader(title, linefeed='\n'):
    res = "<HTML><HEAD><title>" + linefeed
    res = res + title + "</title>" + linefeed
    res = res + "<link rel=\"stylesheet\" type=\"text/css\" href=\"" + linefeed
    res = res + CreateCssString("Verdana", "12pt" ) + linefeed
    res = res + "\" /></HEAD><BODY><H1>"
    res = res + title + "</H1><TABLE border=1>"
    return res
    
def FormatCsvAsHtml(csvFile, opHTML):
    fop = open(opHTML, 'w')
    fop.write(BuildHTMLHeader(csvFile))
    with open(csvFile) as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            fop.write("<TR>")
            for col in row:
                fop.write("<TD>")
                fop.write(col)
                fop.write("</TD>")
            fop.write("</TR>")
        fop.write("</TABLE>")
    fop.write("</BODY></HTML>")
    fop.close()
    
def DisplayImagesAsHTML(imageList):
    pass
    
	
if __name__ == '__main__':
    main()	    
    