
# coding: utf-8

# In[1]:


mylist=[1,2,3]
for item in mylist:
    print(item)


# In[2]:


mylist=[1,2,3,4,5,6,7,8,9,10]
for item in mylist:
    if item % 2 == 0:
        print(num)
    else:
        print("odd number")


# In[6]:


mylist=[1,2,3,4,5]
for item in mylist:
    if item % 2 == 0:
        print(item)
    else:
        print('odd number')


# In[7]:


mylist=[(1,2,3),(4,5,6),(7,8,8)]
for a,b,c in mylist:
    print(a)
    print(b)
    print(c)


# In[8]:


mylist=[(1,2),(4,5),(5,6)]
for a,b in mylist:
    print(a)


# In[9]:


mylist=[(1,2),(4,5),(5,6)]
for a,b in mylist:
    print(a)
    print(b)


# In[10]:


mylist={'k1':1,'k2':2}
for item in mylist:
    print(item)
 


# In[11]:


mylist={'k1':1,'k2':2}
for item in mylist.item():
    print(item)
    
    


# In[12]:


mylist={'k1':1,'k2':2}
for item in mylist.items():
    print(item)


# In[13]:


mylist={'k1':1,'k2':2}
for value in mylist.values():
    print(value)


# In[14]:


for _ in 'hello sayali':
    print('welcome to python programming')

