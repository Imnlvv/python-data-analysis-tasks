#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np


# In[49]:


marvel = pd.read_csv('MarvelComicCaracters.csv', sep = ';')
marvel


# In[25]:


marvel['align'].value_counts()


# In[26]:


marvel['eye'].value_counts()


# In[30]:


marvel.groupby('align')['eye'].value_counts()


# In[38]:


marvel['first_appearance'].value_counts()


# In[41]:


marvel['appearances'].value_counts()


# In[42]:


male_characters_over_100 = marvel[(marvel['sex'] == 'Мужской персонаж') & (marvel['appearances'] > 100)]


# In[54]:


marvel[(marvel['sex'] == 'Мужской персонаж') & (marvel['appearances'] > 100)].shape[0]


# In[55]:


marvel[marvel['sex'] == 'Мужской персонаж'].shape[0]


# In[59]:


marvel[(marvel['align'] == 'Добрый персонаж') & (marvel['eye'] == 'Пурпурные глаза')]


# In[60]:


marvel[(marvel['sex'] == 'Мужской персонаж') & (marvel['appearances'] > 100)].shape[0]


# In[ ]:




