#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


marvel = pd.read_csv('MarvelComicCaracters (1).csv', sep = ';')
marvel.head()


# In[4]:


marvel['align'].value_counts()


# In[6]:


marvel['eye'].value_counts()


# In[8]:


marvel[(marvel['sex'] == 'Мужской персонаж')]['eye'].mode()


# In[9]:


marvel[(marvel['sex'] == 'Женский персонаж')]['eye'].value_counts()


# In[14]:


marvel[(marvel['align'] == 'Добрый персонаж') & (marvel['eye'] == 'Пурпурные глаза')]


# In[4]:


marvel['eye'].mode()


# In[18]:


marvel[(marvel['first_appearance']== 1993)]['appearances']


# In[14]:


marvel[(marvel['sex'] == 'Женский персонаж')]['hair'].mode()


# In[15]:


marvel[(marvel['sex'] == 'Мужской персонаж')]['hair'].mode()


# In[17]:


marvel[(marvel['align'] == 'Злой персонаж')]['appearances'].median()


# In[18]:


print(marvel['appearances'].var(ddof=0))


# In[19]:


marvel['first_appearance'].mode()


# In[20]:


marvel['eye'][501:].mode()


# In[21]:


marvel['eye'].mode()


# In[22]:


marvel['hair'].mode()


# In[26]:


marvel_hair = marvel[marvel['hair'] == 'Черные волосы']


# In[27]:


print(marvel_hair['appearances'].std(ddof=0))

