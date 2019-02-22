
# coding: utf-8

# In[ ]:


#import libraries
import pandas as pd
import numpy as np

from pandas import Series, DataFrame


# In[ ]:


#creating a series using numpy
series_obj=Series(np.arange(8),index=['row1','row2','row3','row4','row5','row6','row7','row8'])
#display series
series_obj


# In[ ]:


#retrieving a series element
series_obj['row6']


# In[ ]:


#retrieving multiple values
series_obj[[0,5]]


# In[ ]:


#setting seed for random number generation
np.random.seed(25)
#creating a data frame object
DF_Obj=DataFrame(np.random.rand(36).reshape(6,6),index=['row1','row2','row3','row4','row5','row6'],columns=['col1','col2','col3','col4','col5','col6'])
#display dataframe
DF_Obj


# In[ ]:


#retrieving a set of elements from DataFrame
DF_Obj.loc[['row1','row2','row3'],['col1','col2','col3']]


# In[ ]:


#data slicing
series_obj['row1':'row5']


# In[ ]:


#filtering with a Scalar
DF_Obj < 0.2


# In[ ]:


#Filtering with a scalar
series_obj[series_obj <> 5]


# In[ ]:


#setting values using a scalar
series_obj[['row1','row5','row7']]=99
series_obj

