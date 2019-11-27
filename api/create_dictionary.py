from hazm import Lemmatizer, Normalizer, word_tokenize
import xlrd
import re


def isdigit(word):
    return (word[0] in ['۹','۸','۷','۶','۵','۴','۳','۲','۱','۰'])

def create_dictionary_from_text(i, str):
    str = normalizer.normalize(str)
    str_for_tokenize = str.translate(str.maketrans('_|ẖ–;،"…=$&@*-/:<>!+.()«»؟', '                          ',
                                                   '\u200c\u202c\u200f\u200e\u2069\u2067\u200b\u200d'))
    words = word_tokenize(str_for_tokenize)
    # print('main words = ')
    # print(words)
    new_dict = {}
    k = 0
    while k < len(words):
        while True:
            if k >= len(words): break
            repeat = False
            word = words[k]
            # list_of_positions = [m.start() for m in re.finditer(word, str)]
            lem_word = lemmatizer.lemmatize(word).split('#')[0]
            if lem_word == '':
                lem_word = 'است'
            if word in stopwords or lem_word in stopwords or isdigit(word):
                words.remove(word)
                repeat = True
            else:
                words[k] = lem_word
                break
        if k >= len(words): break
        k = k + 1
    # print('after process = ')
    # print(words)
    for k in range(len(words)):
        list_of_positions = [x for x, y in enumerate(words) if y == words[k]]
        new_dict[words[k]] = [{i: list_of_positions}]

    sorted_dict = {}
    for i in sorted(new_dict):
        sorted_dict[i] = new_dict[i]
    return sorted_dict


def normalize_content_and_create_dict(i, str):
    result = ''
    for word in str:
        if not re.match(r'[A-Z]+', word, re.I):
            result = result + word
    return create_dictionary_from_text(i, result)


def merge_dicts(d):
    if len(d) == 0:
        return d
    new_dict = d[0]
    for i in range(1, len(d)):
        for word in d[i]:
            if word in new_dict.keys():
                posting_list = new_dict[word]
                posting_list = posting_list + d[i][word]
                new_dict[word] = posting_list
            else:
                new_dict[word] = d[i][word]
    sorted_dict = {}
    for i in sorted(new_dict):
        sorted_dict[i] = new_dict[i]
    return sorted_dict


stopwords_f = open('stop_words.txt', 'r', encoding='utf-8')
stopwords = stopwords_f.readlines()
for i in range(len(stopwords)):
    stopwords[i] = stopwords[i].replace("\n", "")
stopwords_f.close()
wb = xlrd.open_workbook("IR-F19-Project01-Input.xlsx")
sheet = wb.sheet_by_index(0)
lemmatizer = Lemmatizer()
normalizer = Normalizer()
# nim faseleha va alaeme negareshi ro dorost mikone fasele inashuno, "ha" ro michasboone ba nim fasele, vali ghalat emlayi na

# lemmatizer behtar ast tanha be kar ravad chon stemmer feel hara xarab mikonad vali alamate jam ra
## ham hazf mitavanad bokonad va baazan shenase ra ham hazf mikonad

title_Dicts = []
summary_Dicts = []
content_Dicts = []
for i in range(1, sheet.nrows):
    title_Dicts.append(create_dictionary_from_text(i, sheet.cell_value(i, 1)))
    summary_Dicts.append(create_dictionary_from_text(i, sheet.cell_value(i, 3)))
    content_Dicts.append(normalize_content_and_create_dict(i, sheet.cell_value(i, 5)))

f_t = open("title_dict.txt", "w", encoding='utf-8')
f_s = open("summary_dict.txt", "w", encoding='utf-8')
f_c = open("content_dict.txt", "w", encoding='utf-8')
f_t.write(str(merge_dicts(title_Dicts)))
f_s.write(str(merge_dicts(summary_Dicts)))
f_c.write(str(merge_dicts(content_Dicts)))
f_t.close()
f_s.close()
f_c.close()
f = open('title_dict.txt', 'r', encoding='utf-8')
print(f.read())
