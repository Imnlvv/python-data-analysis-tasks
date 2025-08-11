#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# 01

# In[2]:


data = pd.read_csv("datademo2.csv")
data


# In[3]:


data[(data['Year_of_Release'] < 2005) & (data['Genre'] == 'Sports')].shape


# In[4]:


data[data['Publisher'] == 'Nintendo'].shape


# In[5]:


round(16719 / 706, 2)


# 02

# In[6]:


taylor = pd.read_csv("Taylor_final.csv")
taylor.head()


# In[7]:


taylor[(taylor['album'] == 'Fearless') & (taylor['energy'] > 0.6)].shape


# In[8]:


taylor[taylor['album'] == 'Speak Now'].shape


# In[9]:


round(26 / 1265, 2)

