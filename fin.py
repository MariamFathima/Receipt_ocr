def tess(image):
    import cv2
    import os
    import re
    import pytesseract
    from datetime import datetime

    img = cv2.imread(image,0)
    text1 = pytesseract.image_to_string(img, config='-l eng --oem 1 --psm 3')
    exprs = [r'\d{2}\s*/\s*\w*\s*/\s*\d{4}',r'\d{2}\s*-\s*\w*\s*-\s*\d{4}',r'\d{2}\s*\.\s*\w*\s*\.\s*\d{4}',r'\w*\s*\d{2}\s*\,\s*\d{4}','\w*\s*\d{2}\s*\'\s*\d{2}',r'\d{1}\s*/\s*\w*\s*/\s*\d{4}']
    for expr in exprs:
        match = re.search(expr, text1)
        if(match):
            dates = (match.group())
        else:
            print('null')


    def dateParser(date):
        months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        month = 0
        day = 0
        year = 0
        if(re.search(r"\w*\s*\d*\s*,\s*\d{4}",date)):
            match = re.search(r'\w*[a-zA-Z]',date)
            if(match):
                for i, m in enumerate(months):
                    if(m[:3].lower() == match.group()[:3].lower()):
                        month = i+1
            if(date[-4:][:1] == '2'):
                year = date[-4:]
            match = re.search(r"\d{2}",date[:-4])
            if(match):
                day = match.group()
        if(day and month and year):
            return [day,month,year]
        else:
            return False

    try: return datetime.strptime(dates, '%d-%m-%Y').strftime("%m/%d/%Y")
    except: pass
    try: return datetime.strptime(dates, '%d-%m-%Y').strftime("%m/%d/%Y")
    except: pass
    try: return datetime.strptime(dates, '%d/%b/%Y').strftime("%m/%d/%Y")
    except: pass
    try : return datetime.strptime(dates, '%d-%b-%Y').strftime("%m/%d/%Y")
    except: pass
    try: return dateParser('Sep 29, 2018') # returns ['29', 9, '2018']
    except: return ("null")