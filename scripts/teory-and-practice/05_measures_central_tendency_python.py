#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


bikes = pd.read_pickle('BikesDataVars (1).pkl')
bikes.head()


# ### Среднее арифметическое

# In[3]:


bikes['Humidity'].sum() / len(bikes['Humidity'])


# In[4]:


bikes['Humidity'].mean()


# ### Медиана

# In[5]:


hum_sorted = bikes['Humidity'].sort_values().reset_index(drop = True) # сортируем влажность (по возрастанию)
print(len(hum_sorted))

ind_1, ind_2 = int(len(hum_sorted) / 2), int(len(hum_sorted) / 2 + 1)
print(ind_1, ind_2)

print((hum_sorted[ind_1] + hum_sorted[ind_2]) / 2)


# In[6]:


bikes['Humidity'].median()


# ### Мода

# In[7]:


bikes['Humidity'].value_counts().head(2)


# In[8]:


bikes['Humidity'].mode()


# In[9]:


bikes['Humidity'].hist(bins = 100)


# In[10]:


bikes.describe() # возвращение dataframe, в котором для каждой кол-венной переменной дается информация о медиане и тд


# In[11]:


bikes[['Temperature', 'Humidity']].describe()


# In[12]:


bikes['Humidity'].describe()


# #### groupby

# In[13]:


bikes.groupby('Hour')['Rental Count'].mean()


# In[14]:


bikes.groupby('Hour')['Rental Count'].mean().plot(kind = 'bar')


# In[15]:


bikes.groupby(['Hour', 'Good Weather'])['Rental Count'].mean()


# In[16]:


bikes.groupby(['Hour', 'Good Weather'])['Rental Count'].median()


# In[17]:


bikes.groupby('Seasons')['Temperature Category'].agg(lambda x: x.value_counts().index[0])


# In[18]:


bikes.groupby('Seasons')['Temperature'].agg(['mean', 'median'])


# In[19]:


bikes.groupby('Seasons')['Temperature'].mean()


# In[20]:


bikes.pivot_table(index = 'Hour', values = ['Temperature', 'Rental Count'], aggfunc = ['median', 'mean'])


# ### Mеры разброса

# In[21]:


bikes.head()


# In[22]:


bikes_hour = pd.DataFrame(bikes.groupby('Hour')['Rental Count'].sum())


# In[23]:


bikes_hour.plot(kind = 'bar')


# 01/ Размах

# In[28]:


int(bikes_hour['Rental Count'].max() - bikes_hour['Rental Count'].min())


# 02/ Интерквартильный размах

# In[29]:


int(bikes_hour.describe()['Rental Count']['25%'])


# In[30]:


int(np.percentile(bikes_hour['Rental Count'], 25))


# In[31]:


int(np.percentile(bikes_hour['Rental Count'], 75) - np.percentile(bikes_hour['Rental Count'], 25))


# ### Для Выборки

# 03/ Дисперсия

# In[32]:


bikes_mean = bikes_hour['Rental Count'].mean()
deviations = bikes_hour['Rental Count'] - bikes_mean


sq_deviations = deviations ** 2

variance_samp = sq_deviations.sum() / (len(bikes_hour) - 1)
print(variance_samp)


# 04/ Cреднеквадратичное отклонение

# In[33]:


std_samp = np.sqrt(variance_samp)
print(std_samp)


# ### Для генеральной совокупности

# 03/ Дисперсия

# In[34]:


variance_pop = sq_deviations.sum() / len(bikes_hour)
print(variance_pop)


# 04/ Cреднеквадратичное отклонение

# In[35]:


std_pop = np.sqrt(variance_pop)
print(std_pop)


# Дисперсия и Cреднеквадратичное отклонение по формуле

# In[36]:


## выборка

bikes_var = bikes_hour['Rental Count'].var()
bikes_std = bikes_hour['Rental Count'].std()

print(bikes_var)
print(bikes_std)


# In[37]:


## ген совокупность

bikes_var_gen = bikes_hour['Rental Count'].var(ddof=0)
bikes_std_gen = bikes_hour['Rental Count'].std(ddof=0)

print(bikes_var_gen)
print(bikes_std_gen)


# ### Использование мер разброса в суммирующих и агригирующих таблицах

# In[38]:


bikes.groupby('Hour')['Rental Count'].std()


# In[39]:


bikes.groupby('Hour')['Rental Count'].agg(['mean', 'std', 'median'])


# In[40]:


def range_value(x):
    return x.max() - x.min()

bikes.pivot_table(index = 'Hour', values = ['Temperature', 'Rental Count'], aggfunc = ['var', 'std', range_value])


# Частотная таблица

# In[41]:


bikes["Temperature Category"].value_counts()


# In[42]:


bikes["Temperature Category"].value_counts(dropna = False)


# In[43]:


bikes['Good Weather'].value_counts()


# In[44]:


# группируем данные по какому-то признаку


# In[45]:


bikes.groupby('Date')['Rental Count'].sum()


# In[46]:


len(list(bikes.groupby('Date'))) 


# In[47]:


list(bikes.groupby('Date'))[0][1]


# In[48]:


bikes['Seasons'].value_counts()


# In[49]:


bikes.groupby('Seasons').size()


# In[50]:


bikes.groupby('Seasons')['Good Weather'].value_counts()


# In[53]:


bikes.groupby(['Seasons','Temperature Category'], observed=False)['Rental Count'].sum()


# Визуализация

# Кол-венные данные

# In[54]:


bikes.head()


# In[55]:


bikes['Temperature'].hist(bins = 20)  #гистограмма


# In[56]:


bikes['Temperature Category'].value_counts().plot(kind = 'bar') # стоблчатая диаграмма


# In[64]:


bikes.groupby('Temperature Category', observed=True).size().plot(kind='bar')


# In[65]:


## из нескольких категорий


# In[66]:


bikes.groupby('Seasons')['Temperature Category'].value_counts().plot(kind = 'bar')


# In[67]:


bikes.groupby('Seasons')['Temperature Category'].value_counts().unstack()


# In[68]:


bikes.groupby('Seasons')['Temperature Category'].value_counts().unstack().plot(kind = 'bar')


# In[69]:


bikes.groupby('Seasons')['Temperature Category'].value_counts().unstack().plot(kind = 'bar', stacked = True)

