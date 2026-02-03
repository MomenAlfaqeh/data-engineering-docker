#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd

# Read a sample of the data
prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
df = pd.read_csv(prefix + 'yellow_tripdata_2021-01.csv.gz', nrows=100)


# In[18]:


df.head()


# In[19]:


len(df)


# In[20]:


df['VendorID']


# In[22]:


get_ipython().system('uv add sqlalchemy "psycopg[binary,pool]"')


# In[24]:


get_ipython().system('uv add psycopg2-binary')


# In[25]:


from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[26]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[27]:


df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# In[31]:


df_iter = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000
)


# In[32]:


for df_chunk in df_iter:
    print(len(df_chunk))


# In[33]:


get_ipython().system('uv add tqdm')


# In[ ]:




