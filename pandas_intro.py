
# coding: utf-8

# In[4]:

import numpy as np
import pandas as pd


# In[33]:

s = pd.Series(np.random.rand(5), index=['a', 'b', 'c', 'd', 'e'])


# In[ ]:




# In[9]:

s


# In[10]:

s.index


# In[11]:

pd.Series(np.random.rand(5))


# In[12]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[13]:

d


# In[15]:

pd.Series(d)


# In[16]:

pd.Series(.55, index = ['a', 'b', 'c', 'd', 'e'])


# In[17]:

s


# In[18]:

s[0]


# In[19]:

s[:3]


# In[20]:

s


# In[21]:

s[s > s.median()]


# In[22]:

s[[4,3,1]]


# In[23]:

## np.exp(s)


# In[24]:

s['a']


# In[25]:

s['e'] = 99999


# In[26]:

s


# In[27]:

s['e'] = 'test'


# In[28]:

s


# In[29]:

s['e']=9


# In[30]:

s


# In[31]:

'f' in s


# In[32]:

'e' in s


# In[34]:

s


# In[35]:

s.get('e')


# In[39]:

s.get('f', s.median())


# In[40]:

s


# In[41]:

s + s


# In[42]:

s[1:]


# In[43]:

s[:-1]


# In[44]:

s[:-2]


# In[45]:

s[1:] + s[:-1]


# In[46]:

s


# In[47]:

### np.exp(s)


# In[48]:

s['aaa']=9
s


# In[49]:

s = s[:-2]
s


# In[50]:

s['e'] = 1.34122


# In[51]:

s


# In[52]:

d = {'one' : pd.Series([1,2,3], index=['a','b','c']),
    'two' : pd.Series([.5,.7,6.8,9.888], index=['a','b','c','d'])}


# In[53]:

d


# In[54]:

df = pd.DataFrame(d)


# In[56]:

df


# In[57]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'), ('C', 'a10')])


# In[58]:

data


# In[59]:

data[:]=[(1,2,'Hello'), (2,3,'World')]


# In[60]:

data


# In[62]:

pd.DataFrame(data)


# In[63]:

pd.DataFrame(data, index=['first', 'second'])


# In[64]:

df


# In[65]:

df['one']


# In[67]:

df['one']


# In[74]:

df['three']=df['one']*df['two']


# In[ ]:




# In[69]:

df


# In[70]:

df['flag']=df['one']>=2


# In[71]:

df


# In[72]:

del df['three']


# In[73]:

df


# In[75]:

df


# In[76]:

myThree = df.pop('three')


# In[77]:

df


# In[78]:

myThree


# In[79]:

df['three']=myThree


# In[80]:

df


# In[81]:

df.loc['a']


# In[83]:

dir(df)


# In[84]:

df.std


# In[85]:

df


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



