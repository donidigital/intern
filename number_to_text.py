from curses.ascii import isalpha, isdigit

def numToWords(num,join=True):
    units = ['','bir','ikki','uch','to\'rt','besh','olti','yetti','sakkiz','to\'qqiz']
    teens = ['','o\'n_bir','o\'n_ikki','o\'n_uch','o\'n_to\'rt','o\'n_besh','o\'n_olti', 'o\'n_yetti','o\'n_sakkiz','o\'n_to\'qqiz']
    tens = ['','o\'n','yigirma','o\'ttiz','qirq','ellik','oltmish','yetmish', 'sakson','to\'qson']
    thousands = ['','ming','million','milliard','trillion','kvadrillion','kvintilion','sekstilion','septillion','oktilion', 'nonillion','dekillion','undekillion','duodekillion', 'tredekillion','quattuordekillion','sexdekillion', 'septendekillion','oktodekillion','novemdekillion', 'vigintillion', 'unvigintillion','duovigintillion', 'trevigintillion', 'quattourvigintillion' , 'quinvigintillion', 'hexvigintillion', 'septenvigintillion', 'octovigintillion', 'novemvigintillion', 'trigintillion', 'untrigintillion', 'duotrigintillion', 'googol']
    words = []
    if num==0: words.append('nol')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)
        groups = (numStrLen+2)//3
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = groups-(i//3+1)
            if h>=1:
                words.append(units[h])
                words.append('yuz')
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[g]+' ')
    if join: return ' '.join(words)
    return words

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
str1 = "men 1999-yilda  -3.6 va 3.6 ta olma 5.6  keyin 0.0 va 4 tug'ilganman 19-olma 0 "
list1 = str1.split()

for i in range(len(list1)):
    if list1[i].split('-')[0].isdigit() and (list1[i].isdigit() == False):
        kerak = list1[i].split('-')
        list1[i]  =  f"{numToWords(int(kerak[0]))}inchi {kerak[1]}"
def text_ichida(str_text):
    for i in range(len(str_text)):
        if str_text[i].split('-')[0].isdigit() and (str_text[i].isdigit() == False):
            kerak = str_text[i].split('-')
            str_text[i]  =  f"{numToWords(int(kerak[0]))}inchi {kerak[1]}"
        else:
            if list1[i].isdigit():
                list1[i] = numToWords(int(list1[i]))
            elif isfloat(str_text[i]):
                if float(str_text[i]) > 0:
                    list2 = str_text[i].split('.')
                    str_text[i] = f"{numToWords(int(list2[0]))} butun {numToWords(int(list2[1]))}"
                elif float(str_text[i]) < 0:
                    list2 = str_text[i][1:].split('.')
                    str_text[i] = f" minus {numToWords(int(list2[0]))} butun {numToWords(int(list2[1]))}"
                elif float(str_text[i]) == 0.0:
                    list2 = str_text[i].split('.')
                    str_text[i] = f"{numToWords(int(list2[0]))} butun {numToWords(int(list2[1]))}"
        
    return str_text
str2 = " ".join(text_ichida(list1))
print(str2)










