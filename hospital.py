
import mysql.connector

db= mysql.connector.connect(host='localhost',
                             user='root',
                             password='root',
                             database='project')

#fuction creation for inserting

def insert(i,name,number,cause,doctor,amount):
    res=db.cursor()
    sql="insert into employee(sno,patient_name,room,problem,doctor_name,fees) values(%s,%s,%s,%s,%s,%s)"
    res.execute(sql,((i,name,number,cause,doctor,amount))
    db.commit()
    print("Data Insert Successfully!!!!")
    
#fuction creation for updating
def update((i,name,number):
    res=db.cursor()
    sql="update employee set company=%s where Eid=%s AND Ename=%s"
    res.execute(sql,(i,name,number))
    db.commit()
    print("Data Update Successfully!!!!")


#selection the data's
def select():
    res=db.cursor()
    sql="select * from employee"
    res.execute(sql)
    result=res.fetchall()
    print(result)
    db.commit()
    print("Data Selection Successfully!!!!")

#deleting process
    
def delete(name):
    res=db.cursor()
    sql="delete from employee where Ename=%s"
   
    res.execute(sql,(name,))
    db.commit()
    print("Data Delete Successfully!!!!")

while(True):
    print("1.Insert Data")
    print("2.Update Date")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice=int(input("Enter Your Choice:"))
    if(choice==1):
        i=input("Enter the Id")
        name=input("Enter Your Name")
        cname=input("Enter Your Company")
        insert(i,name,cname)
    elif(choice==2):
        i=input("Enter the Id")
        name=input("Enter Your Name")
        cname=input("Enter Your Company")
        update(i,name,cname)
    elif(choice==3):
        select()

    elif(choice==4):
        name=input("Enter The Name")
        delete(name)
    elif(choice==5):
        quit()
    else:
        print("Invalid Choice")
--------------------------------------------------------------------------



