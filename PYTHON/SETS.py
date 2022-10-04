#!/usr/bin/env python
# coding: utf-8

# SETS

# In[1]:


a=set()


# In[2]:


print(type(a))


# In[3]:


#Addition of elements in a set
a.add(1)


# In[4]:


a


# In[5]:


a.add(1)


# In[6]:


a


# In[7]:


b=set()


# In[8]:


b.add(2)


# In[9]:


b


# In[10]:


#Union
a.union(b)


# In[11]:


a.add(3)


# In[12]:


a


# In[13]:


#Removal of elements 
a.remove(3)


# In[14]:


a


# In[15]:


a.discard(1)


# In[16]:


a


# In[17]:


a.add(1)


# In[18]:


a


# In[19]:


#Disjoint sets
a.isdisjoint(b)


# In[20]:


#List
l=[1,2,3,4,5]


# In[21]:


print(type(l))


# In[22]:


#Set from a list
b=set(l)


# In[23]:


b


# In[24]:


print(type(b))


# In[ ]:


print("GG")#updation

