import sqlite3



def selectOperation():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("select * from customers")

    for row in cursor:
        print("first name: " + row[1])

selectOperation()

def insertOperation():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers
                        (firstName,lastName,city,email)
                        values('Fethi','Cekinmez','Istanbul','fekinmez@gmail.com')""")
    connection.commit()
    connection.close()

#insertOperation()

def updateOperation():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set city='Ankara'
                        where city='Istanbul'""")
    connection.commit()
    connection.close()

#updateOperation()

def deleteOperation():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""delete from customers 
                        where city='Ankara' """)
    connection.commit()
    connection.close()    

#deleteOperation()