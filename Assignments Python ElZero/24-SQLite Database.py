
# t~ >>>>                                                 Assignments  117 ==> 127                                            <<<<<
# ? --------------------------------- 1  -------------------------
# 1-(INT)
# 2-(TEXT)
# 3-(TINYINT)
# 4-(DATE)
# 5-(FLOAT)

# import SQLite module 
# import sqlite3

# connect database
# db = sqlite3.connect(r"E:\HACKING\Python\Assignments Python ElZero\24-SQLite\Types.db")

# setting up the cursor
# cr = db.cursor()

# create tables and fields
# cr.execute("create table if not exists Data (id INT, name TEXT, age TINYINT, dob DATE, rank FLOAT)")

# insert data into database
# cr.execute("insert into Data (id, name, age, dob, rank) values (1, 'Ali', 22, '6/2/2000', 96.5)")
# cr.execute("insert into Data (id, name, age, dob, rank) values (2, 'Ola', 20, '30/7/2002', 92.5)")

# commit changes
# db.commit()

# close database
# db.close()

# ? --------------------------------- 2  -------------------------
# import SQLite module 
# import sqlite3

# connect database
# db = sqlite3.connect(r"E:\HACKING\Python\Assignments Python ElZero\24-SQLite\index.db")

# setting up the cursor
# cr = db.cursor()

# create tables and fields
# cr.execute("create table if not exists Data (id INT UNIQUE, name TEXT UNIQUE, dates DATE UNIQUE, email TEXT UNIQUE)")

# insert data into database
# try :
#     cr.execute("insert into Data (id, name, dates, email) values (1, 'Ntfsx00', '25/5/2013', 'ntfsx00.python@hotmail.com')")
#     cr.execute("insert into Data (id, name, dates, email) values (2, 'ntfsv6', '15/8/2001', 'ntfsv6.python2@hotmail.com')")
#     cr.execute("insert into Data (id, name, dates, email) values (3, 'hany', '9/12/2003', 'hany.python3@hotmail.com')")
#     cr.execute("insert into Data (id, name, dates, email) values (4, 'khaled', '7/9/2005', 'khaled.python2@hotmail.com')")
#     cr.execute("insert into Data (id, name, dates, email) values (5, 'hamdy', '19/12/2001', 'hamdy.python2@hotmail.com')")

# except sqlite3.IntegrityError:
    # print("Bad Error sqlite3.IntegrityError")
    # pass

# cr.execute("select * from Data ORDER BY id DESC LIMIT 1") #^^ (5, 'hamdy', '19/12/2001', 'hamdy.python2@hotmail.com')

# results = cr.fetchone()

# print(results)
# ! -------- OR 
# cr.execute("select * from Data")

# results = cr.fetchall()

# print(results[-1])
# ^^ ----------
# def commit_close():
#     """Commit Changes And Close Connection To DataBase .."""
#     db.commit() # Save (Commit) Changes
#     db.close() # Close DataBase File ..
#     print("Connection To DataBase Is Closed.")
# cr.execute("select * from Data")

# results = cr.fetchall()
# my_id = []
# for mmid in results:
#     my_id.append(mmid[0])

# uid = int(input("Write Id For Delete: "))
# def dele_id(uid):
#     if uid in my_id :
#         cr.execute(f"delete from Data where id = '{uid}' ")
#         print(f"Your Id {uid} Succsessfully Deleted..")
#         print("Show Other Data:")
#         cr.execute("select * from Data")

#         results = cr.fetchall()

#         for ids,name,dates,mail in results :
#             print(f"ID => {ids}, Name => {name}, Date Of Birth => {dates}, Email => {mail}")
#         commit_close()
#     else :
#         print("ID Not Found.")
#         commit_close()

# # Make Delete function With id if in Your Id Row
# dele_id(uid)

# ! Memoryyy This ! 0VER Course And Assignments IN >>> 29/1/2026
# ! Memoryyy This ! 0VER Course And Assignments IN >>> 29/1/2026
# ! Memoryyy This ! 0VER Course And Assignments IN >>> 29/1/2026
# ! Memoryyy This ! 0VER Course And Assignments IN >>> 29/1/2026
