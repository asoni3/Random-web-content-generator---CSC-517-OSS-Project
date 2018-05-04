#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 19:45:42 2018

@author: Pranshu Sinha, Abhay Soni
"""
import random
import string
import sys

html = ''
css = ''

#generate a skeleton HTML file with a doctype, head element, and body element and adds CSS to it
def RandomHtml(max_depth, super_random_css, num_sibling_divs, tree_height, quirks_mode_possible, max_headers, min_headers, theSize):
    count = [0]
    max_depth = [max_depth]
    
    quirksMode = random.randint(0,1)
    if quirksMode == 1 or quirks_mode_possible == False:
        yield '<!DOCTYPE html>'
        
    yield '<html>\r\n'
    yield ' RANDOMCSSCONTENTHERETOBEPLACED '
    yield '<body>\r\n'
    yield RandomSection(count, max_depth, num_sibling_divs, tree_height, max_headers, min_headers, theSize)
    yield '</body>\r\n</html>\r\n'
    RandomCSS(count[0], super_random_css, theSize)

#generate a random section
def RandomSection(count, max_depth, num_sibling_divs, tree_height, max_headers, min_headers, theSize):
    global css
    css_contents = {}

    for x in range(0,random.randrange(min_headers, max_headers)):
        random_header_number = random.randrange(3,5)
        if not '<h'+str(random_header_number)+' id=a"'+str(count[0])+'">' in css_contents:
            css_contents[count[0]] = '<h'+str(random_header_number)+'>'
            count[0]+=1
        yield '<p id="a'+str(count[0])+'">'
        count[0]+=1
        num_of_sentences = random.randrange(2, 15)
        for _ in range(num_of_sentences):
            yield RandomSentence(count[0])
        #Create a nested element 30% of the time
        if random.random() < .3:
            yield NestedElement(count, max_depth, num_sibling_divs, tree_height, max_headers, min_headers, theSize)
        yield '</p>\r'
        yield ('\n')

def NestedElement(count, max_depth, num_sibling_divs, tree_height, max_headers, min_headers, theSize):
    choose_element=[RandomSection, RandomTable, RandomOrderedList,RandomUnorderedList, RandomDiv]
        
    if max_depth[0] > 0:
        max_depth[0] = max_depth[0] - 1  
        chosen_element = random.choice(choose_element)
        
        if chosen_element == RandomDiv:
            yield chosen_element(tree_height, count, max_depth, num_sibling_divs, max_headers, min_headers, theSize)
        elif chosen_element == RandomSection:
            yield chosen_element(count, max_depth, num_sibling_divs, tree_height, max_headers, min_headers, theSize)
        else:
            yield chosen_element(theSize)
            
#generate a random sentence using random range function
def RandomSentence(count):
    num_of_words = random.randrange(5, 15)
    yield RandomWord()
    for _ in range(num_of_words-1):
        #1 in 20 words will be within a span
        z= random.randrange(0,99)
        if z<5:
            yield ' '
            yield ''.join(RandomSpan(count))
        else:
            yield ' '
            yield ''.join(RandomWord())
    yield '. '
            
    #yield (' '.join(RandomWord() for _ in range(num_of_words)) + '.')

def RandomWord():
    chars = random.randrange(2, 10)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(chars))

def RandomTable(theSize):
    column_count = random.randrange(1,10)
    row_count = random.randrange(2,theSize)
    yield '<table>\r\n'
    #generate table head
    yield '\t<tr>\r\n\t\t'
    for _ in range(column_count):
        yield '<th>'
        yield RandomWord()
        yield '</th>\r\n'
    yield '\t</tr>'
    #fill in rows
    for _ in range(row_count-1):
        yield '\t<tr>\r\n\t\t'
        for _ in range(column_count):
            yield '<td>'
            yield str(random.randrange(0,50 * theSize))
            yield '</td>'
        yield '\r\n\t</tr>\r\n'
    yield '</table>\r\n'

def RandomOrderedList(theSize):
    list_length=random.randrange(1,theSize)
    yield '<ol>\r\n'
    for _ in range(list_length):
        yield '\t<li>'
        yield RandomWord()
        yield '</li>\r\n'
    yield '</ol>\r\n'

def RandomUnorderedList(theSize):
    list_length=random.randrange(1,theSize)
    yield '<ul>\r\n'
    for _ in range(list_length):
        yield '\t<li>'
        yield RandomWord()
        yield '</li>\r\n'
    yield '</ul>\r\n'

def RandomDiv(tree_height, count, max_depth, num_sibling_divs, max_headers, min_headers, theSize):
    numDivs = random.randint(1,num_sibling_divs)
    for i in range(0, numDivs):
        yield '<div id="a'+str(random.randrange(0,count[0]))+'">\r\n'
        yield RandomSection(count, max_depth, num_sibling_divs, tree_height, max_headers, min_headers)
        if tree_height > 0:
            treeHeight = random.randint(0, tree_height)
            if treeHeight > 0:
                yield RandomDiv(treeHeight - 1, count, max_depth, num_sibling_divs, max_headers, min_headers, theSize)
            
        yield '</div>'

def RandomSpan(count):
    yield '<span id="a'+str(random.randrange(0,count))+'">'
    yield RandomWord()
    yield '</span>'
    
def RandomCSS(count, super_random_css, theSize):
    global css
    fonts = ['Arial','Helvetica','Times New Roman','Times','Courier New','Courier','Verdana','Georgia','Palatino','Garamond','Bookman','Comic Sans MS','Trebuchet MS','Arial Black','Impact']
    font_style = ['normal', 'italic','oblique']
    font_weight = ['normal', 'bold']
    font_align = ['center', 'left']
    displayTypes = ['none', 'inline', 'block', 'inline-block']
    floatTypes = ['left', 'right', 'none', 'inherit']
    borderTypes = ['dotted', 'dashed', 'solid', 'double', 'groove']

    
    string_css = '<head>\r\n<style>\r\n'
    for x in range(count):
        r = lambda: random.randint(0,255)
        string_css += '#a'+str(x)+' {\r\n'
        string_css += 'color: #%02X%02X%02X' %(r(),r(),r())+';\r\n'
        string_css += 'font-family: '+fonts[random.randrange(0, len(fonts))]+';\r\n'
        string_css += 'font-size: '+str(random.randrange(10, 10 + theSize/2)) +'px;\r\n'
        string_css += 'font-style: '+font_style[random.randrange(0, len(font_style))]+';\r\n'
        string_css += 'font-weight: '+font_weight[random.randrange(0, len(font_weight))]+';\r\n'
        
        if super_random_css:
            string_css += 'display: ' + displayTypes[random.randint(0, 3)] + ';\r\n'
            string_css += 'background-color: rgb(' + str(random.randint(0, 255)) + ',' + str(random.randint(0, 255)) + ',' + str(random.randint(0, 255)) +');\r\n'
            string_css += 'float: ' + floatTypes[random.randint(0, 3)] + ';\r\n'
            string_css += 'padding: ' + str(random.randint(0, 10)) + 'px ' + str(random.randint(0, 10)) + 'px ' + str(random.randint(0, 10)) + 'px ' + str(random.randint(0, 10)) + 'px;\r\n'
            string_css += 'margin: ' + str(random.randint(0, 10)) + 'px ' + str(random.randint(0, 10)) + 'px ' + str(random.randint(0, 10)) + 'px ' + str(random.randint(0, 10)) + 'px;\r\n'
            string_css += 'border-width: ' + str(random.randint(0, 10)) + 'px ' + str(random.randint(0, 10)) + 'px ' + str(random.randint(0, 10)) + 'px ' + str(random.randint(0, 10)) + 'px;\r\n'
            string_css += 'border-style: ' + borderTypes[random.randint(0, 4)] + ';\r\n'
        
        string_css += 'text-align: '+font_align[random.randrange(0, len(font_align))]+';\r\n}\r\n'
         
    string_css += 'table,td,tr {border: 1px solid black;}'
    string_css += '\r\n</style>\r\n</head>\r\n'

    css = string_css

def Output(generator):
    global html
    if(isinstance(generator, str)):
        html = html+generator
    else:
        for g in generator: Output(g)
    
html = ''
css = ''

def main():
    global html, css
    
    if len(sys.argv) == 3:  
        simple = (sys.argv[1]).lower()
        size = (sys.argv[2]).lower()
        
        if ((simple == 'true' or simple == 'false') and (size == 'small' or size == 'medium' or size == 'large')):
            if simple == 'true':
                super_random_css = False
                depth = 1
                num_sibling_divs = 1
                max_tree_height = 0
                quirks_mode_possible = False
            elif simple == 'false':
                if size == 'small':
                    super_random_css = True
                    depth = 2
                    num_sibling_divs = 2
                    max_tree_height = 2
                    quirks_mode_possible = True
                else:
                    super_random_css = True
                    depth = 3
                    num_sibling_divs = 3
                    max_tree_height = 3
                    quirks_mode_possible = True
                
            if size == 'small': #was 4 and 2
                max_headers = 3
                min_headers = 2
                theSize = 6
            elif size == 'medium':
                max_headers = 11
                min_headers = 8
                theSize = 14
            elif size == 'large':
                max_headers = 18
                min_headers = 15
                theSize = 22
            
            Output(RandomHtml(depth, super_random_css, num_sibling_divs, max_tree_height, quirks_mode_possible, max_headers, min_headers, theSize))
            html = html.replace('RANDOMCSSCONTENTHERETOBEPLACED', css)
            
            #printing to screen as suggested by reviewers
            #output can now be easily saved as whatever name the user wants or easily output it to another tool
            print(html)
        else:
            print('Please input the correct arguments: simple(\'true\' or \'false\') and size(\'small\', \'medium\', \'large\')')
    else:
        print('Please input the correct number of arguments: simple(\'true\' or \'false\') and size(\'small\', \'medium\', \'large\')')


if __name__ == "__main__":
    main()
 