#!/usr/bin/env python
# coding: utf-8

# Переменные:
# 
# - Date — день/месяц/год (с 01.12.2017 по 30.11.2018)
# - Partner 1 — кол-во велосипедов, взятых в аренду в этот час в 1 партнерсом сервисе
# - Partner 2 — кол-во велосипедов, взятых в аренду в этот час во 2 партнерсом сервисе
# - Hour — час (от 0 до 24)
# - Temperature — температура в градусах Цельсия
# - Humidity — процент влажности
# - Wind speed — скорость ветра м/сек
# - Rainfall — осадки в виде дождя, мм
# - Snowfall — осадки в виде снега, см
# - Seasons — сезон (Winter, Spring, Summer, Autumn)
# - Holliday — рабочий или праздничный день (Holiday/No holiday)
# - Functional Day — рабочий или нерабочий день велопроката (Yes/No)

# In[3]:


import pandas as pd
bikes = pd.read_csv('BikeData.csv')
bikes


# In[3]:


bikes.head() # первые 5


# In[4]:


bikes.head(10) # первые n-колва


# In[5]:


bikes.tail() # последние 5


# In[6]:


bikes.tail(10) # последние n-колва


# In[12]:


bikes.iloc[100:110] # срез середины, с 100 по 110


# In[13]:


bikes.head(5)


# In[ ]:


# категориальные и номинальные переменные - переменные не кол-венные,словами, нельзя сравнить и т.д. 


# Фильтрация данных

# In[14]:


bikes.columns


# In[15]:


bikes.shape


# In[16]:


bikes.info()


# In[ ]:


# Non-Null Count - информация о пустых ячейках в таблицах
# Dtype - тип данных на этой строке (например, object это строка)


# In[19]:


bikes['Hour'].unique() # метод для поиска уникальных значений в коллонке


# In[20]:


bikes['Seasons'].unique()


# In[23]:


bikes[['Partner 1','Partner 2']]


# In[25]:


bikes.iloc[124] # вызываем ряд через iloc


# In[27]:


bikes.iloc[1212]['Partner 1'] # обращаемся к ряду, со значением Partner 1


# In[5]:


bikes['Holiday'] == 'No Holiday'


# In[7]:


bikes['Holiday'][12] == 'No Holiday'


# In[32]:


bikes[bikes['Holiday'] == 'Holiday'].shape


# In[34]:


bikes[(bikes['Holiday'] == 'Holiday') & (bikes['Temperature'] >= 15)].shape


# In[35]:


bikes[(bikes['Holiday'] == 'Holiday') | (bikes['Temperature'] >= 15)].shape


# In[36]:


bikes[~((bikes['Holiday'] == 'Holiday') | (bikes['Temperature'] >= 15))].shape


# In[39]:


bikes[(bikes['Holiday'] == 'No Holiday') & (bikes['Temperature'] >= 15) & (bikes['Seasons'] == 'Spring')].shape


# In[41]:


bikes['Temperature'].isna() # метод для поиска пропущенных ячеек


# In[43]:


bikes[bikes['Temperature'].isna()].shape


# In[49]:


bikes[bikes['Seasons'].isin(['Winter','Summer'])].shape # метод для поиска пренадлежности к нескольким условиям (к 2м и более)


# In[51]:


bikes[bikes['Temperature'].isin(range(15,26))].shape # также по рядам фильтровка


# Сортировка данных

# In[55]:


bikes['Temperature'].sort_values() # сортировка коллонки по возрастанию


# In[56]:


bikes['Temperature'].sort_values(ascending = False) # сортировка коллонки по убыванию


# In[58]:


bikes.sort_values(by=['Temperature'])  # сортировка данных коллонки по убыванию


# In[64]:


bikes.sort_values(by=['Temperature'], ascending = False) # сортировка данных коллонки по убыванию


# In[68]:


bikes.sort_values(by=['Temperature','Humidity']) # сортировка по двум коллонкам по возрастанию


# In[70]:


bikes.sort_values(by=['Temperature','Humidity'], ascending = False) # сортировка по двум коллонкам по убыванию


# In[72]:


bikes.sort_values(by=['Temperature','Humidity'], ascending = [True, False]) # сортировка по двум коллонкам: 1) по возрастанию, 2) по убыванию


# Работа в Excel

# Формулы и функции
# 
# 1. =A1*$F$1 : Фиксация к 1 ячейке повсеместно.
# 2. =СУММ(B1:B5) : Суммарная общая цена.
# 3. Fx : Мастер функций (все функции там).
