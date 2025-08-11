#!/usr/bin/env python
# coding: utf-8

# # Введение в NumPy

# ### Массивы NumPy

# 1. Этот массив помагает выполнять поэлементные опперации
#    для разных видов списков и т.д
#    
#    
# 
# 2. Массив NumPy не может содержать в себе несколько типов
#    данных, поэтому превращает все в самый сильный тип
#    в данном словаре (строки, вещ.число, число, лог.выражения)

# In[1]:


x = [2, 4, 5]
y = [10, 4, 2]

print(x + y)


# In[2]:


import numpy as np

x_np = np.array(x) # .array - вызов для мат фун-ций
y_np = np.array(y)

print(x_np)
print(y_np)
print(type(x_np)) # выполнение поэлементных операций
print(x_np + y_np)
print(x_np * 2)
print(x_np ** 3)


# In[3]:


z = ['cat', 1, 8.2, False]
print(z)

z_np = np.array(z)
print(z_np) # превратилось в строку, а потом по очереди важности

print(z_np[2])
type(z_np[2])


# In[4]:


age = np.array([18, 20, 43, 23, 14, 52, 12])


# In[5]:


print(age >= 18)

print((age < 18) | (age > 35)) # | - or


# In[6]:


# фильтрация origin массива
age[(age < 18) | (age > 35)]


# In[7]:


# многразмерные массивы - матрицы
A = np.array([[2, 5, 6], [8, 10, 4]])
print(A)


# In[8]:


# shape - атрибут, размерность матрицы (ряд, колонка)
# ndim - атрибут, кол-во измерений
# size - атрибут, кол-во элементов в матрице

print(A.shape)
print(A.ndim)
print(A.size)


# In[9]:


# обращение к значениям внутри массива

print(A[1][0]) #1
print(A[1,0]) #2
print(A[1:,0]) # : - ряд, 0 - колонка


# ## Экперимент #1

# In[13]:


# засекаем время
import time

# задаем размер наших списков
size = 1000000

# объявляем списки
list1 = range(size)
list2 = range(size)

# запоминаем временную метку
initial_time = time.time()

# перемножаем элементы списков
result_list = [(a * b) for a,b in zip(list1, list2)]
list_time = time.time() - initial_time

# смотрим, сколько времени это заняло
print(f'{list_time} сек')


# In[15]:


# объявляем массивы numpy
array1 = np.arange(size)
array2 = np.arange(size)

# запоминаем временную метку
initial_time = time.time()

# перемножаем массивы 
result_array = array1 * array2
array_time = time.time() - initial_time

# сколько времени заняло
print(f'{array_time} сек')

# разница с NumPy и без
print(round(list_time/array_time),'раз')


# ## Экперимент #2

# In[17]:


size = 1000000
list  = range(size)
array1 = np.array(list1)

# 1 - суммируем все элементы списка (phyton)
initial_time = time.time()
list_sum = sum(list1)
sum1_time = time.time() - initial_time


# 2 - суммируем все элементы массива (numpy)
initial_time = time.time()
array_sum = array1.sum()
sum2_time = time.time() - initial_time


# 3 - суммируем стандартной фун-ей Phyton массив NumPy
initial_time = time.time()
array2_sum = sum(array1)
sum3_time = time.time() - initial_time

# сумма элементов списка с фун-ей sum()
print(sum1_time)
# сумма элементов массива с нативным методом .sum()
print(sum2_time)
# сумма элементов списка с фун-ей .sum()
print(sum3_time)


# In[65]:


# мораль - использовать нативные методы, 
# созданные и предназначенные для использования
# в этих специальных библиотеках

