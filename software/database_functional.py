import sqlite3
def insert(id,name,age,result,date):
    mydb=sqlite3.connect('diagonis.db')
    mycursor=mydb.cursor()
    mycursor.execute("INSERT INTO History(ID,NAME,AGE, RESULT ,DATE) VALUES(?,?,?,?,?) ",(id,name,age,result,date))
    mydb.commit()
insert('1','arnav','19','normal','24-09-2024')

# select all from table function
def select_all():
    mydb=sqlite3.connect('diagonis.db')
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM HISTORY")
    TwoD_list=mycursor.fetchall()
    mydb.commit()
select_all()

# this function is for select the latest id from the table  

def select_latest_id():
    mydb=sqlite3.connect('diagonis.db')
    mycursor=mydb.cursor()
    mycursor.execute("SELECT MAX(ID) FROM HISTORY")
    latest_id=mycursor.fetchone()
    mydb.commit()

def showfilter(two_d_list):
    pass