# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 13:49:09 2019

@author: ZARA
"""

import pandas as pd
df1 =pd.read_excel("IR-F19-Project01-Input.xlsx") 

import pymysql
db = pymysql.connect('localhost', 'root', '','ir')
cursor = db.cursor()
sql = """create table project1(
             id int primary key,
             publish_date varchar(250) not null,
             title varchar(350) not null,
             url text not null, 
             summary varchar(550) not null, 
             content varchar(5550) not null,
             thumbnail text not null)"""
cursor.execute(sql)
db.close()

from sqlalchemy import create_engine

# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="",
                               db="ir"))

df1.to_sql('project1', con = engine, if_exists = 'replace', chunksize = 1000)