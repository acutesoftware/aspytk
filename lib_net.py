# as_util_html.py  written by Duncan Murray 7/8/2013   (C) Acute Software
# utility functions for HTML work, mainly from udacity course

def TEST():
    print(" --- Testing Net functions --- ")
    print(escape_html("hi there"))
    print(escape_html("hi <t>here"))
 
def escape_html(s):
    res = s
    res = res.replace('&', "&amp;")
    res = res.replace('>', "&gt;")
    res = res.replace('<', "&lt;")
    res = res.replace('"', "&quot;")
    return res
