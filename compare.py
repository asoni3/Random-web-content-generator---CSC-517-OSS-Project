#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:45:26 2018

@author: Alexander
"""

#must install opencv, imutils, and scikit-image

from skimage.measure import compare_ssim 
import imutils
import cv2
import numpy as np
import sys
from pathlib import Path

def find_if_close(cnt1,cnt2):
    row1,row2 = cnt1.shape[0],cnt2.shape[0]
    for i in range(row1):
        for j in range(row2):
            dist = np.linalg.norm(cnt1[i]-cnt2[j])
            if abs(dist) < 50 :
                return True
            elif i==row1-1 and j==row2-1:
                return False

def compareImages(comparison_local_path, comparison_name, image1_local_path_and_name, image2_local_path_and_name):            
    image1 = image1_local_path_and_name
    image2 = image2_local_path_and_name
    
    file1 = Path(image1)
    file2 = Path(image2)
    output_path = Path(comparison_local_path)

    if not file1.exists():
        print('Image 1 does not exist')
    elif not file2.exists():
        print('Image 2 does not exist')
    elif not output_path.exists() and comparison_local_path != 'none' :
        print(comparison_local_path)
        print('Output Path does not exist')
    else:              
        imageA = cv2.imread(image1)
        imageB = cv2.imread(image2)
        
        if len(imageA) != len(imageB) or len(imageA[0]) != len(imageB[0]):
            print('Image Sizes don\'t match...')
        else:
            grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
            grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
            
            (score, diff) = compare_ssim(grayA, grayB, full=True)
            diff = (diff * 255).astype("uint8")
        
            print("Structural Similarity Index(SSIM): {}".format(score))
            
            thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if imutils.is_cv2() else cnts[1]
            
            md = 5
            rectangles = []
            for c in cnts:
                (x, y, w, h) = cv2.boundingRect(c)
                addTo = True
                
                for r in rectangles:
                    checker = False
                    if (x) >= (r[0] - md) and (x) <= (r[0] + r[2] + md) and (y) >= (r[1] - md) and (y) <= (r[1] + r[3] + md):
                        checker = True
                    elif (x) >= (r[0] - md) and (x) <= (r[0] + r[2] + md) and (y + h) >= (r[1] - md) and (y + h) <= (r[1] + r[3] + md):
                        checker = True
                    elif (x + w) >= (r[0] - md) and (x + w) <= (r[0] + r[2] + md) and (y) >= (r[1] - md) and (y) <= (r[1] + r[3] + md):
                        checker = True
                    elif (x + w) >= (r[0] - md) and (x + w) <= (r[0] + r[2] + md) and (y + h) >= (r[1] - md) and (y + h) <= (r[1] + r[3] + md):
                        checker = True
                    
                    if checker:
                        #merge
                        xMax = max((x + w),(r[0] + r[2]))
                        yMax = max((y + h),(r[1] + r[3]))
                        
                        r[0] = min(r[0], x)
                        r[1] = min(r[1], y)  
                        r[2] = xMax - r[0]
                        r[3] = yMax - r[1]
                        addTo = False
                        break
                if addTo:
                    rectangles.append([x, y, w, h])
                        
            changes = True
            newRectangles = []
            while changes:
                changes = False
                
                for rrr in rectangles:
                    x = rrr[0]
                    y = rrr[1]
                    w = rrr[2]
                    h = rrr[3]
                    
                    addTo = True
                    for r in newRectangles:
                        checker = False
                        if (x) >= (r[0] - md) and (x) <= (r[0] + r[2] + md) and (y) >= (r[1] - md) and (y) <= (r[1] + r[3] + md):
                            checker = True
                        elif (x) >= (r[0] - md) and (x) <= (r[0] + r[2] + md) and (y + h) >= (r[1] - md) and (y + h) <= (r[1] + r[3] + md):
                            checker = True
                        elif (x + w) >= (r[0] - md) and (x + w) <= (r[0] + r[2] + md) and (y) >= (r[1] - md) and (y) <= (r[1] + r[3] + md):
                            checker = True
                        elif (x + w) >= (r[0] - md) and (x + w) <= (r[0] + r[2] + md) and (y + h) >= (r[1] - md) and (y + h) <= (r[1] + r[3] + md):
                            checker = True
                        
                        if checker:
                            #merge
                            xMax = max((x + w),(r[0] + r[2]))
                            yMax = max((y + h),(r[1] + r[3]))
                            
                            r[0] = min(r[0], x)
                            r[1] = min(r[1], y)  
                            r[2] = xMax - r[0]
                            r[3] = yMax - r[1]
                            addTo = False
                            changes = True
                            break
                    if addTo:
                        newRectangles.append([x, y, w, h])
                
                rectangles = newRectangles[:]
                newRectangles = []
                
                rectangles.reverse()
                for rrr in rectangles:
                    x = rrr[0]
                    y = rrr[1]
                    w = rrr[2]
                    h = rrr[3]
                    
                    addTo = True
                    for r in newRectangles:
                        checker = False
                        if (x) >= (r[0] - md) and (x) <= (r[0] + r[2] + md) and (y) >= (r[1] - md) and (y) <= (r[1] + r[3] + md):
                            checker = True
                        elif (x) >= (r[0] - md) and (x) <= (r[0] + r[2] + md) and (y + h) >= (r[1] - md) and (y + h) <= (r[1] + r[3] + md):
                            checker = True
                        elif (x + w) >= (r[0] - md) and (x + w) <= (r[0] + r[2] + md) and (y) >= (r[1] - md) and (y) <= (r[1] + r[3] + md):
                            checker = True
                        elif (x + w) >= (r[0] - md) and (x + w) <= (r[0] + r[2] + md) and (y + h) >= (r[1] - md) and (y + h) <= (r[1] + r[3] + md):
                            checker = True
                        
                        if checker:
                            #merge
                            xMax = max((x + w),(r[0] + r[2]))
                            yMax = max((y + h),(r[1] + r[3]))
                            
                            r[0] = min(r[0], x)
                            r[1] = min(r[1], y)  
                            r[2] = xMax - r[0]
                            r[3] = yMax - r[1]
                            addTo = False
                            changes = True
                            break
                    if addTo:
                        newRectangles.append([x, y, w, h])
                
                rectangles = newRectangles[:]
                newRectangles = []
                
            for rrr in rectangles:
                x = rrr[0]
                y = rrr[1]
                w = rrr[2]
                h = rrr[3]
                
                cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
            
            if score != 1.0:
                checkExtension = comparison_name.find('.')
                if checkExtension > -1:
                    comparison_name = comparison_name[:checkExtension]
                    
                if comparison_local_path != 'none':
                    filename = comparison_local_path + comparison_name + '.png'
                else:
                    filename = comparison_name + '.png'
                    
                try:
                    cv2.imwrite(filename,imageA)
                except:
                    print('Cannot write comparison file...')

def main():
    if len(sys.argv) == 5:  
        output_path = sys.argv[1]
        if output_path.lower() == 'none':
            output_path = output_path.lower()
        
        output_name = sys.argv[2]
        f1 = sys.argv[3]
        f2 = sys.argv[4]
        
        if output_path[-1] != '/' and output_path != 'none':
            output_path = output_path + '/'
    
        compareImages(output_path, output_name, f1, f2)  

    else:
        print('Please input the correct number of arguments: output path (or \'none\' if no path), output filename, image1 - local path + name (with extension), image2 local path + name (with extension)')

if __name__ == "__main__":
    main()