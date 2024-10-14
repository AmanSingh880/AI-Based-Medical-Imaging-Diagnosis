import sqlite3
def insert(id,name,age,P_Pos,result,date):
    mydb=sqlite3.connect('diagonis.db')
    mycursor=mydb.cursor()
    mycursor.execute("INSERT INTO History(ID,NAME,AGE,P_POS, RESULT ,DATE) VALUES(?,?,?,?,?,?) ",(id,name,age,P_Pos,result,date))
    mydb.commit()
# insert('1','arnav','19','0','normal','24-09-2024')

# select all from table function
def select_all():
    mydb=sqlite3.connect('diagonis.db')
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM HISTORY")
    TwoD_list=mycursor.fetchall()
    TwoD_list.reverse()
    print(TwoD_list)
    mydb.commit()
# select_all()

# this function is for select the latest id from the table  

def select_latest_id():
    mydb=sqlite3.connect('diagonis.db')
    mycursor=mydb.cursor()
    mycursor.execute("SELECT *FROM HISTORY")
    latest_id=mycursor.fetchall()
    latest_id.reverse()
    mydb.commit()
    return latest_id[0][0]
print(select_latest_id())