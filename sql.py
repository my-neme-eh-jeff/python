import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="3103", database="sample5"
)
cursor = mydb.cursor()

# cursor.execute("""
#                create database sample4;
#                """)
# cursor.execute('show tables;')
# print(cursor.fetchall())
# cursor.execute("CREATE TABLE table4(id INT,name VARCHAR(25),marks INT,age INT,class VARCHAR(3))")
# mydb.commit()

user_command = int(input("enter a number 1) insert 2) retreive 3) delete 4) update : "))
if user_command == 1:
    cursor.execute(
        """
                   insert into table4 values
                   (1,'name1',24,19,'A'),
                   (2,'name2',22,18,'B'),
                   (3,'name3',20,20,'A'),
                   (4,'name4',20,19,'A'),
                   (5,'name5',19,18,'B'),
                   (6,'name6',23,19,'B'),
                   (7,'name7',21,20,'B');
                   """
    )
    mydb.commit()
elif user_command == 2:
    cursor.execute("select * from table4;")
    res = cursor.fetchall()
    for i in res:
        print(i)

elif user_command == 3:
    cursor.execute("delete from table4 where id=6;")
    print("after delete : ")
    mydb.commit()
    cursor.execute("select * from table4;")
    res = cursor.fetchall()
    for i in res:
        print(i)

elif user_command == 4:
    cursor.execute("update table4 set marks =10 where id =7;")
    mydb.commit()
    print("after upadte : ")
    cursor.execute("select * from table4;")
    res = cursor.fetchall()
    for i in res:
        print(i)