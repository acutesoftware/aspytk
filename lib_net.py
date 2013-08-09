# as_util_html.py  written by Duncan Murray 7/8/2013   (C) Acute Software
# utility functions for HTML work, mainly from udacity course

import csv

def TEST():
    print(" \n --- Testing Net functions  --- ")
    print(" ------------------------------ ")
    print(escape_html("hi there"))
    print(escape_html("hi <t>here"))

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

def FormatCsvAsHtml(csvFile, opHTML):
    fop = open(opHTML, 'w')
    fop.write("<HTML><HEAD><title>")
    fop.write(csvFile)
    fop.write("</title><link rel=\"stylesheet\" type=\"text/css\" href=\"")
    fop.write(CreateCssString("Verdana", "12pt" ))
    fop.write("\" /></HEAD><BODY><H1>")
    fop.write(csvFile)
    fop.write("</H1><TABLE border=1>")
    
    fop.write(csvFile)
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
    
    
    
    
    