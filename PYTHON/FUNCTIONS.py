#!/usr/bin/env python
# coding: utf-8

# FUNCTIONS:
#   1. FUNCTION DEFINITION
#   2. FUNCTION CALLING
#   3. USE OF RETURN
#   4. PASSING ARGUMENTS
#   5. EXAMPLE
#   6. Arbitrary arguments
#   7. Keyword arbitrary arguments
#   

# # Basic syntax of a function
# def function_name(arg1,arg2):
#         

# In[1]:


def add(a,b):
    print(a+b)


# In[2]:


add(12,13)


# In[3]:


# Function using return 
def add1(a,b):
    return (a+b)


# In[4]:


add1(12,13)


# In[5]:


def add3(a,b):
    c=a+b
    print(c)


# In[6]:


add3(2,3)


# In[7]:


c=10


# In[8]:


c


# In[9]:


c=10
def add4(a,b):
    c=9


# In[10]:


c


# In[11]:


#Function to checK whether a given number is prime
def prime(a):
    for n in range(2,a):
        if(a%n==0):
            print("Is not prime")
            break
        else:
            print("Is prime")
            


# In[12]:


prime(3)


# In[13]:


prime(22)


# In[14]:


prime(18)


# In[15]:


# Arbitrary arguments : *args


# In[16]:


def hello(*names):
    for name in names:
        print("hello "+name)


# In[17]:


hello("A","B","C","D")


# In[18]:


#Keyword arguments

def family(father,mother,son,daughter):
    print("The father is "+ father)


# In[19]:


family(father = "X", mother = "Y",son="Z",daughter = "V")


# In[20]:


# Arbitrary keyword argument = **kwargs


# In[21]:


def name(**a):
    print("First name is ",a["firstname"])


# In[22]:


name(firstname="Jyoti",lastname="OJha")


# In[23]:


#Function using list as argument
def func(hobby):
    """ This function is for hobbies """ #Docstrings
    for x in hobby:
        print(x)


# In[24]:


hobby=["swimming","singing"]


# In[25]:


func(hobby)


# In[26]:


# Default parameter value

def func1(fruit="Apple"):
    print("I love "+fruit)


# In[27]:


func1()


# In[28]:


func1("Mango")


# In[29]:


# DOCSTRINGS : These are used to define the purpose of the given fuction and can be accessed later to check the purpose of defined function.
# Docstrings are defined/written at the construction time.


# In[30]:


# Let's see how to access the doctring which we defined while making function func.
print(func.__doc__)
priny("hello")

# In[31]:


#As we can see above that we defined a function func somewhere at an early stage and with the use of docstrings we can check the use of that function later and can use it if needed.


# In[ ]:




