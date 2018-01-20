
# coding: utf-8

# In[2]:


# -*- coding: MS950 -*-
import unittest
from PttWebCrawler.crawler import *
import codecs, json, os
from imgurdownloader import *
import re,os
from connectSQL import *


# In[4]:


FROM=2200
FOLDER="newDownload"
TO=2150


# In[6]:


def get_articles(index):
    c = PttWebCrawler(as_lib=True)
    t=c.parse_articles(index,index, 'beauty')
    return (t)


# In[7]:


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


# In[9]:


def download_urls(urls,article_id,index,article_num,folder):
    j=0
    conn,cursor=connectSQL()
    for url in urls:
        if url.startswith(('https://i.imgur','http://i.imgur','https://imgur','http://imgur')):# or url.startswith('http://imgur') or url.startswith('https://imgur') or url.startswith('http://i.imgur'):
            filename=str(index)+"_"+str(article_num)+"_"+str(j)
            print("Processing image:",filename,url)
            downloader = ImgurDownloader(url,FOLDER,filename)
            if (not os.path.exists(folder+"/"+filename+".jpg")) and (not os.path.exists(folder+"/"+filename+".png")):
                downloader.on_image_download(downloader.save_images())
                insertSQL(conn,cursor,filename+".jpg",article_id[article_num])
#                 connectSQL(filename+".jpg",article_id[article_num])
                print("save",filename)
            else:
                print(filename,"already exist")
        j=j+1
    disconnectSQL(conn)
        


# In[10]:


INDEX=FROM
while(INDEX>TO):
    t=".\\beauty-"+str(INDEX)+"-"+str(INDEX)+".json"
    if not os.path.exists(t):
        t=get_articles(INDEX)
    contents,titles,article_id=get_contents(t)
    i=0
    for content in contents:
        if titles[i].startswith('[正妹]'):
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
            print("start article:",titles[i])
            download_urls(urls,article_id,INDEX,i,FOLDER)
        i=i+1
    INDEX=INDEX-1
    if INDEX!=FROM:
        os.remove(t)


# In[ ]:


get_ipython().system('jupyter nbconvert --to script PttBeautyDownload.ipynb')

