import sqlite3

student_data = sqlite3.connect("student.db")
c = student_data.cursor()

def add_student(a):
    #To add detais in table
    global total
    z = f"INSERT INTO student_name VALUES ({a}, {total});"
    student_data.execute(z)
    student_data.commit()

a = int(input('''press 1 to add details of student\npress 2 to get result by name\npress 3 to get result by roll number'''))

b=""
if a== 1:
    subject = int ( input ( "Enter Number of Subject" ) )
    z = ""

    for i in range ( 1, subject + 1 ) :
        if i < subject :
            c = input ( f"Name of subject {i}" )
            z = z + c + "INT, "
        if i == subject :
            c = input ( f"Name of subject {i}" )
            z = z + c

    # Create Tables
    try :
        x = f"CREATE TABLE student_name(Rollnumber INT, Name, {z}, Total_Marks INT);"
        student_data.execute ( x )
    except sqlite3.OperationalError :
        student_data.execute ("DROP TABLE student_name;")
        x = f"CREATE TABLE student_name(Rollnumber INT, Name, {z}, Total_Marks INT);"
        student_data.execute ( x )
        print ( "Table already exist" )

    d=input("give roll number")
    b = b + d +", "
    e = input ( "Name of student" )
    b = b +"'"+ e + "'"+", "
    total = 0
    for i in range ( 0, subject ) :
        if i < subject-1:
            f = input ( f"{e}'s marks of subject {i+1}" )
            total = total + int(f)
            b = b + f + ", "
        if i == subject-1:
            f = input ( f"{e}'s marks of subject {i+1}" )
            total = total + int(f)
            b = b + f
    add_student(b)

if a==2:
    g = input("Give Name of Student")
    h = f"SELECT * FROM student_name where Name ={g}"
    d = c.execute(h)
    for i in d:
        print("******************************************************************************************************")
        print(f"\tRoll number {i[0]}\n\tName {i[1]}\n\tTotal Marks {i[-1]}\n")
        print("******************************************************************************************************")

if a==3:
    aa = input("Give Roll number of Student")
    bb = f"SELECT * FROM student_name where Rollnumber = {aa} "
    cc = c.execute(bb)
    for i in cc:
        print("******************************************************************************************************")
        print(f"\tRoll number {i[0]}\n\tName {i[1]}\n\tTotal Marks {i[-1]}\n")
        print("******************************************************************************************************")


student_data.close()