#!/usr/bin/env python
# coding: utf-8

# Группировка данных

# In[2]:


import pandas as pd
import numpy as np

bikes = pd.read_pickle('BikesDataVars.pkl')
bikes.head()


# In[3]:


bikes['Temperature Category'].value_counts()


# In[4]:


bikes['Temperature Category'].value_counts(dropna = False)


# In[5]:


bikes['Good Weather'].value_counts()


# In[6]:


bikes.groupby('Date')['Rental Count'].sum()


# In[7]:


list(bikes.groupby('Date'))[0][1]


# In[8]:


bikes['Seasons'].value_counts() # сортировка по убыванию


# In[9]:


bikes.groupby('Seasons').size() # сортировка по индексу


# In[10]:


bikes.groupby('Seasons')['Good Weather'].value_counts()


# In[14]:


bikes.groupby(['Seasons', 'Temperature Category'], observed=True)['Rental Count'].sum()


# ##### Part 02

# Визуализация данных

# In[26]:


### Количественные переменные


# In[27]:


bikes.head()


# In[31]:


bikes['Temperature'].hist(bins = 20)


# In[ ]:


### Категориальные переменные


# In[34]:


bikes['Temperature Category'].value_counts().plot(kind = 'bar', xlabel = ' ') # от большего к меньшему


# In[36]:


bikes.groupby('Temperature Category').size().plot(kind = 'bar') # в алфавитном порядке


# In[38]:


bikes.groupby('Seasons')['Temperature Category'].value_counts().plot(kind = 'bar')


# In[42]:


bikes.groupby('Seasons')['Temperature Category'].value_counts().unstack().plot(kind = 'bar')


# In[43]:


bikes.groupby('Seasons')['Temperature Category'].value_counts().unstack().plot(kind = 'bar', stacked = True)

