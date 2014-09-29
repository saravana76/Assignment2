
# coding: utf-8

# In[71]:

#
#
#      Hi, welcome to the home of our assignment 2! 
#                                              -- Saravana Subbiah & Lin Xiongtao
#
#
#      The theme of our data is "Customer Complaints in Financial Services in U.S.".
#          The data is mainly from data.gov, census.gov and topsy.com.
#              Please feel free to play with any data in this notebook.
#
#


# In[2]:

# Use boto to get the data saved in Amazon S3 with Access Key.
import boto
s3 = boto.connect_s3("AKIAJ4ATBBYHPUMEZOUQ","arPAmwUzS9QVXNS6ne8g4zx85/bMfs6xw6+pILWP")
key = s3.get_bucket('bigdataassign').get_key('Consumer_Complaints.csv')
key.get_contents_to_filename('Consumer_Complaints.csv')


# In[39]:

# Set graph display options and read the data.
import pandas as pd
pd.set_option('display.mpl_style', 'default') 
pd.set_option('display.line_width', 5000) 
pd.set_option('display.max_columns', 60) 
d=pd.read_csv("Consumer_Complaints.csv",parse_dates=['Date received'], index_col='Date received')


# In[120]:

# Understand the structure of the data.
d.head(2)


# In[70]:

# Total complaints of each kind of products.
figsize(10, 5)
ProductWise=d['Product'].value_counts()
ProductWise.reindex(index=ProductWise.index[::-1]).plot(kind="barh",title="Total complaints of each kind of products")


# In[68]:

# Total complaints of top 20 issues.
figsize(10, 5)
IssueWise=d['Issue'].value_counts()[:20]
IssueWise.reindex(index=IssueWise.index[::-1]).plot(kind="barh",title="Total complaints of top 20 issues")


# In[69]:

# Total complaints of top 20 sub issues.
figsize(10, 5)
SubIssueWise=d['Sub-issue'].value_counts()[:20]
SubIssueWise.reindex(index=SubIssueWise.index[::-1]).plot(kind="barh",title="Total complaints of top 20 sub issues")


# In[75]:

# Total complaints of each portal
figsize(8, 3)
PortalWise=d['Submitted via'].value_counts()
PortalWise.reindex(index=PortalWise.index[::-1]).plot(kind="barh",title="Total complaints of each portal")


# In[76]:

# Total complaints of each company
figsize(10, 5)
CompanyWise=d['Company'].value_counts()[:20]
CompanyWise.reindex(index=CompanyWise.index[::-1]).plot(kind="barh",title="Total complaints of each company")


# In[81]:

# Response Status
figsize(8, 8)
d['Company response'].value_counts().plot(kind="pie",title="Response Status")


# In[85]:

# Customer Disputed?
figsize(3, 3)
d['Consumer disputed?'].value_counts().plot(kind="pie",title="Customer Disputed?")


# In[86]:

w=d.groupby(d.index)


# In[104]:

i=0
def count(r):
    global i
    i=i+1
    return len(r)


# In[112]:

w.groupby(d['Product'])


# In[123]:

d['Timely response?']


# In[ ]:



