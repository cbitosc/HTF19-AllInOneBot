#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
import io
import random
import string # to process standard python strings
import warnings
import numpy as np
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer 

import warnings
warnings.filterwarnings('ignore')


# In[ ]:


app = Flask(__name__)


# In[4]:


import nltk
from nltk.stem import WordNetLemmatizer


# In[5]:


lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# In[6]:


GREETING0_INPUTS = ("hey","hai","hello","hi","good morning")
GREETING0_RESPONSES = ["hey","hai","hello","hi"]

GREETING1_INPUTS = ("principal's name","principal")
GREETING1_RESPONSES = ["Ravinder reddy"]

GREETING2_INPUTS = ("about","infrastructure","rank")
GREETING2_RESPONSES = ["Chaitanya Bharathi Institute of Technology (CBIT) is a private engineering college located in Gandipet,Hyderabad, Telangana, India.90 acres of Land,NRIF Ranking:101–150 "]

GREETING3_INPUTS = ("phone","contact","email","address","media")
GREETING3_RESPONSES = [" Phone: +91-040-24193276 Fax: +91-040-24193278 Email: principal@cbit.ac.in"]

GREETING4_INPUTS = ("placement","company","job")
GREETING4_RESPONSES = [" a total of 300 companies visited CBIT recruiting 12,909 students from various disciplines. "]

GREETING5_INPUTS = ("events")
GREETING5_RESPONSES = ["Hacktoberfest","Sparkle "," Tissue engineering"]



def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING1_INPUTS:
            return random.choice(GREETING1_RESPONSES)
        elif word.lower() in GREETING2_INPUTS:
            return random.choice(GREETING2_RESPONSES)
        elif word.lower() in GREETING3_INPUTS:
            return random.choice(GREETING3_RESPONSES)
        elif word.lower() in GREETING4_INPUTS:
            return random.choice(GREETING4_RESPONSES)
        elif word.lower() in GREETING5_INPUTS:
            return random.choice(GREETING5_RESPONSES)
        elif word.lower() in GREETING0_INPUTS:
            return random.choice(GREETING0_RESPONSES)


# In[ ]:





# In[7]:





# In[ ]:





# In[ ]:
@app.route("/")
def home():
    
    return render_template("front.html") 
@app.route("/getans", methods=["POST"])
def get_bot_response():    
    userText = request.form['msg']
    lemmatizer = WordNetLemmatizer()
    flag=True
    resp = ''
    print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
    if(True):
        user_response = userText
        user_response=user_response.lower()
        word_list = nltk.word_tokenize(user_response)
        lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
        if(lemmatized_output!='bye'):
            if(lemmatized_output=='thanks' or lemmatized_output=='thank you' ):
                flag=False
                print("ROBO: You are welcome..")
                resp  = ("ROBO: You are welcome..")
            else:
                if(greeting(lemmatized_output)!=None):
                    print("ROBO: "+greeting(lemmatized_output))
                    resp = "ROBO: "+greeting(lemmatized_output)
                else:
                    print("ROBO: ",end="")
                    print("Sorry ! will improve soon :)")
                    resp = "Sorry ! will improve soon :)"
        else:
            flag=False
            
            resp  = "Sorry ! will improve soon :)"
        return render_template('resp.html', resp = resp)
     
if __name__ == "__main__":    
    app.run(port="5001", debug=True)





# In[ ]:




