#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib-venn')


# In[2]:


#Import libraries
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


venn2(subsets = (30, 30, 10))


# In[4]:


c = venn3_circles(subsets = (20, 10, 12, 10, 9, 4, 3), linestyle='dashed', linewidth=1)
c[0].set_lw(5.0)
c[1].set_lw(8.0)
c[2].set_lw(2.0)


# In[ ]:




