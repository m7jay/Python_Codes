
# coding: utf-8

# In[20]:


from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup


# In[51]:


def Get_Text(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return "Page not found"
    except URLError as u:
        return "URL not found"
    try:
        bs_obj = BeautifulSoup(html)
    except AttributeError as e:
        return "Attribute Not Found" 
    
    #namelist = bs_obj.findAll("title")#,{"class":"spcht"})
    #findAll(tagName,tagAttributes);**case sensitive
    #findAll(tag,attributes,recursive,text,limit,keywords)
    #find(tag,attributes,recursive,text,keywords)

    #namelist = bs_obj.findAll("span",{"class":"green"})
    #namelist = bs_obj.findAll(text="the prince")
    namelist = bs_obj.findAll(id="text")
    for name in namelist:
        print(name.get_text())
    print("Len=",len(namelist))
        
    
            


# In[52]:


text = Get_Text("http://www.google.com")
#text = Get_Text("http://www.pythonscraping.com/pages/warandpeace.html")

