import flask
from flask import request, jsonify
from flask_cors import CORS

import pandas as pd
df1 =pd.read_excel("IR-F19-Project01-Input.xlsx") 
import json
d = df1.to_dict(orient='records') #use this, it doesnt convert it to anything
j= json.dumps(d,ensure_ascii=False)
document=[]

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

from hazm import Lemmatizer, Normalizer, word_tokenize

def query_process(query):
    str = normalizer.normalize(query)
    str = str.translate(str.maketrans('_|ẖ–;،"…=$&@*-/:<>!+.()«»٪؟', '                           ',
                                                   '\u200c\u202c\u200f\u200e\u2069\u2067\u200b\u200d'))
    words = word_tokenize(str)
    words = list(dict.fromkeys(words))
    i = 0
    while i < len(words):
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

        for t in range(len(samewords)):
            if lem_word in samewords[t]:
                lem_word = samewords[t][0]
                break

        words[i] = lem_word
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
#print('same=' + str(samewords))
samewords_f.close()
stopwords_f.close()
#print('stop='+str(stopwords))

lemmatizer = Lemmatizer()
normalizer = Normalizer()
#print(query_process("ما تو را کودک،. کتابهای به برای دوست داریم خودرو را هنوز اتومبیل"))


@app.route('/api/dataframe', methods=['GET'])
def df():
    return j

def find_in_dictionary(word,dictionary1):
    if word in dictionary1:
        return dictionary1[word].copy()#returns a list of docIDs with where the term is
    else:
        return []


 


def find_the_same_docIDs(list1,list2):
    list11=[]
    for docID in list1:
                for key in docID.keys(): 
                    list11.append(key)
    list22=[]
    for docID in list2:
                for key in docID.keys(): 
                    list22.append(key)
    same=[]
    same=list(set(list11).intersection(set(list22)))
    return same#list of shared documents

def find_position_in_list(list1,i):
    list1_positions_i=[]
    for j in range(0, len(list1)):
        dic=list1[j]
        if i in dic:
            return dic[i].copy()


def search_in_inputarrlist_items(sentence,dictionary): #at the end it would return a list
    list_of_documents_for_terms=[]
    #not sure about this: if sentece is a list(its ok) o.w make it(it is a string then) a list by:
    #sentence= list(sentence.split(" "))
    for term in sentence:#each term is a string(word)
        docIDs= find_in_dictionary(term,dictionary) #this is docIDs with positions
        if docIDs:
            list_of_documents_for_terms.append(docIDs)
        else:
            return []#if one is empty all would be empty

    list1= list_of_documents_for_terms[0]
    #check others with this one, one by one and update this list as going on
    for k in range(1,len(list_of_documents_for_terms)):
        list2= list_of_documents_for_terms[k]
        same= find_the_same_docIDs(list1,list2)
        if same:
            list1_new=[]
            for i in same:
                list1_positions_i=find_position_in_list(list1,i)
                for j in range(0,len(list1_positions_i)):
                    list1_positions_i[j]=list1_positions_i[j]+1
                list2_positions_i=find_position_in_list(list2,i)
                insect=[]
                list_new={}
                insect=list(set(list1_positions_i).intersection(set(list2_positions_i)))
                if insect:
                    list_new.update( {i : insect} )
                #if insect is mpty, the intersection is empty so we delete this part completely 
                list1_new.append(list_new)
                ###############
            list1= list1_new.copy()
        else:
            return []
    #list1 now has docIDs we need and we have to return the docIDs as a list
    doc_list=[]
    for t in range(0,len(list1)):
        q= list1[t]
        q1= q.keys()
        doc_list.extend(q1)
    return doc_list.copy()


def search_in_inputarrlist(inputarrlist,dictionary):
    if (len(inputarrlist)==0):
        return []
    list_of_documents=[]
    for sentence in inputarrlist:
        list1= search_in_inputarrlist_items(sentence,dictionary)
        if list1:
            list_of_documents.append(list1)
        else: 
            return []
    list1= list_of_documents[0]
    for i in range(1,len(list_of_documents)):
        list2=list_of_documents[i]
        list1= list(set(list1).intersection(set(list2)))
    return list1  


def search_in_inputarr(inputarr,dictionary):
    if (len(inputarr)==0):
        return []
    list_of_documents_for_terms=[]
    for term in inputarr:#each term is a string(word)
        docIDs= find_in_dictionary(term,dictionary) #this is docIDs with positions; since it is not needed, we get rid of it
        list1=[]
        if docIDs:#if docIDs is not empty
            for docID in docIDs:
                #print(docID)
                for key in docID.keys(): 
                    list1.append(key)
                #print(list1)
        else:#if one docID is empty, it makes the whole answer empty
            return []
        list_of_documents_for_terms.append(list1)
        
    #find insection of docIDs between terms
    if list_of_documents_for_terms:
        list1= list_of_documents_for_terms[0]
    for i in range(1,len(list_of_documents_for_terms)):
        list2=list_of_documents_for_terms[i]
        list1= list(set(list1).intersection(set(list2)))
    return list1

