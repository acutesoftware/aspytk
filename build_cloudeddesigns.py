# -*- coding: utf-8 -*-
# build_cloudeddesigns.py    written by Duncan Murray 20/1/2015
import os
import sys
import shutil

"""
index,webdesign,web_links_example
index,gadgets,self_sufficient_data_centre
page2,lifecube,Life_Cube_technical_requirements
page2,lifecube,life_cube_usage
index,house,dream_workshop
page3,house,house_plan_dog_house
page3,house,convert_wheat_silo_to_house
page2,webdesign,what_is_the_point_of_your_website
index,food,cooking-chart
page3,gadgets,idea_super_stick
page2,house,high_density_housing
page3,webdesign,log_of_building_a_drupal_website
index,house,zombie-proof-house
CAT,,lifecube
CAT,,food
CAT,,virtual
CAT,,webdesign
CAT,,about
CAT,,links
CAT,,house
CAT,,gadgets

This is version 0.1 of a simple application to demonstrate how to use various elements in a web application. It shows how to:





use Ajax in a text prompt to avoid needing a submit button on a form
use PHP to access source files (txt) on the server
use CSS to have a responsive design so it can be viewed on a desktop or smartphone

"""

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "AIKIF" + os.sep + "aikif" + os.sep + "lib") 
print("in test_cls_filelist : root_folder = " + root_folder)
sys.path.append(root_folder)


import cls_filelist as fl 
try:
	from BeautifulSoup import BeautifulSoup, Comment 
except:
	from bs4 import BeautifulSoup
    
source_folder = 'S:\\DATA\\BACKUP\\_WK\\site2015_dl'
html_folder   = 'T:\\user\\dev\\src\\python\\acuteweb\\deploy\\'
img_folder    = 'T:\\user\\dev\\src\\python\\acuteweb\\deploy\\img\\'




def main():
    print('Building static version of www.cloudeddesigns.com...')
    #lst = collect_source_file_list()
    #print(lst)
    pages = []
    with open('pages.csv', 'r') as flist:
        for line in flist:
            cols = line.split(',')
            content = create_html_page(cols[0], cols[1], cols[2].strip('\n'))
            pages.append([cols[0], cols[1], cols[2].strip('\n'), content])
    print("Done making " + str(len(pages)))
    make_index_pages(pages)
    

def make_index_pages(pages):
    f_ndx = open(html_folder + 'index.html', 'w')
    f_p2  = open(html_folder + 'page2.html', 'w')
    f_p3  = open(html_folder + 'page3.html', 'w')

    f_ndx.write(BuildHTMLHeader('Welcome', linefeed='\n', border='1') + '<TABLE valign=top align=center border=0>')
    f_p2.write(BuildHTMLHeader('Page 2', linefeed='\n', border='1') + '<TABLE valign=top align=center border=0>')
    f_p3.write(BuildHTMLHeader('Page 3', linefeed='\n', border='1') + '<TABLE valign=top align=center border=0>')
    
    for art in pages:
        #print('art = ', art)
        txt = ''
        nice_name = art[2].replace('_', ' ').replace('-', ' ').title()
        if art[0] == 'index':
            f_ndx.write('<TR><TD><H2>' + nice_name + '</H2>\n')
            f_ndx.write(art[3][0:800])
            if len(art[3]) > 800:
                f_ndx.write('<BR><BR><a href="' + art[2] + '.html">Read more...<a/><BR><BR>\n\n')
            else:
                f_ndx.write('<BR><BR><BR><BR>\n\n')
            f_ndx.write('</TD></TR>')
            
        if art[0] == 'page2':
            f_p2.write('<TR><TD><H2>' + nice_name + '</H2>\n')
            f_p2.write(art[3][0:800])
            if len(art[3]) > 800:
                f_p2.write('<BR><BR><a href="' + art[2] + '.html">Read more...<a/><BR><BR>\n\n')
            else:
                f_p2.write('<BR><BR><BR><BR>\n\n')
            f_p2.write('</TD></TR>')

        if art[0] == 'page3':
            f_p3.write('<TR><TD><H2>' + nice_name + '</H2>\n')
            f_p3.write(art[3][0:800])
            if len(art[3]) > 800:
                f_p3.write('<BR><BR><a href="' + art[2] + '.html">Read more...<a/><BR><BR>\n\n')
            else:
                f_p3.write('<BR><BR><BR><BR>\n\n')
            f_p3.write('</TD></TR>')

    print("\n\nart[0] = " + art[0])    
    f_ndx.write( '</TABLE>' + BuildHTMLFooter('index'))
    f_p2.write( '</TABLE>' + BuildHTMLFooter('page2'))
    f_p3.write( '</TABLE>' + BuildHTMLFooter('page3'))
    
    
    f_ndx.close()
    f_p2.close()
    f_p3.close()

    
