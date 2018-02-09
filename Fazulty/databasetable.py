import sqlite3
conn=sqlite3.connect('main.db')
c=conn.cursor()

c.execute("""CREATE TABLE reg_stud(id INTEGER primary key,name text,regno text  unique,password text,specialization text,mobile real unique,mail text unique,supervisor text)""");
c.execute("""CREATE TABLE reg_fac(id INTEGER primary key,name text,uid text  unique,password text,specialization text,mobile real unique,mail text unique,hours real)""");
c.execute("""CREATE TABLE allot(id INTEGER primary key,fname text,sname text,specialization text)""")

