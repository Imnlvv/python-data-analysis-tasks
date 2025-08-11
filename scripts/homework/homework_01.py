#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


star = pd.read_csv('StarWars.csv', sep = ';')
star


# In[12]:


star.loc[10:20]


# In[20]:


star[star['loc'] == 'Горный'].shape


# In[17]:


star[star['loc'] == 'Южно-Атлантический'].shape


# In[21]:


star[star['loc'] == 'Юго-Восточный центральный'].shape


# In[22]:


star[star['loc'] == 'Тихоокеанский'].shape


# In[23]:


star[star['loc'] == 'Средне-Атлантический'].shape


# In[24]:


star[star['loc'] == 'Северо-Восточный центральный'].shape


# In[25]:


star[(star['age_group'] == '18-29') & (star['fan'] == 'нет') & (star['loc'] == 'Тихоокеанский')].shape


# In[52]:


star[star['yoda'].isna()].shape


# In[33]:


star[(star['princess_leia_organa'] == 'очень нравится') & (star['loc'] == 'Новая Англия')].shape


# In[36]:


star[(star['seen'] == 'нет') & (star['fan'] == 'да')].shape


# In[40]:


star[(star['loc'] == 'Горный') & (star['income'] == '150.000+')]


# In[42]:


star[(star['age_group'] == '45-60') & (star['fan'] == 'да')].shape


# In[43]:


star[(star['age_group'] == '18-29') & (star['fan'] == 'нет')].shape


# In[50]:


star[(star['fan'] == 'да') & (star['loc'] == 'Новая Англия') & (star['income'] == '0 - 24.999')].shape[0]


# In[48]:


star


# In[54]:


star[(star['seen'].isna()) & (star['fan'].isna())].shape


# In[56]:


star[(star['fan'] == 'да') & (star['loc'] == 'Новая Англия') & (star['income'] == '0 - 24.999')].shape

