import nltk


import glob
import os.path
from xml.etree import ElementTree

## Remove stop words
a = open("C:/Users/HP/pycharmprojects/ontologie/newtext.txt", "r", encoding = 'utf-8')
raw = a.read()
raw1 = raw
words = raw.split()
c = open("C:/Users/HP/Documents/motvide.txt", "r", encoding = 'utf-8')
line = c.read()
ll = line.split()
for word in words:
    for word1 in ll:
        if word1 == word:
            word2 = " " + word1 + " "
            raw1 = raw1.replace(word2, ' ')

tt = open('text.txt', 'w', encoding = 'utf-8')
tt.write(raw1)
tt.close()
## stop words removed

# from nltk import word_tokenize

# from nltk.stem.isri import ISRIStemmer

# st = ISRIStemmer()
# b = open("C:/Users/HP/pycharmprojects/ontologie/newtext.txt", "r", encoding = 'utf-8')
#raw = b.read()
#word = raw.split()
#w = " البحث العلمي أو البحث أو التجربة التنموية هو أسلوب منظم في جمع المعلومات الموثوقة " \
#   "وتدوين الملاحظات والتحليل الموضوعي لتلك المعلومات باتباع أساليب ومناهج علمية محددة بقصد التأكد من صحتها أو تعديلها " \
#   "أو إضافة الجديد لها، ومن ثم التوصل إلى بعض القوانين والنظريات والتنبؤ بحدوث مثل هذه الظواهر والتحكم في أسبابها"

#for a in word_tokenize(word):

#    print(st.stem(a))
# b = open("C:/Users/HP/Documents/prefixes.txt", "r", encoding = 'utf-8')
# raw1 = b.read()
# word1 = raw1.split()
# for words in word:
#   for words1 in word1:
#       if words.startswith(words1):
#           aa = words.replace(words1, " ")
#           print (aa)
#           break

# tt = open('textcleaning.txt', 'w', encoding = 'utf-8')
# chn = " ".join(word)
# tt.write(chn)
# tt.close()





# h = open("C:/Users/HP/Documents/prefixes.txt", "r", encoding = 'utf-8')
# raw1 = h.read()
# b = open("C:/Users/HP/Documents/prefixes.txt", "r", encoding = 'utf-8')
# raw2 = b.read()



## for extract relation

# import lxml

# from lxml import etree

# realation = etree.parse("C:/Users/HP/Documents/relation.xml")
# for type_rel in realation.xpath("/type_relations/type_relation/indicateur"):
#     print(type_rel.text)
## end relation

