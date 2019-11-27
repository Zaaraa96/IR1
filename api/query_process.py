from hazm import Lemmatizer, Normalizer, word_tokenize
import re


def query_process(query):
    str = normalizer.normalize(query)
    str = str.translate(str.maketrans('_|ẖ–;،"…=$&@*-/:<>!+.()«»؟', '                          ',
                                                   '\u200c\u202c\u200f\u200e\u2069\u2067\u200b\u200d'))
    words = word_tokenize(str)
    words = list(dict.fromkeys(words))
    i = 0
    while i < len(words):
        internal_list = []
        while True:
            if i >= len(words): break
            repeat = False
            word = words[i]
            lem_word = lemmatizer.lemmatize(word).split('#')[0]
            if lem_word == '':
                lem_word = 'است'
            if word in stopwords or lem_word in stopwords:
                words.remove(word)
                repeat = True
            if repeat == False:
                break
        lem_words = [lem_word]
        for k in range(len(samewords)):
            if lem_words[0] in samewords[k]:
                samewords[k].remove(lem_words[0])
                lem_words = lem_words + samewords[k]
                samewords[k] =  samewords[k] + [lem_words[0]]
                print(samewords[k])
                break

        words[i] = lem_words
        i = i + 1
    return words


stopwords_f = open('stop_words.txt', 'r', encoding='utf-8')
stopwords = stopwords_f.readlines()
for i in range(len(stopwords)):
    stopwords[i] = stopwords[i].replace("\n", "")
samewords_f = open('same_words.txt', 'r', encoding='utf-8')
samewords = samewords_f.readlines()
#samewords_tokens = word_tokenize(samewords_f.read(),"\n")
for i in range(len(samewords)):
    samewords[i] = samewords[i].replace("\n", "")
    samewords[i] = word_tokenize(samewords[i])
print('same=' + str(samewords))
samewords_f.close()
stopwords_f.close()
print('stop='+str(stopwords))

lemmatizer = Lemmatizer()
normalizer = Normalizer()
print(query_process("ما تو را بچه کتابهای به برای دوست داریم خودرو را هنوز اتومبیل"))