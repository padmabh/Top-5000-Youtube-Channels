#!/usr/bin/env python
# coding: utf-8

# In[85]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[104]:


data=pd.read_csv('C:\\Users\\Lenovo\\Downloads\\top-5000-youtube-channels.csv')
data


# # 1. Display All Rows Except the Last 5 rows Using Head Method

# In[105]:


data.head(-5)


# # 2. Display All Rows Except the First 5 Rows Using Tail Method

# In[106]:


data.tail(-5)


# # 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)

# In[46]:


data.shape


# In[107]:


print('Number of rows: ',data.shape[0])
print('Number of Columns: ',data.shape[1])


# # 4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement

# In[108]:


data.info()


# # 5. Get Overall Statistics About The Dataframe

# In[109]:


pd.options.display.float_format='{:.2f}'.format


# In[110]:


data.describe()


# # 6. Data Cleaning  (Replace '--'  to NaN)

# In[111]:


data=data.replace('--',np.nan,regex=True)


# In[112]:


data.head(20)


# # 7. Check Null Values In The Dataset

# In[113]:


data.isnull().sum()


# In[114]:


data.dropna(axis=0,inplace=True)


# In[115]:


data.isnull().sum()


# # 8. Data Cleaning [ Rank Column ]

# In[116]:


data['Rank']=data['Rank'].str[0:-2]


# In[117]:


data['Rank']=data['Rank'].str.replace(',','').astype('int')


# In[118]:


data.dtypes


# # 9. Data Cleaning [ Video Uploads & Subscribers ]

# In[119]:


#In this we have to change the datatype from object to int as they are having only numerical values.
data['Video Uploads']=data['Video Uploads'].astype('int')


# In[120]:


data.dtypes


# In[121]:


data['Subscribers']=data['Subscribers'].astype('int')


# In[122]:


data.dtypes


# # 10. Data Cleaning [ Grade Column ]

# In[123]:


data['Grade']=data['Grade'].map({'A++ ':5,'A+ ':4,'A ':3,'A- ':2,'B+ ':1})


# In[124]:


data.dtypes


# # 11. Find Average Views For Each Channel

# In[125]:


data['Avg_Views']=data['Video views']/data['Video Uploads']


# In[126]:


data['Avg_Views']


# In[127]:


data.head()


# # 12. Find Out Top Five Channels With Maximum Number of Video Uploads

# In[128]:


data.sort_values(by='Video Uploads',ascending=False).head()


# # 13. Find Correlation Matrix

# In[129]:


data.corr()


# # 14.  Which Grade Has A Maximum Number of Video Uploads?

# In[130]:


sns.barplot(x='Grade',y='Video Uploads',data=data)


# # 15.Which Grade Has The Highest Average Views?

# In[132]:


sns.barplot(x='Grade',y='Avg_Views',data=data)


# # 16.  Which Grade Has The Highest Number of Subscribers? 

# In[133]:


sns.barplot(x='Grade',y='Subscribers',data=data)


# # 17. Which Grade Has The Highest Video Views? 

# In[134]:


sns.barplot(x='Grade',y='Video views',data=data)


# In[135]:


data.groupby('Grade').mean()


# In[ ]:




