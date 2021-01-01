#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df=pd.read_csv("C:\\Users\\AMAN BIRADAR\\Downloads\\Python\\iris.csv")
df.head(5)


# In[5]:


df.info()


# In[6]:


df.columns


# In[7]:


df.describe()


# In[9]:


#Scatter Plot 
plt.scatter(df['sepal_length'],df['petal_length'])
plt.xlabel('sepal_length')
plt.ylabel('petal_length')


# In[10]:


#Scatter plot
plt.scatter(df['sepal_length'],df['sepal_width'])
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')


# In[11]:


#student task 
#plot a scatter plot with each possible of two col in iris dataset
#Scatter Plot
plt.scatter(df['petal_length'],df['petal_width'])
plt.xlabel('petal_length')
plt.ylabel('petal_width')


# In[15]:


# scatter plot
plt.scatter(df['sepal_width'],df['petal_width'])
plt.xlabel('sepal_width')
plt.ylabel('petal_width')


# In[16]:


#Scatter plot
plt.scatter(df['petal_length'],df['sepal_width'])
plt.xlabel('petal_length')
plt.ylabel('sepal_width')


# In[17]:


#Scatter plot
plt.scatter(df['sepal_width'],df['petal_length'])
plt.xlabel('sepal_width')
plt.ylabel('petal_length')


# In[18]:


#Scatter plot
plt.scatter(df['petal_length'],df['sepal_length'])
plt.xlabel('petal_length')
plt.ylabel('sepal_length')


# In[21]:


x=np.array(np.arange(5))
y=x**2
x


# In[22]:


y


# In[23]:


plt.plot(x,y,'-*')


# In[26]:


df1=pd.read_csv("C:\\Users\\AMAN BIRADAR\\Downloads\\Python\\Sal.csv")
df1


# In[29]:


plt.plot(df1['Age'],df1['Sal'],'-*')


# In[46]:


plt.bar(df1['F_name'],df1['Sal'])
plt.figure(figsize=(10,15))


# In[49]:


plt.bar(df1['Age'],df1['Sal'])
plt.figure(figsize=(15,10))


# In[50]:


plt.bar(df1['F_name'],df1['Age'])
plt.figure(figsize=(15,10))


# In[ ]:




