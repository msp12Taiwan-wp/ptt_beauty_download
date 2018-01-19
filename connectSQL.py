
# coding: utf-8

# In[7]:


import MySQLdb


# In[16]:


# conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='',db='try_ptt_beauty')


# In[32]:


# cursor=conn.cursor()


# In[33]:


# SQLQuery="""INSERT INTO PICTURE(IMAGE_NAME,SOURCE_URL)VALUES(%s,%s)"""


# In[34]:


# cursor.execute(SQLQuery,("replacetry","retry"))


# In[30]:


# conn.commit()


# In[31]:


def connectSQL(image_name,article_id):
    conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='',db='try_ptt_beauty')
    cursor=conn.cursor()
    SQLQuery="""INSERT INTO PICTURE(IMAGE_NAME,SOURCE_URL)VALUES(%s,%s)"""
    cursor.execute(SQLQuery,(image_name,article_id))
    conn.commit()

