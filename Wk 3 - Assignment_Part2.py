#!/usr/bin/env python
# coding: utf-8

# # Wk3 - Pulling table from Wikipedia_ Part 1

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import pandas as pd
url='https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
df=pd.read_html(url, header=0)[0]
df.head()


# In[4]:


df.info()


# Only process the cells that have an assigned borough. Ignore cells with a borough that is Not assigned

# In[5]:


df.drop(df[df['Borough']=="Not assigned"].index,axis=0, inplace=True)
df.head()


# In[6]:


df1 = df.reset_index()
df1.head()


# In[7]:


df1.info()


# In[8]:


df2= df1.groupby('Postcode').agg(lambda x: ','.join(x))
df2.head()


# More than one neighborhood can exist in one postal code area. For example, in the table on the Wikipedia page, you will notice that M5A is listed twice and has two neighborhoods: Harbourfront and Regent Park. These two rows will be combined into one row with the neighborhoods separated with a comma as shown in row 11 in the above table.
# If a cell has a borough but a Not assigned neighborhood, then the neighborhood will be the same as the borough. So for the 9th cell in the table on the Wikipedia page, the value of the Borough and the Neighborhood columns will be Queen's Park.

# In[9]:


df2.loc[df2['Neighbourhood']=="Not assigned",'Neighbourhood']=df2.loc[df2['Neighbourhood']=="Not assigned",'Borough']
df3 = df2.reset_index()
df3.head()


# In[10]:


df3['Borough']= df3['Borough'].str.replace('nan|[{}\s]','').str.split(',').apply(set).str.join(',').str.strip(',').str.replace(",{2,}",",")
df3.head()


# Use the .shape method to print the number of rows of your dataframe.

# In[11]:


df3.shape


# # Part 2

#  Geocoder package or the csv file to create the dataframe

# In[20]:


df_geo = pd.read_csv("http://cocl.us/Geospatial_data")
df_geo.head()


# In[21]:


df_geo.rename(columns={"Postal Code": "Postcode"}, inplace=True)
df_geo.head()


# In[33]:


df_final = df3.merge(df_geo, on="Postcode", how="left")
df_final.head()


# In[ ]:





# In[ ]:





# In[ ]:




