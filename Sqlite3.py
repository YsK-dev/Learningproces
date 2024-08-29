import sqlite3

connection=sqlite3.connect('../../../DataspellProjects/dsProject/E:/KelimeGameYsK.db')
#%%

cursor=connection.cursor()
#%%
command1='''
 CREATE TABLE IF NOT EXISTS
 stores(store_id INTEGER PRIMARY KEY,location TEXT)'''


cursor.execute(command1)



command2="""
 CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY,store_id INTEGER,total_cost FLOAT,
FOREIGN KEY (store_id) REFERENCES stores(store_id))"""

cursor.execute(command2)


cursor.execute("INSERT INTO stores VALUES (47,'Mardin,MK')")
cursor.execute("INSERT INTO stores VALUES (21,'ŞanlıUrfa,ŞU')")
cursor.execute("INSERT INTO stores VALUES (23,'Diyarbakır,DB')")
cursor.execute("INSERT INTO stores VALUES (43,'Şırnak,ŞI')")



cursor.execute("INSERT INTO purchases VALUES (47,21,14.24)")

#cursor.execute('''SELECT * FROM purchases''')
#result=cursor.fetchall()
#print(result)

#print(type(result)

print("----------------------------------------------------------------\n")

cursor.execute('''SELECT * FROM stores''')
result=cursor.fetchall()
print(result)


print("----------------------------------------------------------------\n")

print(type(result))