def create_html_page(ndx, cat, art):
    fname = html_folder + art + '.html'
    nice_name = art.replace('_', ' ').replace('-', ' ').title()
    print('making html file = ' + fname)
    with open(fname, 'w') as f:
        f.write(BuildHTMLHeader(nice_name, linefeed='\n', border='1'))
        
        
        with open (source_folder + '\\' + art + '.html', "r") as myfile:
            web_text=myfile.read().replace('\n', '').replace('src="./' + art + '_files/', 'src="./img/').replace('<a href="http://www.cloudeddesigns.com/pics/', '<a href="img/')       
         
        p_html, p_txt = ExtractContent(web_text, 'field-items')
 #       f.write(p_html.replace('src="./' + art + '_files/', 'src="./img/'))
        f.write(p_html)
        
        f.write(BuildHTMLFooter(ndx))
        return p_html

def ExtractContent(rawText, divID):
    html = ''
    soup = BeautifulSoup(rawText)
    #results = soup.find("div", {"id": divID})
    
    results = soup.find("div", {"class": divID})
    #print(results)
    txt = results.getText()   # gives results without List items
    #print(str(len(txt)) + ' bytes read\n')
    tmp = ''
    old = ''
    new = ''
    for line in results.contents:
        tmp = str(line) + '\n'
        old, new = rename_node(tmp)
        html += tmp.replace(old, new)
    return html, txt

def rename_node(txt):
    """
    takes a hard coded drupal rubbish and returns local href
    INPUT = <a href="http://www.cloudeddesigns.com/node/25">Self Sufficient Data Centre</a><br>
    OUTPUT = <a href="self_sufficient_data_centre.html">Self Sufficient Data Centre</a><br>
    """
    new_text = txt    
    p1 = txt.find('<a href="http://www.cloudeddesigns.com/node/')
    if p1 > 0:
        p2 = txt.find('"', p1 + 12)
        old_url = txt[p1:p2]
        p3 = txt.find('</a>', p1 + 32)
        #new_link = txt[p2+4:p3].lower().replace(' ', '_') + '.html>'
        new_link = txt[p1+48:p3].lower().replace(' ', '_') + '.html'
        new_url = '<a href="' + new_link + ''
        
        print('\n\np1 = ', p1, 'p2 = ', p2, 'p3 = ', p3, '\n')
        print('renaming \n' + old_url + ' \n' + new_url)
        return old_url, new_url
    return txt, txt
    
def collect_source_file_list():
    """
    S:\DATA\BACKUP\_WK\site2015_dl\idea_super_stick.html
    S:\DATA\BACKUP\_WK\site2015_dl\page2.html
    S:\DATA\BACKUP\_WK\site2015_dl\page3.html
    S:\DATA\BACKUP\_WK\site2015_dl\zombie-proof-house_files\zombie-proof-house-site-sm.jpg
    S:\DATA\BACKUP\_WK\site2015_dl\zombie-proof-house_files\zombie-proof-house-plan-sm.jpg
    """
    fl_html = fl.FileList([source_folder ], ['*.html','*.jpg' ], [])
    fl_html.save_filelist('web_files.csv', ['fullfilename'], delim=',', qu='"')
    return fl_html.get_list()


    
