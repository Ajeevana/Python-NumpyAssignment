#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Use NumPy program to generate an array of 15 random numbers 
from a standard normal distribution


# In[54]:


import numpy as np
rand_num = np.random.normal(0,1,15)
rand_num


# In[52]:


'''Create an array of 20 linearly spaced points between 0 and 1


# In[53]:


np.linspace(0, 1, 20)


# In[ ]:


'''declare a numpy array of values from 1 to 100 and make it into a 10*10 matrix


# In[55]:


import numpy as np
array = np.arange(100).reshape(10,10)
array


# In[ ]:


'''using the previously defined matrix print rows 1,5,6


# In[56]:


print(array[0])
print(array[4])
print(array[5])


# In[ ]:


'''using the same matrix print values from 3rd row 2nd column to 5th row 8th column


# In[57]:


print(array[2:5,1:8])


# In[ ]:


'''Write a code to generate a 1000 random numbers each in the range(0,1)
such that the count of all random points like are almost same


# In[58]:


from random import seed
from random import random
seed(1)
for _ in range(1000):
    value = random()
    print(value)


# In[ ]:


'''Write the commands to get standard deviation, mean, mode, median for a given vector


# In[59]:


import numpy as np
from scipy import stats
array=[110,12,140,34,56,78,69,20,34]
print(np.std(array))
print(np.mean(array))
print(np.median(array))
print(stats.mode(array))


# In[ ]:


'''''''''''''''''''''''''''''''''''''''THANKYOU'''''''''''''''''''''''''''''''''''''''''''''''

