
# coding: utf-8

# In[3]:


# -*- coding: MS950 -*-
import unittest
from PttWebCrawler.crawler import *
import codecs, json, os
from imgurdownloader import *
import re,os


# In[4]:


FROM=2110
TO=2110
FOLDER='./Download'


# In[5]:


c = PttWebCrawler(as_lib=True)
t=c.parse_articles(FROM, TO, 'beauty')


# In[15]:


with open(t, 'r',encoding = 'utf8') as f:
    data=json.load(f)
content=[]
title=[]
for article in data['articles']:
    content.append(article['content'])
    title.append(article['article_title'])
# content[2]
data


# In[13]:



# if not os.path.exists(directory):
#     os.makedirs(directory)
i=0
j=40
for con in content[40:len(content)]:
    text = con
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    folder=title[j].split(' ')[1].replace("?","")
#     filename
    directory='Download/'+folder
    if not os.path.exists(directory):
        os.makedirs(directory)    
    print(folder)
    i=0
    for url in urls:
        if url.startswith('http://i.imgur') or url.startswith('http://imgur'):
            filename=str(title[j]+str(i))
            
            print(filename)
            downloader = ImgurDownloader(url,FOLDER,filename)
#             i=i+1
            print("down",url)
            i=i+1
            downloader.on_image_download(downloader.save_images(folder))
            
    j=j+1
    


# In[54]:


print(filename+"_"+str(i)+"_"+str(j),url)


# In[24]:


FROM=2340
INDEX=FROM
FOLDER="Download"
while(INDEX>2300):
    t=".\\beauty-"+str(INDEX)+"-"+str(INDEX)+".json"
    if not os.path.exists(t):
        t=get_articles(INDEX)
    contents,titles,article_id=get_contents(t)
    i=0
    for content in contents:
        if titles[i].startswith('[正妹]'):
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
            if len(titles[i].split(' '))>1:
                folder=titles[i].strip()
                for k in ":;?*:<>\/|<.":
                    folder=folder.replace(k,"")
            else:
                folder="正妹"+str(INDEX)+" "+str(i)
            directory=('Download/'+folder).strip()
            if not os.path.exists(directory):
                os.makedirs(directory)
            print("start article:",folder)
            j=0
            for url in urls:
                if url.startswith(('https://i.imgur','http://i.imgur','https://imgur','http://imgur')):# or url.startswith('http://imgur') or url.startswith('https://imgur') or url.startswith('http://i.imgur'):
                    filename=str(INDEX)+"_"+str(i)+"_"+str(j)
                    print("Processing image:",filename,url)
                    downloader = ImgurDownloader(url,FOLDER,filename)
                    if (not os.path.exists(directory+"/"+filename+".jpg")) and (not os.path.exists(directory+"/"+filename+".png")):
                         if os.path.exists(directory):
                            downloader.on_image_download(downloader.save_images(folder))
                            print("save",directory,filename)
                            j=j+1
        i=i+1
    INDEX=INDEX-1
    if INDEX!=FROM:
        os.remove(t)


# In[21]:


def get_articles(index):
    c = PttWebCrawler(as_lib=True)
    t=c.parse_articles(index,index, 'beauty')
    return (t)


# In[23]:


def get_contents(t):
    with open(t, 'r',encoding = 'utf8') as f:
        data=json.load(f)
    contents=[]
    titles=[]
    article_id=[]
    for article in data['articles']:
        contents.append(article['content'])
        titles.append(article['article_title'])
        article_id.append(article['article_id'])
    print(article_id[1:5])
    return(contents,titles,article_id)


# In[25]:


def get_urls(contents,titles):
    i=0
    for content in contents:
        if titles[i].startswith('[正妹]'):
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    return(urls)
        


# In[26]:


get_ipython().system('jupyter nbconvert --to script config_template.ipynb')

