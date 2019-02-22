
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup  


# In[2]:



try:
    html=urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
except HTTPError as e:
    print("Page not found!")
except URLError as url_err:
    print("URL not found!")
else:
    bs_obj=BeautifulSoup(html.read())
    print(bs_obj.h1)


# In[28]:




