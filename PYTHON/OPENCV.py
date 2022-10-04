#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


#Reading of an image 

image_path = 'doraemon.PNG'

image = cv2.imread(image_path)


# In[3]:


#Displaying an image
cv2.imshow('Sample image',image)
cv2.waitKey(0)#instructs system to wait till image is displayed
cv2.destroyAllWindows()


# In[4]:


#Saving of image
directory = r'C:\Users\Jyoti Ojha\Desktop\OpenCv'
filename = 'savedimagefortest.png'
cv2.imwrite(filename,image)
print("Image saved")


# In[5]:


#Accessing properties of an image
print(image.shape)#resolution of image


# In[6]:


#Changing color space
#RGB to GRAY
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale',gray)
cv2.waitKey(0)#instructs system to wait till image is displayed
cv2.destroyAllWindows()


# In[7]:


directory = r'C:\Users\Jyoti Ojha\Desktop\OpenCv'
filename = 'gray.png'
cv2.imwrite(filename,gray)


# In[8]:


#GRAY to RGB
org = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
cv2.imshow('Original',org)
cv2.waitKey(0)#instructs system to wait till image is displayed
cv2.destroyAllWindows()


# In[9]:


#Resize an image
resize = cv2.resize(image,(200,200))


# In[10]:


cv2.imshow('Resized',resize)
cv2.waitKey(0)#instructs system to wait till image is displayed
cv2.destroyAllWindows()


# In[11]:


#Writing on an image
new = cv2.putText(image,'Doraemon',(500,550),cv2.FONT_HERSHEY_SIMPLEX,4,(25,0,0),10)
cv2.imshow('New',new)
cv2.waitKey(0)#instructs system to wait till image is displayed
cv2.destroyAllWindows()


# In[12]:


line = cv2.line(image,(0,0),(120,500),(0,0,512),8)
cv2.imshow('line',line)
cv2.waitKey(0)#instructs system to wait till image is displayed
cv2.destroyAllWindows()


# In[13]:


circle = cv2.circle(image,(220,150),150,(120,0,0),9)
cv2.imshow('circle',circle)
cv2.waitKey(0)#instructs system to wait till image is displayed
cv2.destroyAllWindows()


# In[ ]:


rc = cv2.rectangle(image,(50,120),(50,120),(55,0,55),80)
cv2.imshow('rect',rc)
cv2.waitKey(0)#instructs system to wait till image is displayed
cv2.destroyAllWindows()


# In[ ]:


#Open the camera
vid = cv2.VideoCapture(0)
while(True):
    ret_, frame = vid.read()
    cv2.imshow("vid",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
        vid.release()
cv2.detroyAllWindows()


# In[ ]:
print("Hello")#updation




