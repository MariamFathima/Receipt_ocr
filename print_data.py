import cv2
import os
import re
import pytesseract
from matplotlib import pyplot as plt
from datetime import datetime

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('./Receipts/') if isfile(join('./Receipts/', f))]

dates = []
count =0
for file in onlyfiles:
    img = cv2.imread("./Receipts/"+file)
    text1 = pytesseract.image_to_string(img, config='-l eng --oem 1 --psm 3')
    exprs = [r'\d{2}\s*/\s*\w*\s*/\s*\d{4}',r'\d{2}\s*-\s*\w*\s*-\s*\d{4}',r'\d{2}\s*\.\s*\w*\s*\.\s*\d{4}',r'\w*\s*\d{2}\s*\,\s*\d{4}','\w*\s*\d{2}\s*\'\s*\d{2}',r'\d{1}\s*/\s*\w*\s*/\s*\d{4}']
    for expr in exprs:
        match = re.search(expr, text1)
        if(match):
            dates.append(match.group())
    count+=1
len(dates)
print(count)
print(dates)
print((len(dates)/count)*100)