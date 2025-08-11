#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# Работа с датасетом

# In[2]:


books = pd.read_csv('books.csv')
books.head()


# In[3]:


books.info()


# In[4]:


bk = books[(books['num_pages'] > 1000)]
bk


# In[5]:


bk.shape


# In[6]:


books[books['publisher'] == 'Scholastic Inc'].shape


# In[7]:


books[(books['language_code'] != 'eng') & (books['ratings_count'] >= 500)].shape


# In[8]:


books


# In[9]:


round(822/10063, 2)


# In[10]:


bs = books[(books['language_code'] == 'eng') & (books['num_in_ser'] == 0)]
bs.shape


# In[11]:


round((6335/10063)* 100,2)


# In[12]:


books['num_pages'].sort_values()


# In[13]:


books['num_pages'].max()


# In[14]:


books[books.num_pages == books.num_pages.max()]


# In[15]:


books['title'].value_counts(ascending = True)


# In[16]:


count_values = books['title'].value_counts(ascending = False)
print(count_values)


# In[17]:


books_r = books['ratings_count'].min()


# In[18]:


books_r


# In[19]:


books_n = books['num_pages'].max()


# In[20]:


books_n


# In[23]:


books[books['num_pages'] == 6576.0]


# In[24]:


books['ratings_count'].sort_values()


# In[25]:


books[["mounth","day", "year"]] = books["publication_date"].str.split("/",expand=True)


# In[26]:


books[["mounth","day", "year"]] = books[["mounth","day", "year"]].astype("int64")


# In[27]:


books.info()


# In[28]:


books["century"] = books["year"].apply(lambda x: x // 100 if x % 100 == 0 else 1 + (x // 100))


# In[29]:


type(books["century"])


# In[30]:


books


# In[31]:


books[books['century'] == 19]


# In[32]:


books['num_coauthors'] = books['authors'].apply(lambda x: x.count('/') + 1)


# In[33]:


books


# In[34]:


books['num_coauthors'].max()


# In[35]:


books[books['num_coauthors'] == 51]


# Практика

# In[36]:


def c_page(x):
    if x < 100:
        return "до 100 стр."
    if 100 < x > 500:
        return "от 100 до 500 стр."
    if 500 < x > 1000:
        return "от 500 до 1000 стр."
    if x > 1000:
        return "от 1000 стр."


# In[54]:


books['pages_category'] = books['num_pages'].apply(c_page)
books_2 = books[(books['pages_category'] == 'от 100 до 500 стр.') & (books['century'] == 20)]
books_3 = books_2[(books_2['ratings_count'] >= 100)]
books_3['average_rating'].max()


# In[41]:


books_3[books_3['average_rating'] == 4.7]


# In[42]:


books_0 = books['ratings_count'] > 0


# In[43]:


books_0.min()


# In[44]:


filtered_books = books[books['ratings_count'] > 0]
max_pages_book = filtered_books.loc[filtered_books['num_pages'].idxmax()]
publication_date = max_pages_book['publication_date']
print(publication_date)


# In[46]:


books


# Сохранение обновленного датасета (.csv и .pkl)

# In[47]:


books.to_csv('booksVars.csv', index = False)
df = pd.read_csv('booksVars.csv')
df.info()


# In[48]:


books.to_pickle('booksVars.pkl')
df = pd.read_pickle('booksVars.pkl')
df.info()


# Еще практики

# In[49]:


def c_page(x):
    c_page = ''
    if x <= 100:
        c_page = "до 100 стр."
    if 100 < x < 500:
        c_page = "от 100 до 500 стр."
    if 500 <= x < 1000:
        c_page = "от 500 до 1000 стр."
    if x >= 1000:
        c_page = "от 1000 стр."
    return c_page


# In[50]:


df.pages_category = df.num_pages.apply(c_page)


# In[51]:


hund = df[df.pages_category == 'от 100 до 500 стр.']
df1 = hund[(hund.century == 20) & (hund.ratings_count >= 100)]


# In[52]:


df1.average_rating.max()


# In[53]:


df1[df1.average_rating == 4.72]['title_ser']