def copy_image(fullname, fname):
    # S:\DATA\BACKUP\_WK\site2015_dl\about_files
    print(' copying ' + fname)
    shutil.copy2(fullname, img_folder)

def CreateCssString(fontFamily, baseFontSize, linefeed='\n'):
    css = "<STYLE>" + linefeed
    css = css + "BODY {      font-size:" + baseFontSize + "; FONT-FAMILY:" + fontFamily + "; }" + linefeed
    css = css + "A:link {    font-size:" + baseFontSize + "; COLOR: blue;TEXT-DECORATION:none}" + linefeed
    css = css + "A:visited { color: #003399; font-size:" + baseFontSize + ";TEXT-DECORATION:none }" + linefeed
    css = css + "A:hover {   color:#FF3300;TEXT-DECORATION:underline}" + linefeed
    css = css + "TD {        font-size:" + baseFontSize + "; valign=top; FONT-FAMILY:Arial; padding: 1px 2px 2px 1px;  }" + linefeed
    css = css + "H1 {        font-size:200%; padding: 1px 0px 0px 0px; margin:0px; }" + linefeed
    css = css + "H2 {        font-size:160%; FONT-WEIGHT:NORMAL; margin:0px 0px 0px 0px; padding:0px; }" + linefeed
    css = css + "H3 {        font-size:100%; FONT-WEIGHT:BOLD; padding:1px; letter-spacing:0.1em; }" + linefeed
    css = css + "H4 {        font-size:140%; FONT-WEIGHT:NORMAL; margin:0px 0px 0px 0px; padding:1px; }" + linefeed
    css = css + "</STYLE>" + linefeed
    return css
    
def escape_html(s):
    res = s
    res = res.replace('&', "&amp;")
    res = res.replace('>', "&gt;")
    res = res.replace('<', "&lt;")
    res = res.replace('"', "&quot;")
    return res

def BuildHTMLHeader(title, linefeed='\n', border='1'):
    res = "<HTML><HEAD><title>" + linefeed
    res += title + " | Clouded Designs</title>" + linefeed
    #res = res + "<link rel=\"stylesheet\" type=\"text/css\" href=\"" + linefeed
    res += CreateCssString("Arial", "12pt", linefeed ) + linefeed
    res += '</HEAD><BODY><img src = "img/banner-v03b.jpg" width="100%">'
    res += '<TABLE align=center valign=top border=0 width=80%><TR>'
    cats = ['webdesign','food','virtual','lifecube','about','links','house','gadgets']
    for c in cats:
        res += '<TD><a href=' + c + '.html>' + c + '</a></td>'

    res += '</TR></TABLE><BR>'
    res += '<p><I>A place to discuss gadget ideas, electronic devices, design tips</I></p><BR><BR>'
    
    
    res += '<H1>' + title + "</H1><BR>"
    return res
    
def BuildHTMLFooter(ndx, linefeed='\n', border='1'):
    res = linefeed
   # print('IN FOOTER = ndx = ' + ndx)
    
    if ndx == 'index':
        res += '<BR><BR>1, <a href="page2.html">2</a>,  <a href="page3.html">3</a><BR><BR>'  
    elif ndx == 'page2':
        res += '<BR><BR><a href="index.html">1</a>, 2 <a href="page3.html">3</a><BR><BR>'  
    elif ndx == 'page3':
        res += '<BR><BR><a href="index.html">1</a>, <a href="page2.html">2</a>  3<BR><BR>'  
    res += "(C) Acute Software 2011 - 2015"
    res += "</body></HTML>" + linefeed
    return res
 
if __name__ == '__main__':
    main()	
  