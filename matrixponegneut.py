# !/usr/bin/python
# -*- coding: utf-8 -*-
from numpy import *
from owlready2 import *

# a = open("C:/Users/HP/pycharmprojects/ontologie/text.txt", "r", encoding = 'utf-8')
# raw = a.readlines()
# words = raw.split()
# with open("C:/Users/HP/pycharmprojects/ontologie/text.txt", "r", encoding = 'utf-8') as f:
#    i = 0
#    for line in f:
#        y = line.split()
#        i = i + 1
#        h = str(i) + '\t' + line
#        print(y)
onto = get_ontology("file://C:/Users/HP/Desktop/memoire/restaurantonto.owl").load()
print(list(onto.classes()))
print(list(onto.individuals()))
print(list(onto.object_properties()))


construct = str(list(onto.اكل.constructs()))
construct = construct.replace('restaurantonto.', '')
construct = construct.replace('[', '')
construct = construct.replace(']', '')
print(construct.split(','))
# print(list(onto.اكل.get_class_properties()))

# print(list(onto.اكل.constructs()))
# get object property of akel's class

constructeur = list(onto.اكل.constructs())[0]
print(construct.split(','), onto.اكل.get_class_properties(), constructeur.subclasses())

constru = str(list(onto.طلب.constructs()))
constru = constru.replace('restaurantonto.', '')
constru = constru.replace('[', '')
constru = constru.replace(']', '')
print(constru.split(','))
cons = list(onto.طلب.constructs())[0]
print(constru.split(','), onto.طلب.get_class_properties(), cons.subclasses())

# print(constructeur.subclasses())
#  displays each GO concept with its parent classe
with onto:
    for onto_concept in onto.classes():
        print(onto_concept)
    for parent in onto_concept.is_a:
        print(" is a %s" % parent)

for onto_objectproperty in onto.اكل.get_class_properties():
    print(onto_objectproperty)

m = str(onto.search(is_a = onto.اكل))
m = m.replace('restaurantonto.', '')
m = m.replace('10.', '')
m = m.replace('[', '')
m = m.replace(']', '')
m = m.replace('_', " ")
print(m.split(','))

# f = str(onto.search(is_a = onto.وجبه))
# f = f.replace('10.', '')
# print(f.split(','))

n = str(onto.search(is_a = onto.خدمه))
n = n.replace('restaurantonto.', '')
n = n.replace('10.', '')
n = n.replace('[', '')
n = n.replace('_', " ")
n = n.replace(']', '')
print(n.split(','))

o = str(onto.search(is_a = onto.فلوس))
o = o.replace('restaurantonto.', '')
o = o.replace('10.', '')
o = o.replace('[', '')
o = o.replace(']', '')
print(o.split(','))

p = str(onto.search(is_a = onto.طلب))
p = p.replace('restaurantonto.', '')
p = p.replace('[', '')
p = p.replace(']', '')
print(p.split(','))

g = str(onto.search(is_a = onto.مدينه))
g = g.replace('restaurantonto.', '')
g = g.replace('10.', '')
g = g.replace('[', '')
g = g.replace(']', '')
print(g.split(','))

q = str(onto.search(is_a = onto.وقت))
q = q.replace('restaurantonto.', '')
q = q.replace('[', '')
q = q.replace(']', '')
print(q.split(','))

d = str(onto.search(is_a = onto.مطعم))
d = d.replace('restaurantonto.', '')
d = d.replace('10.', '')
d = d.replace('[', '')
d = d.replace(']', '')
d = d.replace('_', " ")
print(d.split(','))


print(["سلبي"])
# print(onto.search(type = onto.concept_negative))
z = str(onto.search(type = onto.سلبي))
a = z.replace('restaurantonto.', '')
a = a.replace('10.', '')
a = a.replace('[', '')
a = a.replace(']', '')
a = a.replace('_', " ")
print(a.split(','))
# print(a.strip("."))

print(["محايد"])
# print(onto.search(type = onto.concept_neutre))
s = str(onto.search(type = onto.محايد))
b = s.replace('restaurantonto.', ' ')
b = b.replace('[', '')
b = b.replace(']', '')
print(b.split(','))
print(["ايجابي"])
# print(onto.search(type = onto.concept_positive))
x = str(onto.search(type = onto.ايجابي))
c = x.replace('restaurantonto.', ' ')
c = c.replace('10.', '')
c = c.replace('[', '')
c = c.replace(']', '')
print(c.split(','))

with open("C:/Users/HP/pycharmprojects/ontologie/text.txt", "r", encoding = 'utf-8') as ins:
    tab = []
    for line in ins:
        tab.append(line)
tab = array(tab)
print(tab)
print(tab[0])

# sujet = ''
for i in range(len(tab)):
    countneg = 0
    countpos = 0
    countneut = 0


    for item in str(tab[i]).split():
        for j in a.split():
            if j.replace(',', '') == item:
                countneg = countneg + 1


        for k in b.split():
            if k.replace(',', '') == item:
                countneut = countneut + 1

        for h in c.split():
            if h.replace(',', '') == item:
                countpos = countpos + 1

    if countneg > countpos and countneg > countneut:
        print(tab[i].split(), 'negative')
    elif countpos > countneg and countpos > countneut:
        print(tab[i].split(), 'positive')
    elif countneg == countpos:
        print(tab[i].split(), 'neutre')
    else:
        print(tab[i].split(), 'neutre')




#    if countneg > countpos and countneg > countneut:
#            print(tab[i].split(), 'negative')
#    elif countpos > countneg and countpos > countneut:
#            print(tab[i].split(), 'positive')
#    elif countneg == countpos:
#            print(tab[i].split(), 'neutre')
#    else:
#            print(tab[i].split(), 'neutre')


#    IF conteurneg>conteurPOS>conteurnEUTRE



#    if



 #       if raw.count(a)

#        if words.count(words.positive) > word.count(words) and word.count(words.positive) > word.count\
#                    (words):
#            print('positive')
#        elif word.count(words.text) > word.count(words.text) and word.count(words.text) > word.count\
#                    (words.neutre):
#            print('negative')
#        else:
#            print('neutre')

 #       if words == onto.classes() and words in onto.concept_negative:
 #           print(raw, 'negative')
 #       elif words == onto.classes() and words in onto.concept_positive:
 #           print(raw, 'positive')
 #       else:
 #           print(raw, 'neutre')
