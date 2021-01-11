import nltk
from nltk import ngrams

nltk.download('punkt')
## frequence des mots à partir de text

a = open("C:/Users/HP/pycharmprojects/ontologie/text.txt", "r", encoding = 'utf-8')
raw = a.read()
tokens = nltk.word_tokenize(raw)
# Create your bigrams
bgs = nltk.bigrams(tokens)
# compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
# var = sorted(fdist, key = fdist.__getitem__, reverse=True)[0:]
# print(var)
for k, v in fdist.items():
#    print(k, v)
    if v >= 7:
        print(k, v)

n = 1
ungrams = ngrams(raw.split(), n)
fdist = nltk.FreqDist(ungrams)
# gives the top 10 (plus courants) words used in the text
# var = sorted(fdist, key = fdist.__getitem__, reverse=True)[0:10]
# print(var)
#
for k, v in fdist.items():
    if v >= 80:
        print(k, v)
# tt.write()
# tt.close()
