#!/usr/bin/env python
# coding: utf-8

# # Библиотека Pandas

# In[1]:


# импорт библиотеки и создание 1 pandas датафрейма
# датафрейм будет хранить и отображать табличные данные для нас

import pandas as pd
import numpy as np
df = pd.DataFrame()


# In[2]:


type(df)


# In[3]:


# df - название датафрейма
# ['name'] - название колонки
# [n, n, n] - структура словаря и таблицы

df['STATS'] = [9, 10, 7]


# In[4]:


# добавить колонку
df['PROG'] = [8, 5, 10]


# In[5]:


df


# In[6]:


display(df)


# In[7]:


# обращение к колонке таблицы
df['STATS']


# In[8]:


# .name - атрибут, выводит имя колонки
df['STATS'].name


# In[9]:


# .dtype - атрибут, выводит тип данных, содержащихся в колонке
df['STATS'].dtype


# In[10]:


# .values - атрибут, выводит NumPy массив
df['STATS'].values


# In[11]:


# dataframe, где 1 коллонка типа pandas, а внутри - массив NumPy


# In[12]:


type(df['STATS'].values)


# In[13]:


type(df['STATS'])


# In[14]:


df['AVERAGE'] = (df['STATS'] + df['PROG']) / 2
df['AVARAGE'] = (df['STATS'] + df['PROG']) / 10
df


# In[15]:


df['PROG']


# In[16]:


df[['STATS', 'AVERAGE']]


# In[17]:


df = df[['AVERAGE', 'STATS', 'PROG']]


# In[18]:


df


# In[19]:


# .columns - атрибут, выводит объект со всеми колонками
df.columns


# In[20]:


# замена названия колонок
df.columns = ['AV', 'STATS', 'PROG']
df


# In[21]:


# .index - атрибут, выводит индексацию
df.index


# In[22]:


# замена объекта в индексе
df.index = ['A', 'M', 'P']
df


# In[23]:


# достаем ряд из таблицы
df.iloc[0] # порядковый номер ряда


# In[24]:


df.loc['A'] # ряд по названию


# In[25]:


df.index = ['Alice', 'Mark', 'Petya']


# In[26]:


df


# In[27]:


df.iloc[0, 0] # обращаемся через индекс


# In[28]:


df.loc['Alice', 'STATS'] # обращаемся через названия


# In[29]:


df['STATS'][0] # через колонку


# In[30]:


df.iloc[0]


# In[31]:


pd.DataFrame({'a':[2,4], 'b':[4,5]})


# Чтение существующих таблиц и данных

# In[37]:


df_csv_1 = pd.read_csv('students.csv')
df_csv_1


# In[38]:


df_csv_2 = pd.read_csv('coffee_stats_2.csv', sep = ';', header = None, 
                       names = ['Type', 'Size', 'Sirop'] )
df_csv_2


# In[39]:


df_txt = pd.read_csv('forest.txt', sep = '\t')
df_txt


# In[40]:


rating = np.array([3.4, 2.9, 0.2, 8.3, 9.2, 3.4, 4.2])
print(rating[(rating < 1.6) | (rating >  3.5)])

