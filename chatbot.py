#!/usr/bin/env python
# coding: utf-8

# In[13]:


from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


# In[14]:


app = Flask(__name__)


# In[15]:


bot = ChatBot('CBIT CHATBOT')


# In[17]:




trainer = ListTrainer(bot)


# In[19]:


trainer.train(['What is your name?', 'My name is CBIT'])
trainer.train(['Who are you?', 'I am a bot' ])


# In[23]:


from chatterbot.trainers import ChatterBotCorpusTrainer
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
bot.get_response("who is obama?")


# In[ ]:


@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()


# In[ ]:




