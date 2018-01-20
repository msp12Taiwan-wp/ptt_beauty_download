
# coding: utf-8

# In[2]:


import MySQLdb


# In[3]:


def connectSQL():
    conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='',db='try_ptt_beauty')
    cursor=conn.cursor()
    return(conn,cursor)


# In[4]:


def insertSQL(conn,cursor,image_name,article_id):
    SQLQuery="""INSERT INTO api_picture('image_name','article_id') VALUES(%s,%s)"""
    cursor.execute(SQLQuery,(image_name,article_id))
    conn.commit()


# In[5]:


def disconnectSQL(conn):
    conn.close()
    
    
    


# In[ ]:


conn,cursor=connectSQL()


# In[10]:



insertSQL(conn,cursor,"imagename","id")


# In[9]:


disconnectSQL(conn)


# In[35]:


get_ipython().system('jupyter nbconvert --to script connectSQL.ipynb')

