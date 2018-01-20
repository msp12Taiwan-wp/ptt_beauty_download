
# coding: utf-8

# In[2]:


import MySQLdb
import time
import datetime

# In[3]:


def connectSQL():
    conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='',db='beauty')
    cursor=conn.cursor()
    return(conn,cursor)


# In[4]:


def insertSQL(conn,cursor,image_name,article_id):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    SQLQuery="INSERT INTO images(image_name,article_id,created_at) VALUES('%s','%s','%s')"%(image_name,article_id,timestamp)
    cursor.execute(SQLQuery)
    conn.commit()


# In[5]:


def disconnectSQL(conn):
    conn.close()
    
    
    



