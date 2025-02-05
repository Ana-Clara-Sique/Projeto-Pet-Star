from flask import Flask,render_template,request,redirect,url_for
from sqlalchemy import create_engine,column,integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url ="mysql+pymysql://root@localhost/test"
engine = create_engine(database_url,echo=True)
base = declarative_base()
