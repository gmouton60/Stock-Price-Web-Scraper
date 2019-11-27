#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

html_url = 'https://finance.yahoo.com/quote/REKR?p=REKR'
fetch = uReq(html_url)
data_html= fetch.read()
fetch.close()
soup_data= soup(data_html, "html.parser")
html_div = soup_data.find("div",{"class":"My(6px) Pos(r) smartphone_Mt(6px)"})
data= html_div.find('span').text
print("The price of Rekor Stock is currently: "+ data)



# In[ ]:




