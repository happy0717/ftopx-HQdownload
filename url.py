#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re 
import string

with open('1.txt','r',encoding='utf-8') as f:
  string = f.read()
def Find(string): 
    # findall() 查找匹配正则表达式的字符串
    url = re.findall(r"https://ftopx.com/pic/1920x1080(.+?)\"", string) 
    new_li1 = list(set(url))
    str1='\n'.join(new_li1)
    #for x in range(len(url)):
         #str11 = 'https://ftopx.com/pic/1920x1080' + str1
    return str1
      
 
str123 = ( Find(string))          
fo = open("666.txt", "w")
fo.write(str123)
fo.close()


# In[ ]:


with open('666.txt','r',encoding='utf-8') as f:
    line = f.readline()             # 调用文件的 readline()方法  
    while line:
        line = 'https://ftopx.com/pic/1920x1080'+ f.readline()
        print(line, end = '')       # 在 Python 3中使用

  


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




