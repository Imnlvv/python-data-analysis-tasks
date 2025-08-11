#!/usr/bin/env python
# coding: utf-8

# ## Рассчет Z-оценки. Pandas

# In[1]:


import pandas as pd
import numpy as np
import scipy.stats


# In[2]:


eng = pd.read_csv('eng_test.csv', sep = ';')
eng.head()


# In[3]:


eng['Score'].hist(bins = 100)


# In[4]:


toefl = eng[eng['Exam'] == 'TOEFL']
toefl['Score'].hist()


# In[5]:


ielts = eng[eng['Exam'] == 'IELTS']
ielts['Score'].hist()


# ## Поиск Z-числа

# In[6]:


X = toefl['Score'][0] # общее число данных
mean = toefl['Score'].mean() # среднее число
std = toefl['Score'].std(ddof=0) # среднеквадратичное число
print(X, mean, std)


# In[7]:


z_score = (X - mean) / std
print(z_score)


# ## Поиск Z-числа. Обратный порядок.

# In[8]:


z_new = 1.4706109
X_new = mean + z_new * std
print(round(X_new))


# ## Поиск Z-числа. С помощью функции.

# In[56]:


toefl.loc[:,'z_score'] = scipy.stats.zscore(toefl['Score'])


# In[57]:


toefl.head()


# In[58]:


ielts.loc[:, 'z_score']= scipy.stats.zscore(ielts['Score'])


# In[59]:


ielts.head()


# ## Обединение групп

# In[60]:


eng_new = pd.concat([toefl, ielts])
eng_new


# In[14]:


eng_new['z_score'].hist()


# In[15]:


eng_new[eng_new['z_score'] < -3] # выборосы


# In[16]:


eng_new.groupby('Advanced')['z_score'].mean()


# ## Выбросы

# In[18]:


bikes = pd.read_pickle('BikesDataVars.pkl')
bikes.head()


# In[19]:


bikes['Rental Count'].describe()


# In[20]:


q3 = np.percentile(bikes['Rental Count'], 75)
q1 = np.percentile(bikes['Rental Count'], 25)


# In[21]:


q3, q1


# In[22]:


iqr = q3 - q1
iqr


# In[23]:


iqr_threshold_bottom = q1 - 1.5 * iqr # нижняя граница выбросов
iqr_threshold_top = q3 + 1.5 * iqr # верхняя граница выбросов

print(iqr_threshold_bottom, iqr_threshold_top)


# In[24]:


bikes[bikes['Rental Count'] > iqr_threshold_top].shape # кол-во наблюдений, которые считаются выбросами


# In[25]:


bikes[bikes['Rental Count'] > iqr_threshold_top]['Hour'].value_counts()


# In[26]:


bikes[bikes['Rental Count'] > iqr_threshold_top]['Seasons'].value_counts()


# In[27]:


# Выбросы через стреднеквадратичное отклонение


# In[28]:


# нужно : найти среднее, верхнюю и нижнюю границу (на 2 сркв откл больше и ниже)


# In[29]:


mean = bikes['Rental Count'].mean()
std = bikes['Rental Count'].std()
std_threshold_bottom = mean - 2.5 * std
std_threshold_top = mean + 2.5 * std

print(std_threshold_bottom, std_threshold_top)


# In[30]:


bikes[bikes['Rental Count'] > std_threshold_top].shape


# In[31]:


# отфильтруем наши значения и посмотрим на мцд той выборки, где нет выбросов и где есть (оригинальная)


# In[32]:


# фильтрация без выбросов

iqr_no_outliers = bikes[bikes['Rental Count'] <= iqr_threshold_top]
std_no_outliers = bikes[bikes['Rental Count'] <= std_threshold_top]


# In[33]:


# среднее

print(bikes['Rental Count'].mean()) # оригинал
print(iqr_no_outliers['Rental Count'].mean()) 
print(std_no_outliers['Rental Count'].mean())


# In[34]:


# медиана

print(bikes['Rental Count'].median()) # оригинал
print(iqr_no_outliers['Rental Count'].median()) 
print(std_no_outliers['Rental Count'].median())


# ## Работа с пропущенными значениями

# In[35]:


bikes.head()


# In[36]:


def get_temp_cat(temp):
    if temp < 0:
        return 'Freezing'
    elif temp > 15:
        return 'Chilly'
    elif temp < 26:
        return 'Nice'
    elif temp >= 26:
        return 'Hot'
    else:
        return temp


# In[37]:


bikes.info()


# In[38]:


bikes.isna().sum() # сумма пропущенных значений в каждой ячейке


# In[39]:


type(bikes[bikes['Temperature'].isna()]['Temperature'][39])


# In[40]:


# что можно делать с пропущенными значениями?
# 1 - если большинство значений пропущены или недоступны, то стоит эту колонку выбросить


# In[41]:


# 2 - выбросить только те наблюдения, в которых есть пропущенные значения

bikes.dropna(subset = ['Temperature']).shape

# есть метод для dropna() - inplace = True. Он значит, что коллонка удалится в оригинальном датасете


# ## Заполнение пропущенных значений

# In[42]:


# метод fillna() - заполняет пустую ячейку либо числом, либо искать нужное значение в векторе и подставлять его

bikes['Temperature_Median'] = bikes['Temperature'].fillna(bikes['Temperature'].median())
bikes[bikes['Temperature'].isna()].head()


# In[43]:


bikes.head()


# In[44]:


bikes.iloc[38:42]


# In[45]:


# Заполнение случайными данными


# In[46]:


tamps_random = np.random.choice(bikes['Temperature'].dropna(), 8760)


# In[47]:


tamps_random[:100]


# In[48]:


bikes['Temperature_Random'] = bikes['Temperature'].fillna(pd.Series(tamps_random))


# In[49]:


bikes[bikes['Temperature'].isna()].head()


# In[50]:


bikes.iloc[38:42]


# In[51]:


# заполнение по медиане и некоторым категориям


# In[52]:


# bikes.groupby(bikes['Date'].dt.isocalendar().week, 'Hour'])['Temperature'].transform('median')

