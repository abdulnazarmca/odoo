# -*- coding: utf-8 -*-
import logging
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

#-------------------------------------------------------------
#English Number to Arabic Number
#-------------------------------------------------------------

n0 = '٠'
n1 = '١'
n2 = '٢'
n3 = '٣'
n4 = '٤'
n5 = '٥'
n6 = '٦'
n7 = '٧'
n8 = '٨'
n9 = '٩'
arnumber = (n0, n1, n2, n3, n4, n5, n6, n7, n8, n9)

def number_convert(word):
    res = ''
    for v in range(len(word)):
        if word[v] == ',':
            res += word[v]
        else:
            res += arnumber[int(word[v])]
    return res

def split_amount(amount):
    list = str(amount).split('.')
    start_word = list[0]
    end_word = list[1]
    return start_word, end_word


def ennotoarno(amount):
    start_word, end_word = split_amount(amount)
    res = number_convert(start_word) + '/' + number_convert(end_word)
    return res


#-------------------------------------------------------------
#Number to String
#-------------------------------------------------------------

#individual = [degit number 1.2.3....... less then <10]
individual = [u"صفر", u"واحد", u"إثنان", u"ثلاثة", u"أربعة", u"خمسة", u"ستة", u"سبعة", u"ثمانية", u"تسعة"]

#tens = [u"10   ", u"20    ", u"30   ", u"40   ", u"50    ", u"60   ", u"70   ", u"80   ", u"90     "]
tens = [u"عشرة", u"عشرون", u"ثلاثون", u"أربعون", u"خمسون", u"ستون", u"سبعون", u"ثمانون", u"تسعون"]

#teens = [u"11    ", u" 12    ", u"13     ", u"14       ", u"15        ", u"16      ", u"17      ", u"18       ", u"19       "]
teens = [u"أحد عشر", u"إثنا عشر", u"ثلاثة عشر", u"أربعة عشر", u"خمسة عشر", u"ستة عشر", u"سبعة عشر", u"ثمانية عشر", u"تسعة عشر"]

#handreds = [u"100", u"200 ", u"300  ", u"400   ", u"500    ", u"600   ", u"700   ", u"800   ", u"900   "]
handreds = [u"مائة", u"مائتان", u"ثلاثمائة", u"أربعمائة", u"خمسمائة", u"ستمائة", u"سبعمائة", u"ثمانمائة", u"تسعمائة"]
biger = [u"", u"ألف", u"مليون", u"مليار", u"بليون", u"بليار", u"تريليون", u"تريليار",
         u"كتريلليون", u"كتريليار", u"سنكلليون", u"سنكليار", u"سيزليون", u"سيزليار", 
         u"سيتيليون", u"سيتليار", u"ويتيليون", u"ويتيليار"]


        
       
def split_number(number):
    list_fin = []
    n = len(str(number))
    list_number = list(str(number))
    d = []
    for a in range(n):
        v = list_number.pop(-1)
        if len(d) < 3 and len(list_number) > 0:
            d.insert(0, v)
        elif len(d) < 3 and len(list_number) == 0:
            d.insert(0, v)
            s = ''.join(d)
            list_fin.append(s)
        elif len(d) == 3 and len(list_number) > 0:
            s = ''.join(d)
            list_fin.append(s)
            d = []
            d.insert(0, v)
        elif len(d) == 3 and len(list_number) == 0:
            s = ''.join(d)
            list_fin.append(s)
            d = []
            d.insert(0, v)
            s = ''.join(d)
            list_fin.append(s)
    return list_fin
    
    
def set_tamiiz(txt, n, i):
    text = txt
    if i != 1:
        if n == 1 : 
            text = biger[i-1]
        elif n == 2 : 
            text = biger[i-1]+u'انِ'
        elif n == 4 : 
            text = txt+u' '+biger[i-1]+u'اً'
        elif n == 3 : 
            if i == 2:
                text = txt+u' آلافٍ'
            elif i == 3:
                text = txt+u' ملايينٍ'
            else:
                text = txt+u' '+biger[i-1]+u'اتٍ'
        elif n == 5 :
            if txt == u'مائتان':  txt = u'مائتا'
            text = txt+u' '+biger[i-1]+u'ٍ'
    return text  
        
         
def convert_tens(level, i):
    if int(level) == 0:
        txt = u''
    elif int(level) == 1:
        txt = set_tamiiz(individual[1], 1, i)
    elif int(level) == 2:
        txt = set_tamiiz(individual[2], 2, i)
    elif int(level) == 10:
        txt = set_tamiiz(tens[0], 3, i)
    elif int(level)%10 == 0:
        txt = set_tamiiz(tens[(int(level)/10)-1], 4, i)
    elif int(level) < 10:
        txt = set_tamiiz(individual[int(level[1])], 3, i)
    elif int(level) < 20:
        txt = set_tamiiz(teens[int(level)-11], 4, i)
    else:
        txt1 = individual[int(level[1])]
        txt2 = set_tamiiz(tens[(int(level)/10)-1], 4, i)
        txt = txt1+u' و'+txt2
    return txt
        
             
def convert_handreds(level, i): 
    if int(level[0]) == 0:
        txt1 = u''
    else:
        txt1 = handreds[int(level[0])-1]
    txt2 = convert_tens(level[1:], i)
    if txt1 == u'' and txt2 == u'':
        txt = u''
    elif txt1 == u'':
        txt = txt2
    elif txt2 == u'':
        txt = set_tamiiz(txt1, 5, i)
    else:
        txt = txt1+u' و'+txt2
    return txt
        
              
def convert_to_text(level, i, l): 
    if len(level) == 1:
        if int(level) == 1:
            txt = set_tamiiz(individual[1], 1, l-i)
        elif int(level) == 2:
            txt = set_tamiiz(individual[2], 2, l-i)
        else:
            txt = set_tamiiz(individual[int(level)], 3, l-i)
    elif len(level) == 2:
        txt = convert_tens(level, l-i)
    else:
        txt = convert_handreds(level, l-i)
    return txt
            
        
      
def take_number(number):
    new_text = ''
    if number:
        new_int = int(number)
        list_number = split_number(new_int)
        list_number.reverse()
        new_list = []
        a = 0
        for level in list_number:
            txt = convert_to_text(level, a, len(list_number))
            a += 1
            if txt != u'':
                new_list.append(txt)
        new_text = u' و'.join(new_list)
    return new_text

#-------------------------------------------------------------
#Number to String main
#-------------------------------------------------------------

def amount_to_text_ar(number, currency):
    number = '%.2f' % number
    units_name = currency.name_before_decimal
    list = str(number).split('.')
    start_word = take_number(int(list[0]))
    end_word = take_number(int(list[1]))
    amount_number = int(list[1])
    amount_name = (amount_number > 1) and currency.name_after_decimal or currency.name_after_decimal
    amount_name = (amount_number <> 0) and amount_name or ''
    return ' '.join(filter(None, [start_word, units_name, (start_word or units_name) and (end_word or amount_name) and u' و ', end_word, amount_name]))







#-------------------------------------------------------------
# Generic functions
#-------------------------------------------------------------

_translate_funcs = {'ar' : amount_to_text_ar}
    
#TODO: we should use the country AND language (ex: septante VS soixante dix)
#TODO: we should use ar by default, but the translation func is yet to be implemented
def amount_to_text_ar(nbr, lang='ar', currency=u' ريال '):

    import openerp.loglevels as loglevels
#    if nbr > 10000000:
#        _logger.warning(_("Number too large '%d', can not translate it"))
#        return str(nbr)
    
    if not _translate_funcs.has_key(lang):
        _logger.warning(_("no translation function found for lang: '%s'"), lang)
        #TODO: (default should be en) same as above
        lang = 'ar'
    return _translate_funcs[lang](abs(nbr), currency)

if __name__=='__main__':
    from sys import argv
    
    lang = 'nl'
    if len(argv) < 2:
        for i in range(1,200):
            print i, ">>", int_to_text(i, lang)
        for i in range(200,999999,139):
            print i, ">>", int_to_text(i, lang)
    else:
        print int_to_text(int(argv[1]), lang)



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
