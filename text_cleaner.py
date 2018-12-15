
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re
from nltk.tokenize import word_tokenize 
import string
from nltk.stem import PorterStemmer
from stop_words import get_stop_words


# In[2]:


apos_words ={
"aren't" :'are not',"can't":"cannot","couldn't":"could not","didn't":"did not",
"doesn't":"does not","don't":"do not","hdn't":"had not","hasn't":"has not",
"haven't":"have not","he'd":"he would","he'll":"he will","he's":"he is",
"He'd":"He would","He'll":"He will","He's":"He is",
"I'd":"I would","I'll":"I will","I'm":"I am","I've":"I have",
"isn't":"is not","it's":"it is","let's":"let us","mustn't":"must not","shan't":"shall not",
"she'd":"she would","she'll":"she will","she's":"she is","shouldn't":"should not",
"She'd":"She would","She'll":"She will","She's":"She is",
"that's":"that is","there's":"there is","they'd":"they had","they'll":"they will",
"they're":"they are","they've":"they have","we'd":"we would","we're":"we are",
"we've":"we have","weren't":"were not","what'll":"what will","what're":"what are",
"what's":"what is","what've":"what have","where's":"where is","who'd":"who would",
"who'll":"who will","who're":"who are","who's":"who is","who've":"who have",
"won't":"will not","wouldn't":"would not","you'd":"you would","you'll":"you will",
"you're":"you are","you've":"you have", "You're":"You are"}


# In[3]:


punc = list(string.punctuation)
punc.append('--')
punc.append('//')
punc.append('’')
punc.append('!!')
punc.append("``")
punc.append("''")
punc.remove("\"")


# In[4]:


languages = ['Danish','Dutch','English','Finnish','French','German',
             'Hungarian','Italian','Portuguese','Russian','Spanish','Swedish']
stop_words=[]
for language in languages:
    stop_words_pre = get_stop_words(language.lower())
    for sw in stop_words_pre:
        stop_words.append(sw) 


# In[5]:


def digit_remover(words):
    exp = '\d+'
    for word in words:
        if re.match(exp, word):
            words.remove(word)
    return words
         
def apost_word_replacer(words):
    for word in words:
        if word in apos_words.keys():
            w = apos_words[word]
            idx = words.index(word)
            words[idx] = w
        elif re.match("\w+'s",word):
            w = word.split("'")
            w = w[0]+" is"
            idx = words.index(word)
            words[idx] = w
            
            
    return words        

def stemmer(words):
    lem =PorterStemmer()
    for word in words:
        w = lem.stem(word)
        idx = words.index(word)
        words[idx] = w
    return words   


# In[6]:


def text_modifier(words):    
    words = digit_remover(words)
    
    return words


# In[7]:


def text_cleaner(text):
    new_text=""
    text_words = apost_word_replacer(text.split(" "))
    for word in text_words:        
        new_text =new_text+" "+word
    text_words = word_tokenize(new_text)
    text_words = text_modifier(text_words)
    new_text=""
    for word in text_words:
        if word in punc:
            pass
        else:
            new_text =new_text+" "+word
    return new_text        


# In[8]:


def all_texts_cleaner(text_set):
    all_texts=[]
    for text in text_set:
        new_text = text_cleaner(text)
        all_texts.append(new_text)
    return all_texts    


# In[9]:


def text_without_stop_words_aux(text):
    words = word_tokenize(text)
   # words = stemmer(words)
    for word in words:
        if word in stop_words:
            idx = words.index(word)
            words[idx] = ""
        else:
            idx = words.index(word)
            words[idx] = word.lower()
    new_text=""        
    for word in words:        
        new_text =new_text+" "+word        
    return new_text       


# In[10]:


def texts_without_stop_words(texts):
    texts_ws = []
    texts = all_texts_cleaner(texts)
    for text in texts:
        text = text_without_stop_words(text)
        texts_ws.append(text)
    return texts_ws    

