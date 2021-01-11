# !/usr/bin/python
# encoding: utf-8


import nltk


nltk.download('punkt')

##filtred concepts
b = ""
file = open("newconcepts.txt", "w", encoding = 'utf-8')

x = open("C:/Users/HP/pycharmprojects/ontologie/conceptsss.txt", "r", encoding = 'utf-8')
raw = x.read()
words = raw.split('\n')
for s in words:
    if len(s) > 2:
        b = b + s + "\n"
file.write(b)
file.close()





# trigram generation

nltk.download('punkt')
b = open("C:/Users/HP/Documents/pizza.txt", "r", encoding = 'utf-16LE')
raw = b.read()
tokens = nltk.word_tokenize(raw)
# Create your bigrams
bgs = nltk.trigrams(tokens)

# compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)

for k, v in fdist.items():
    if v > 2:
        print(k, v)
    print(k, v)


# biGrams et distributions de fréquence


nltk.download('punkt')
a = open("C:/Users/HP/Documents/pizza.txt", "r", encoding = 'utf-16LE')
raw = a.read()
tokens = nltk.word_tokenize(raw)
# Create your bigrams
bgs = nltk.bigrams(tokens)

# compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
for k, v in fdist.items():
    if v > 2:
        print(k, v)
    print(k, v)

# frequency of words

# def word_count(filename):
#     with open(filename) as f:
#        return Counter(f.read().split())
# c = open("C:/Users/HP/Documents/pizza.txt", "r", encoding = 'utf-16LE')

# counter = word_count(c)
# for i in counter:
#   print(i, ':', counter[i])


# reding my corpus
# Corpus = open("C:/Users/HP/Documents/pizza.txt", "r", encoding = 'utf-16LE')
# print((Corpus.read()))


# find common word
# words = re.findall(r'\w+', open("C:/Users/HP/Documents/pizza.txt", encoding = 'utf-16LE').read().lower())
# count = counter.most_common(20)
# print(count)
