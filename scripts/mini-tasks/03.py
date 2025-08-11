#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# 01

# In[2]:


wine = pd.read_csv('wine.csv')
wine.head()


# In[3]:


avg = wine['residual sugar'].mean()
std = wine['residual sugar'].std()

left = avg - 1.5 * std
right = std + 1.5 * std

left, right


# In[4]:


wine[(wine['residual sugar'] < left) | (wine['residual sugar'] > right)].shape[0]


# In[5]:


q1 = wine['residual sugar'].quantile(0.25)
q3 = wine['residual sugar'].quantile(0.75)

iqr = q3-q1

left = q1 -1.5*iqr
right = q3 +1.5*iqr

left, right


# In[6]:


wine[(wine['residual sugar'] < left) | (wine['residual sugar'] > right)].shape[0]

