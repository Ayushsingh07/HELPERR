#!/usr/bin/env python
# coding: utf-8

# In[5]:


import nltk
from nltk.chat.util import Chat, reflections


# In[6]:


reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}


# In[7]:


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
   
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"1",
        ["Enter 'A' for complaint against authorities.\nEnter 'E' for complaint against employees.\nEnter 'Rr' for complaint against rules and regulations.\nEnter 'Oth' for complaint against other staff\n"]
    ],
    [
        r"A",
        ["Enter your complaint and then type Done."]
    ],
    [
         r"E",
        ["Enter your complaint and then type Done."]
    ],
    [
        r"Rr",
        ["Enter your complaint and then type Done."]
    ],
    [
        r"Oth",
        ["Enter your complaint and then type Done."]
    ],
    [
        r"Done",
        ["Your complaint has been registered in the respective section"]
    ],
    [
        r"2",
        ["Enter 'C' for confidence related issues.\nEnter 'L' for leadership skills issues.\nEnter 'S' to learn about social skills."]
    ],
    [
        r"C",
        ["1. Be positive and believe in yourself.\n2. Build on your strengths.\n3. Develop new skills.\nTo learn more refer to following links :\nhttps://www.lmalloyds.com/LMA/Young_Professionals/Newsletter/Top_10_tops_confidence.aspx\nhttps://hbr.org/2021/08/how-to-build-confidence-at-work\nhttps://virtualspeech.com/blog/speak-with-confidence-in-public\nhttps://hbr.org/2019/10/how-to-look-and-sound-confident-during-a-presentation\nhttps://www.skillsyouneed.com/ps/confidence.html"]
    ],
    [
        r"L",
        ["1. Be confident and fluent with your words.\n2. Present your points in the best way you can.\n3. Try to understand the problems of people around you.\nFor further information refer to following links:\nhttps://www.forbes.com/sites/ashiraprossack1/2021/06/29/how-to-unlock-your-full-leadership-potential/?sh=5129fea144ac\nhttps://www.hrdconnect.com/2019/08/06/how-to-develop-leadership-skills-in-the-workplace/\nhttps://www.thriveyard.com/35-ways-to-improve-your-leadership-skills-at-work/\nhttps://www.thebalancecareers.com/top-leadership-skills-2063782\nhttps://elearningindustry.com/build-develop-your-leadership-skills-5-ways"]
    ],
    [
        r"S",
        ["Refer to following links:\nhttps://www.indeed.com/career-advice/career-development/developing-social-skills\nhttps://www.conovercompany.com/7-interpersonal-social-skills-for-the-workplace/\nhttps://www.orblogic.com/Post/View/improving-social-skills\nhttps://www.futurelearn.com/courses/communication-and-interpersonal-skills-at-work\nhttps://www.hcamag.com/us/news/general/6-soft-skills-needed-in-the-workplace/316149"]
    ],
    
]


# In[ ]:


def chat():
    print(" Hello! This is Bot,your virtual assisstant.")
    print(" How can I help you ?")
    print("   Enter 1 to register complaint \n   Enter 2 to learn\n")
    print(" * Enter quit when you want to exit\n")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()
print('end of the program')

# In[ ]:




