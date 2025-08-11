#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# 01

# In[2]:


train = pd.read_csv('train1_b.csv')
train.head()


# In[3]:


train['atemp'].plot(kind = 'hist')


# In[4]:


train['humidity'].plot(kind = 'hist')


# In[5]:


train['windspeed'].plot(kind = 'hist')


# 02

# In[6]:


train2 = pd.read_csv('train1_C.csv')
train2.head()


# In[7]:


train2[((train2['FuelType'] == 'Gasoline') & (train2['Region'] == 'Armavir'))].sort_values('Year')


# In[8]:


train2[(train2['Year'] >= 2001)]['Mileage'].mean()


# In[9]:


round(126058.44031077245, 2)


# In[10]:


def fun(x):
    if 'Toyota' in x:
        return 1
    else:
        return 0


# In[11]:


train2['coded'] = train2['Car Name'].apply(fun)


# In[12]:


train2['coded'].sum()


# 03

# In[14]:


train3 = pd.read_csv('train2_C.csv')
train3.head()


# In[15]:


train3[(train3['bedrooms'] == 1)].sort_values('sqft_lot')


# In[16]:


mean_sqft_lot = train3['sqft_lot'].mean()
train3[(train3['waterfront'] == 1) & (train3['sqft_lot'] > mean_sqft_lot)]['grade'].var()


# In[17]:


round(3.1409460105112266, 2)


# In[18]:


train3.head()


# In[19]:


train3[(train3['bedrooms'] == 1)].sort_values('sqft_lot')


# In[22]:


train3['coded'] = train3['yr_renovated'].apply(fun)


# In[23]:


def fun(x):
    if x == 0:
        return 1
    elif x > 2001:
        return 21
    else:
        return 20


# In[24]:


train3['yr_renovated'].sort_values()


# In[25]:


train3['coded'].std()


# In[26]:


round(3.9140998408066743, 2)


# In[27]:


train3.head()


# In[28]:


mean_sqft = train3['sqft_lot'].mean()

train3[((train3['waterfront'] == 1) & (train3['sqft_lot'] > mean_sqft))]['grade'].var()


# In[29]:


round(3.133695652173913, 2)

