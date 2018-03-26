#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 19:45:42 2018

@author: Pranshu Sinha, Abhay Soni
"""
import random
import string
import os

#Short-listed some of the most commonly used fonts in web pages
fonts = ['Arial','Helvetica','Times New Roman','Times','Courier New','Courier','Verdana','Georgia','Palatino','Garamond','Bookman','Comic Sans MS','Trebuchet MS','Arial Black','Impact']
font_style = ['normal', 'italic','oblique']
font_weight = ['normal', 'bold']
font_align = ['center', 'left']
html = ''
css_contents = {}
count=0
css = ''

#generate a skeleton HTML file with a doctype, head element, and body element and adds CSS to it
def RandomHtml():
    yield '<!DOCTYPE html>'
    yield '<html>\r\n'
    yield ' RANDOMCSSCONTENTHERETOBEPLACED '
    yield '<body>\r\n'
    yield RandomSection()
    yield '</body>\r\n</html>\r\n'
    RandomCSS()

#generate a random section
def RandomSection():
    global css
    global count
    for x in range(0,random.randrange(5,10)):
        random_header_number = random.randrange(3,5)
        if not '<h'+str(random_header_number)+' id=a"'+str(count)+'">' in css_contents:
            css_contents[count] = '<h'+str(random_header_number)+'>'
            count+=1
        yield '<p id="a'+str(count)+'">'
        count+=1
        num_of_sentences = random.randrange(2, 15)
        for _ in range(num_of_sentences):
             yield RandomSentence()
        yield '</p>\r'
        yield ('\n')

#generate a random sentence using random range function
def RandomSentence():
    global count
    num_of_words = random.randrange(5, 20)
    yield (' '.join(RandomWord() for _ in range(num_of_words)) + '.')

def RandomWord():
    chars = random.randrange(2, 10)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(chars))

def RandomCSS():
    global count, fonts, font_style, font_weight, css
    string_css = '<head>\r\n<style>\r\n'
    for x in range(count):
        r = lambda: random.randint(0,255)
        string_css += '#a'+str(x)+' {\r\n'
        string_css += 'color: #%02X%02X%02X' %(r(),r(),r())+';\r\n'
        string_css += 'font-family: '+fonts[random.randrange(0, len(fonts))]+';\r\n'
        string_css += 'font-size: '+str(random.randrange(10, 25)) +'px;\r\n'
        string_css += 'font-style: '+font_style[random.randrange(0, len(font_style))]+';\r\n'
        string_css += 'font-weight: '+font_weight[random.randrange(0, len(font_weight))]+';\r\n'
        string_css += 'text-align: '+font_align[random.randrange(0, len(font_align))]+';\r\n}\r\n'
    string_css += '\r\n</style>\r\n</head>\r\n'
    css = string_css

def Output(generator):
    global html
    if(isinstance(generator, str)):
        html = html+generator
    else:
        for g in generator: Output(g)

#As of now, we are creating 5 random files
if not os.path.exists(os.getcwd()+'/Generated_HTML_Files/'):
    os.makedirs(os.getcwd()+'/Generated_HTML_Files/')

os.chdir(os.getcwd()+'/Generated_HTML_Files/')
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