def search_in_not(notin,dictionary):
    if (len(notin)==0):
        return []
    list_of_documents_for_terms=[]
    for term in notin:#each term is a string(word)
        docIDs= find_in_dictionary(term,dictionary) #this is docIDs with positions; since it is not needed, we get rid of it
        list1=[]
        if docIDs:#if docIDs is not empty
            for docID in docIDs:
                for key in docID.keys(): 
                    list1.append(key)
        list_of_documents_for_terms.extend(list1)
    list_of_documents_for_terms=list(set(list_of_documents_for_terms))
    return list_of_documents_for_terms.copy()


@app.route('/api/search', methods=['POST'])
def search():
    #get word and dictionary and search in it; response is a list of docIDs with where the word is
    #for each word call find_in_dictionary(word,dictionary)
    #if returned list!=[] then...
    
    import ast
    dictionary={}
    dictionary2={}
    dictionary3={}
    f=open('title_dict.txt','r',encoding='utf-8')
    f2=open('summary_dict.txt','r',encoding='utf-8')
    f3=open('content_dict.txt','r',encoding='utf-8')
    dictionary=f.read();
    dictionary2=f2.read();
    dictionary3=f3.read();
    dictionary=ast.literal_eval(dictionary)
    dictionary2=ast.literal_eval(dictionary2)
    dictionary3=ast.literal_eval(dictionary3)
    query=request.get_json()
    inputarrlist=query["list"]
    #print(query)
    q=[]
    for input1 in inputarrlist:
        #query_process returns a list
        #maybe we should bring query_process to search functions?
        q.append(query_process(input1))
    inputarrlist=q.copy()
    #call search function in inputarrlist with the desired dictionary
    documentlist1= search_in_inputarrlist(inputarrlist,dictionary) 
    documentlist12= search_in_inputarrlist(inputarrlist,dictionary2)
    documentlist13= search_in_inputarrlist(inputarrlist,dictionary3)
    
    
    q=[]
    inputarr=query["words"]
    #print(inputarr)
    ttt=[]
    for input1 in inputarr:
        #print(input1)
        ttt.append(query_process(input1)[0])
    #print(inputarr)
    #call search function in inputarr with the desired dictionary
    documentlist2= search_in_inputarr(ttt,dictionary)    #returns only documentIDs as a list
    documentlist22= search_in_inputarr(ttt,dictionary2)
    documentlist23= search_in_inputarr(ttt,dictionary3)
    #print(documentlist2)
    #inputarr=query_process(inputarr)
    notin=query["notin"]
    
    q=[]
    for input1 in notin:
        #query_process returns a list
        q.append(query_process(input1)[0])
    
    #print("**",q)
    documentlist3= search_in_not(q,dictionary)
    documentlist32= search_in_not(q,dictionary2)
    documentlist33= search_in_not(q,dictionary3)
    #print("***",documentlist3)
    #notin=query_process(notin)
    source=query["source"] #search url
    cat=query["cat"] #search meta-tags?
    document_for_dictionary_one=[]
    document_for_dictionary_two=[]
    document_for_dictionary_three=[]
    
    document_for_dictionary_one= list(set(documentlist1).intersection(set(documentlist2)))
    if len(inputarrlist)==0:
        document_for_dictionary_one=documentlist2.copy()
    if len(inputarr)==0:
        document_for_dictionary_one=documentlist1.copy()
    document_for_dictionary_one= list(set(document_for_dictionary_one).difference(set(documentlist3)))
    
    document_for_dictionary_two= list(set(documentlist12).intersection(set(documentlist22)))
    if len(inputarrlist)==0:
        document_for_dictionary_two=documentlist22.copy()
    if len(inputarr)==0:
        document_for_dictionary_two=documentlist12.copy()
    document_for_dictionary_two= list(set(document_for_dictionary_two).difference(set(documentlist32)))
    
    document_for_dictionary_three= list(set(documentlist13).intersection(set(documentlist23)))
    if len(inputarrlist)==0:
        document_for_dictionary_three=documentlist23.copy()
    if len(inputarr)==0:
        document_for_dictionary_three=documentlist13.copy()
    document_for_dictionary_three= list(set(document_for_dictionary_three).difference(set(documentlist33)))
    
    
    #run query
    #search in dictionary
    #inputarrlist=["hello there", "hello here"]
    #inputarr=["سلام","رهبر"]
    #dictionary={'سلام': [{4: [22]},{5: [2,3,4]},{6: [2]}],'رهبر': [{4: [23]},{6: [10]}],'نمایشگاه': [{4: [23]},{6: [3]}]}
    #print(document_for_dictionary_one)
    #print(document_for_dictionary_two)
    print(document_for_dictionary_three)
    document=[]
    document.extend(document_for_dictionary_one)
    document.extend(document_for_dictionary_two)
    document.extend(document_for_dictionary_three)
    document=list(set(document))
    #return result as a list in document list
    
    #document=[2,4]
    #print(document)
    #print(document_for_dictionary_one)
    return jsonify(document)

@app.route('/api/results', methods=['GET'])
def result():
    # get array or list of docIDs -> results?id=1,2,3
    if 'id' in request.args:
        ids = request.args['id']
        ids= ids.split(',')
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    for id in ids:
        results.append(id)
        if int(id)<1730:
            results.append(d[int(id)])
        
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return json.dumps(results,ensure_ascii=False)



app.run()