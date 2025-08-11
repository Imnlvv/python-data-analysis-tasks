#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[10]:


comics = pd.read_csv('MarvelComicsCaracters.csv', sep = ';')
comics.head()


# In[12]:


comics['appearances'].isna().sum()


# In[14]:


comics_app = comics.dropna(subset = ['appearances'])


# In[16]:


q3 = np.percentile(comics_app['appearances'], 75)
q1 = np.percentile(comics_app['appearances'], 25)

iqr = q3 - q1

iqr_threshold_bottom = q1 - 1.5 * iqr # нижняя граница выбросов
iqr_threshold_top = q3 + 1.5 * iqr # верхняя граница выбросов

print(iqr_threshold_bottom, iqr_threshold_top)


# In[ ]:




