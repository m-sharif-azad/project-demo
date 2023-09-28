import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  #database="test_demo"
)

mycursor = mydb.cursor()



# Create database
mycursor.execute("CREATE DATABASE test_demo")




# show databases
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)




# create student table
mycursor.execute("CREATE TABLE Students (Name VARCHAR(255),Nourse VARCHAR(255), Address VARCHAR(255), Phone INT(64))")

# Add primary key that  auto increment
mycursor.execute("ALTER TABLE students ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# insert data in the table
sql = "INSERT INTO students (Name, Nourse, Address,Phone) VALUES (%s, %s, %s, %s)"
val = [
  ('Md aminul', 'python', 'Dhaka', "01799999999"),
  ('Md arif', 'machine learning', 'Rajshahi', "01799999999"),
  ('Md arif', 'machine learning', 'Rajshahi', "01799999999"),
  ('Md arif', 'machine learning', 'Rajshahi', "01799999999")


]

mycursor.executemany(sql, val)

mydb.commit()



# fetchall for whole column and row

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# retrieve Name and Phone
mycursor = mydb.cursor()

mycursor.execute("SELECT Name, Phone FROM students")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



mycursor.execute('''
                UPDATE students
                SET Name= "Md Najmul", Nourse = "python", Address = "Joypurhat", Phone = "0173977399"
                WHERE id = 3
                ''')

mydb.commit()




# delete rows
"""
sql = "DELETE FROM students WHERE id = 4"

mycursor.execute(sql)

mydb.commit()

"""
