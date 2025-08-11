#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[8]:


books = pd.read_csv("books.csv")
books.head()


book = 'books.csv'
books = pd.read_csv(book, index_col='Unnamed: 0', on_bad_lines='skip')
books.head()


# In[15]:


books.info()


# In[16]:


books.shape


# In[11]:


books.columns


# In[12]:


books[["authors", "language_code", "publication_date"]]


# In[14]:


books["text_reviews_count"].head()


# In[18]:


books.info()


# In[19]:


books.columns

