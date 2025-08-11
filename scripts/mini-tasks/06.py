#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# 01

# In[3]:


train = pd.read_csv('train3_C.csv')
train.head()


# In[4]:


train[(train['day_of_week'] == 'Friday')].sort_values('humidity')


# In[5]:


train[train['day_of_week'].isin(['Friday', 'Saturday'])].sort_values('humidity')


# In[6]:


round(306.250000, 2)


# In[7]:


qv_count = train['pedestrian_count'].quantile(0.25)


train_c = train[(train['pedestrian_count'] < qv_count)]
train_c.head()


# In[10]:


incidents = train_c['pedestrian_incidents'].max() - train_c['pedestrian_incidents'].min()
incidents


# In[29]:


def fun(x):
    return len(x.split(',')) 


# In[30]:


train['coded'] = train['weather_conditions'].apply(fun)


# In[31]:


train['coded'].sum()


# 02

# In[42]:


trainss = pd.read_csv('trains_b.csv')
trainss.head()


# In[104]:


trainss['Region'].value_counts().plot(kind = 'line')


# In[67]:


tr = pd.read_csv('train4_b.csv')
tr.head()


# In[75]:


tr.groupby('Sex').sum().plot(kind = 'pie', subplots=True)


# 03

# In[73]:


train5 = pd.read_csv('train5_b.csv')
train5.head()


# In[76]:


train5['Humidity'].plot(kind = 'box')


# 04

# In[77]:


catty = pd.read_csv('catti.csv')
catty.head()


# In[83]:


catty['cat'].value_counts().plot(kind = 'bar')


# 05

# In[105]:


trainy = pd.read_csv('train5_C.csv')
trainy.head()


# In[106]:


trainy['Country'].value_counts(ascending=True)


# In[114]:


austria = trainy[(trainy['Country'] == 'Austria')]


# In[117]:


austria[austria['HighestPoint'] == 780]


# In[123]:


lif = trainy[(trainy['NightSki'] == 'Yes')]['LiftCapacity']


# In[120]:


lif.quantile(0.75) - lif.quantile(0.25)


# In[121]:


round(45356.0, 2)


# In[124]:


def fun(x):
    if 'Russia' in x:
        return 1
    else:
        return 0


# In[126]:


trainy['coded'] = trainy['Country'].apply(fun)


# In[127]:


trainy['coded'].sum()


# In[128]:


round(5, 2)


# 06

# In[11]:


mus = pd.read_csv('music.csv')
mus.head()


# In[12]:


df = mus[mus['album_name'] == 'Different Stages']


# In[13]:


df['loudness'].abs()


# In[16]:


ds = mus[mus['album_name'] == 'Different Stages']


# In[17]:


ds['loudness'].abs().max()


# In[18]:


ds['song_name'].loc[345]


# In[19]:


mus[mus['song_name'] == '2112 (Discovery) - Live']


# In[189]:


mus.head()


# In[191]:


inst = mus[(mus['mode'] == 0)]['instrumentalness']


# In[193]:


inst.quantile(0.75)


# In[194]:


round(0.26475000000000004, 2)


# In[195]:


def fun(x):
    return len(x)


# In[196]:


mus['coded'] = mus['song_name'].apply(fun)


# In[197]:


mus['coded'].mean()


# In[198]:


round(30.758928571428573, 2)

