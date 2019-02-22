
# coding: utf-8

# In[ ]:


#import libraries
import numpy as np
import pandas as pd

from pandas import Series, DataFrame


# In[ ]:


#missing values
missing = np.nan


# In[ ]:


#create a series with missing values
series_obj = Series(['row1','row2',missing,'row4','row5','row6',missing,'row8'])
#display series
series_obj


# In[ ]:


#Find missing values
series_obj.isnull()


# In[ ]:


#Filling missing values

#first create a dataframe
np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape(6,6))
DF_obj


# In[ ]:


#Data Frame created does not have any missing values
DF_obj.loc[3:5,0] = missing
DF_obj.loc[1:4,5] = missing
DF_obj


# In[ ]:


#Filling missing values
DF_obj_filled = DF_obj.fillna(0)
DF_obj_filled


# In[ ]:


#filling missing values using a dictionary
DF_obj_filled = DF_obj.fillna({0:0.1 , 5:1.25})
DF_obj_filled


# In[ ]:


#Fill forward method
DF_obj_ffill = DF_obj.fillna(method = 'ffill')
DF_obj_ffill


# In[ ]:


DF_obj


# In[ ]:


#count the missing values per coln
DF_obj.isnull().sum()


# In[ ]:


#Drop rows with missing values
DF_drop = DF_obj.dropna(axis = 1)
DF_drop


# In[ ]:


#dropping rows only if all  values are missing
DF_row_missing = DF_obj.dropna(how = 'all')
DF_row_missing

