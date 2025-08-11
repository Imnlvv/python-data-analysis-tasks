#!/usr/bin/env python
# coding: utf-8

# Создание переменных

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


bikes = pd.read_csv('BikeData.csv')
bikes.head()


# In[3]:


bikes['Rental Count'] = bikes['Partner 1'] + bikes['Partner 2']


# In[4]:


bikes.head()


# In[5]:


del bikes['Partner 1'] # удаление коллонки


# In[6]:


bikes.head()


# In[7]:


bikes = bikes.drop('Partner 2', axis = 1) # удаляем колонку при помощи pandas, указывая ее columns (1)


# In[8]:


bikes.head()


# Работа с датами

# In[9]:


bikes.info()


# In[10]:


pd.to_datetime(bikes['Date'], dayfirst=True) # меняем тип признака Date


# In[11]:


pd.to_datetime(bikes['Date'], dayfirst=True).dt.year # смотрим год


# In[12]:


pd.to_datetime(bikes['Date'], dayfirst=True).dt.day # смотрим день


# In[13]:


pd.to_datetime(bikes['Date'], dayfirst=True).dt.month # смотрим месяц


# In[14]:


bikes['Date'] = pd.to_datetime(bikes['Date'], dayfirst=True)


# In[15]:


bikes[bikes['Date'].dt.month == 3].shape


# In[16]:


bikes[bikes['Date'].dt.day_name() == 'Sunday'].shape


# Переменные True и False

# ###### Бинарная переменная - 1 способ

# In[17]:


bikes['Functioning Day'] = bikes['Functioning Day'] == 'Yes'


# In[18]:


bikes.head()


# ###### Бинарная переменная - 2 способ

# In[19]:


def currency_converter(rub):
    return round(rub / 74.73, 2)

print(currency_converter(1000))
amounts = [1000, 2000, 5000, 12345]
print(list(map(currency_converter, amounts)))
print(list(map(lambda rub: round(rub / 74.73, 2), amounts))) # анонимная функция


# In[20]:


bikes['Holiday'].apply(lambda x : 1 if x == 'Holiday' else 0) # бинарность через apply


# In[21]:


bikes['Holiday'] = bikes['Holiday'].apply(lambda x : 1 if x == 'Holiday' else 0)


# In[22]:


bikes.head()


# In[23]:


bikes['Humidity'].apply(lambda x: 1 if x in range(40,61) else 0)


# In[24]:


bikes['Humidity'] = bikes['Humidity'].apply(lambda x: 1 if x in range(40,61) else 0)


# In[25]:


bikes.head()


# Категориальные переменные из колличественных

# In[26]:


def get_temp_cat(temp):
    if temp < 0:
        return 'Freesing'
    elif temp < 15:
        return 'Chilly'
    elif temp < 26:
        return 'Nice'
    elif temp >=26:
        return 'Hot'
    else:
        return temp


# In[27]:


bikes['Temperature Category'] = bikes['Temperature'].apply(get_temp_cat)


# In[28]:


bikes.head()


# In[29]:


bikes.info()


# In[30]:


bikes['Temperature Category'] = pd.Categorical(bikes['Temperature Category']) # меняем категорию


# In[31]:


bikes.info()


# In[32]:


bikes['Temperature Category']


# In[33]:


bikes['Temperature Category'].cat.codes # массив, закодированный числами


# In[34]:


bikes['Temperature Category'].cat.categories # категории


# Переменная с несколькими основными переменными

# In[35]:


bikes['Good Weather'] = np.where((bikes['Temperature Category'] == 'Nice') & (bikes['Humidity'] == 1) & (bikes['Wind speed'] <= 5.4) & (bikes['Snowfall'] == 0) & (bikes['Rainfall'] == 0), 1, 0)


# In[36]:


bikes.head()


# In[37]:


bikes['Good Weather'].sum()


# Cохранение DataFrame

# In[42]:


bikes.to_csv('BikesDataVars.csv', index = False)
bikes.to_excel('BikesDataVars.xlsx', index = False)
df = pd.read_csv('BikesDataVars.csv')
df.info()


# In[43]:


df = pd.read_excel('BikesDataVars.xlsx')
df.info()


# In[44]:


bikes.to_pickle('BikesDataVars.pkl')
df = pd.read_pickle('BikesDataVars.pkl')
df.info()

