#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 19:45:42 2018

@author: PranshuSinha
"""
import random
import string

fonts = ['Arial','Helvetica','Times New Roman','Times','Courier New','Courier','Verdana','Georgia','Palatino','Garamond','Bookman','Comic Sans MS','Trebuchet MS','Arial Black','Impact']
font_style = ['normal', 'italic','oblique']
font_weight = ['normal', 'bold']
font_align = ['center', 'left', 'right']
html = ''
css_contents = {}
count=0
css = ''
def RandomHtml():
    yield '<html>\r\n'
    yield ' RANDOMCSSCONTENTHERETOBEPLACED '
    yield '<body>\r\n'
    yield RandomBody()
    yield '</body>\r\n</html>\r\n'
    RandomCSS()


def RandomCSS():
    global count, fonts, font_style, font_weight, css
    string_css = '<head>\r\n<style>\r\n'
    for x in range(count):
        r = lambda: random.randint(0,255)
        string_css += '#a'+str(x)+' {\r\n'
        string_css += 'color: #%02X%02X%02X' %(r(),r(),r())+';\r\n'
        string_css += 'font-family: '+fonts[random.randrange(0, len(fonts))]+';\r\n'
        string_css += 'font-size: '+str(random.randrange(1, 40)) +'px;\r\n'
        string_css += 'font-style: '+font_style[random.randrange(0, len(font_style))]+';\r\n'
        string_css += 'font-weight: '+font_weight[random.randrange(0, len(font_weight))]+';\r\n'
        string_css += 'text-align: '+font_align[random.randrange(0, len(font_align))]+';\r\n}\r\n'
    string_css += '\r\n</style>\r\n</head>\r\n'
    css = string_css
    
    
    
def RandomBody():
    yield RandomSection()
    if random.randrange(2) == 0:
        yield RandomBody()

def RandomSection():
    global css
    global count
    for x in range(0, random.randrange(5,10)):
        for x in range(0,random.randrange(5,10)):
            random_header_number = random.randrange(1,6)
            if not '<h'+str(random_header_number)+' id=a"'+str(count)+'">' in css_contents:
                css_contents[count] = '<h'+str(random_header_number)+'>'
                count+=1
            yield '<h'+str(random_header_number)+'>'
            yield RandomSentence()
            yield '</h'+str(random_header_number)+'>\r\n'
            sentences = random.randrange(5, 20)
            for _ in range(sentences):
                 yield RandomSentence()

def RandomSentence():
    global count
    words = random.randrange(5, 15)
    yield '<p id="a'+str(count)+'">'
    count+=1
    yield (' '.join(RandomWord() for _ in range(words)) + '.').capitalize()
    yield '</p>\r\n'

def RandomWord():
    chars = random.randrange(2, 10)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(chars))

def Output(generator):
    global html
    if(isinstance(generator, str)):
        html = html+generator
    else:
        for g in generator: Output(g)


for x in range(0,5):
    html = ''
    css_contents = {}
    count = 0
    css = ''
    Output(RandomHtml())
    #print(css)
    html = html.replace('RANDOMCSSCONTENTHERETOBEPLACED', css)
    html_file = open("file{}.html".format(x), "w")
    html_file.write(html)
    html_file.close()
    print("The file: html{}.hmtl created!".format(x))
