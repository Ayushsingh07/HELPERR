#!/usr/bin/env python
# coding: utf-8

# NumPy = Numerical python
# 
# 
#     1. Import NumPy
#     2. Creation of ndarray
#     3. Dimension in arrays
#     4. Indexing the arrays
#     5. Slicing the arrays
#     
#     

# In[3]:


# Array object in NumPy is called 'ndarray'


# In[4]:


import numpy


# In[5]:


arr = numpy.array([1,2,3,4,5])


# In[7]:


print(arr)


# In[2]:


# Import NumPy as np
import numpy as np 


# In[9]:


arr = np.array([1,2,3,4,5])
print(arr)


# In[10]:


print(type(arr))


# In[11]:


# To create a ndarray any object like list, tupple can be passed to the array() method and converted to an  ndarray


# In[12]:


arr = np.array((1,2,3,4,5))


# In[13]:


print (arr)


# In[14]:


# 0-D array
arr = np.array(200)
print(arr)


# In[16]:


# 1-D array
arr = np.array([1,2,3])
print(arr)


# In[19]:


# 2-D array
arr = np.array([[1,2],[3,4]])
print(arr)


# In[20]:


# 3-D array
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr)


# In[21]:


print(arr.ndim)


# In[23]:


print(arr[0])


# In[24]:


arr = np.array([[[[[1]]]]])


# In[25]:


print(arr)


# In[26]:


print(arr.ndim)


# In[27]:


arr = np.array((((((1))))))


# In[28]:


print(arr)


# In[3]:


arr2= np.array([1,2,3,4,5,6])
print(arr2[2]-arr2[3])


# In[4]:


print(arr2[2]*arr2[3])


# In[7]:


arr3 = np.array([[1,2,3],[4,5,6]])
print("2nd element in first row",arr3[0,1])


# In[10]:


print("1st element in second row",arr3[1,0])


# In[11]:


print(arr2[0:1])


# In[13]:


print(arr2[1:])


# In[18]:


# Second row first two elements
print(arr3[1,0:2])


# In[25]:


print(arr3[0:2,1])


# In[26]:


print(arr3[0:1,1:2])


# In[27]:


print(arr2.dtype)


# In[28]:


arr4 = np.array(["A","B","c"])


# In[29]:


print(arr4.dtype)


# In[30]:


a = arr2.copy()
arr2[0] = 10
print(arr2)
print(a)


# In[31]:


a = arr2.view()
arr2[0] = 10
print(arr2)
print(a)


# In[32]:


a[2] = 50
print(a)
print(arr2)


# In[34]:


print(arr2.shape)


# In[35]:


print(arr4.shape)


# In[37]:


print(arr3.shape)


# In[38]:


arr5 = np.array([1,2], ndmin = 5)
print(arr5.shape)


# In[48]:


# 1-D to 2-D
arr6 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr6.reshape(4, 3)

print(newarr)


# In[50]:


newarr2 = arr6.reshape(2,3,2)
print(newarr2)


# In[ ]:

print("Hello")#updation


