
# coding: utf-8

# In[10]:


def function_name(): 
    '''
    Docstring:info about this function
    Input:No input
    Output:Hello
    '''
    print("Hiii") 


# In[2]:


function_name() 


# In[11]:


help(function_name)


# In[15]:


def hello_function(name):
    print('Hello '+name)


# In[16]:


hello_function('sayali')


# In[17]:


def hello_function(name='NAME'):
    print('Hello ' +name)


# In[18]:


hello_function()


# In[19]:


result = hello_function('sayu')
    


# In[20]:


result


# In[21]:


type(result)


# In[22]:


def hii_function(name):
    return 'hello' +name


# In[23]:


result=hii_function(sayalee)


# In[24]:


result=hii_function('sayalee')


# In[25]:


type(result)


# In[26]:


def add_function(n1,n2):
    return n1+n2


# In[27]:


add_function(20,30)


# In[28]:


def cat_check(mystring):
    if 'cat' in mystring:
        return true
    else:
        return false
    


# In[29]:


cat_check('this is my cat')


# In[30]:


def cat_check(mystring):
    if 'cat' in mystring:
        return TRUE
    else:
        return FALSE


# In[31]:


cat_check('this is my cat')


# In[32]:


def cat_check(mystring):
    if 'cat' in mystring:
        return True
    else:
        return False


# In[33]:


cat_check('this is my cat')


# In[34]:


cat_check('this is my dog')

