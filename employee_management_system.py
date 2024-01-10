import mysql.connector as my

def connector():
	global conn,cursor
	conn=my.connect(host="localhost",user="root",password="",database="employee")
	if conn.is_connected():
		cursor=conn.cursor()
		show("basic")
		
	else:
		return

def register_new_emp():
	emp_id=int(input("Enter the employee Id: "))
	emp_name=input("Enter the Employee Name: ")
	emp_gender=input("Enter Gender(M/F/O): ")
	emp_salary=input("Enter Salary(in rupees): ")
	emp_work_hour=int(input("Enter Working Hour: "))
	emp_post=input("Enter his/her post: ")
	emp_address=input("Enter employee Adress: ")
	emp_phone=input("Enter Phone Number: ")
	
	sql=f'INSERT INTO employee(EmpId,EmpName,Gender,Salary,WorkingHour,Post,Address,PhoneNo) VALUES({emp_id},"{emp_name}",\'{emp_gender}\',{emp_salary},{emp_work_hour},"{emp_post}","{emp_address}","{emp_phone}");'
	
	cursor.execute(sql)
	conn.commit()
	print("New employee created Successfully")
	show("basic")
	
def display_emp_detail():
	message=show("emp_detail")
	
	if message==1:
		emp_id=int(input("Enter the employee Id: "))
		sql=f"SELECT EmpName FROM employee WHERE EmpId={emp_id};"
	elif message==2:
		emp_id=int(input("Enter the employee Id: "))
		sql=f"SELECT Gender FROM employee WHERE EmpId={emp_id};"
	elif message==3:
		emp_id=int(input("Enter the employee Id: "))
		sql=f"SELECT Salary FROM employee WHERE EmpId={emp_id};"
	elif message==4:
		emp_id=int(input("Enter the employee Id: "))
		sql=f"SELECT WorkingHour FROM employee WHERE EmpId={emp_id};"
	elif message==5:
		emp_id=int(input("Enter the employee Id: "))
		sql=f"SELECT Post FROM employee WHERE EmpId={emp_id};"
	elif message==6:
		emp_id=int(input("Enter the employee Id: "))
		sql=f"SELECT Address FROM employee WHERE EmpId={emp_id};"
	elif message==7:
		emp_id=int(input("Enter the employee Id: "))
		sql=f"SELECT PhoneNo FROM employee WHERE EmpId={emp_id};"
	elif message==8:
		emp_id=int(input("Enter the employee Id: "))
		sql=f"SELECT * FROM employee WHERE EmpId={emp_id};"
	
	elif message==0:
		message("basic")
		return
	else:
		print("Wrong Choice")
		message("basic")
		return
	cursor.execute(sql)
	data=cursor.fetchall()
	for i in data:
		if message!=8:
			print(i[0])
		else:
			print(i)
		
	show("basic")
		
		
def update_emp_detail():
	message=show("emp_update")
	
	if message==1:
		emp_id=int(input("Enter the employee Id: "))
		emp_new_id=int(input("Enter the employee new Id: "))
		sql=f"UPDATE employee SET EmpId={emp_new_id} WHERE EmpId={emp_id};"
	elif message==2:
		emp_id=int(input("Enter the employee Id: "))
		emp_new_name=input("Enter the employee new name: ")
		sql=f'UPDATE employee SET EmpName="{emp_new_name}" WHERE EmpId={emp_id};'
	elif message==3:
		emp_id=int(input("Enter the employee Id: "))
		emp_new_gender=input("Enter the employee new gender(M/F/O): ")
		sql=f"UPDATE employee SET Gender='{emp_new_gender}' WHERE EmpId={emp_id};"
	elif message==4:
		emp_id=int(input("Enter the employee Id: "))
		emp_new_salary=int(input("Enter the employee new salary:"))
		sql=f"UPDATE employee SET Salary={emp_new_salary} WHERE EmpId={emp_id};"
	elif message==5:
		emp_id=int(input("Enter the employee Id: "))
		emp_new_work_hour=int(input("Enter the employee new working hour: "))
		sql=f'UPDATE employee SET WorkingHour="{emp_new_work_hour}" WHERE EmpId={emp_id};'
	elif message==6:
		emp_id=int(input("Enter the employee Id: "))
		emp_new_post=input("Enter the employee new post: ")
		sql=f'UPDATE employee SET Post="{emp_new_post}" WHERE EmpId={emp_id};'
	elif message==7:
		emp_id=int(input("Enter the employee Id: "))
		emp_new_address=input("Enter the employee new address: ")
		sql=f'UPDATE employee SET Address="{emp_new_address}" WHERE EmpId={emp_id};'
	elif message==8:
		emp_id=int(input("Enter the employee Id: "))
		emp_new_phone=input("Enter the employee new phone: ")
		sql=f'UPDATE employee SET PhoneNo="{emp_new_phone}" WHERE EmpId={emp_id};'
	elif message==0:
		show("basic")
		return
	else:
		print("\nWrong Choice\n")
		show("basic")
		return
	cursor.execute(sql)
	conn.commit()
	print("Updated Successfully")
	show("basic")
	
def delete_emp_detail():
	emp_id=int(input("Enter the employee Id: "))
	choice=input(f"\nAre You Sure To Delete Employee {emp_id}, You cannot recover it later(Y/N)?")
	
	if choice=="Y" or choice=="y":
		sql=f"DELETE from employee WHERE EmpId={emp_id}"
		cursor.execute(sql)
		conn.commit()
		print("Record Deleted Successfully\n")
	
	show("basic")
	
	
	
def show(to_show):
	if to_show=="basic":
		print("\nEnter 1 to Register new Employee\nEnter 2 to Display Employee Details\nEnter 3 To update Employee Detail\nEnter 4 to delete employee details\nEnter 0 to quit")
		choice=int(input("Enter your choice: "))
		if choice==1:
			register_new_emp()
		elif choice==2:
			display_emp_detail()
		elif choice==3:
			update_emp_detail()
		elif choice==4:
			delete_emp_detail()
		elif choice==0:
			print("\nGood Bye")
			return
		else:
			print("Wrong Choice")
	
	elif to_show=="emp_detail":
		print("\nEnter 1 to Show Employee Name\nEnter 2 to Show Gender\nEnter 3 To show Employee Salary\n Enter 4 To Show Employee Working Hour\nEnter 5 to Show Employee Post\nEnter 6 to show Employee Address\nEnter 7 to show Employee Phone Number \nEnter 8 to Show Complete Details\nEnter 0 to quit")
		choice=int(input("Enter Your Choice: "))
		return choice
		
	elif to_show=="emp_update":
		print("\nEnter 1 to Update Employee Id\nEnter 2 to Upate Employee Name\nEnter 3 to Update Gender\nEnter 4 To Update Employee Salary\n Enter 5 To Update Employee Working Hour\nEnter 6 to Update Employee Post\nEnter 7 to Update Employee Address\nEnter 8 to Update Employee Phone Number\nEnter 0 to quit")
		choice=int(input("Enter Your Choice: "))
		return choice
		
connector()