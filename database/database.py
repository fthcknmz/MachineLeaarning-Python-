import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.execute("select * from customers")

for row in cursor:
    print("first name: " + row[1])

print("\n************************************\n")

cursor = connection.execute("""select FirstName, LastName, City
                            from customers
                            where city='Prague' or city='Berlin'
                            order by FirstName asc""")

for row in cursor:
    print("first name: " + row[0])
    print("city: " + row[2])
    print("*********")

print("\n************************************\n")

cursor = connection.execute("""select city,count(*) from customers
                            group by city
                            having count(*)>1
                            order by count(*) desc""")

for row in cursor:
    print("city: " + row[0])
    print("count: " + str(row[1]))
    print("*********")

print("\n************************************\n")

cursor = connection.execute("""select FirstName, LastName from customers
                            where FirstName like 'a%' """)

for row in cursor:
    print("name: " + row[0])

print("\n************************************\n")


connection.close()