#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# 01

# In[2]:


cat = pd.read_csv('cat.csv')
cat.head()


# In[3]:


def fun(x):
    if x == 'Horror':
        return 2
    if x == 'Drama':
        return 1
    else:
        return 0


# In[4]:


cat['coded'] = cat['Genre'].apply(fun)


# In[5]:


cat['coded'].sum()


# In[6]:


total_sum = cat['coded'].sum().item()  # преобразование к обычному числу
print(total_sum)

