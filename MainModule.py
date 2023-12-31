import time
from StudentModule import Student
from dbConfiguration import dbconf

while True:
    print("""
          
          Welcome to School Mangement System
          1. Student Management System
          2. Teacher Management System
          3. Exit
          
          
          
          """)
    
    chi=int(input('Enter the choice:'))
    if chi==1:
        print("""Student Management System
          
          1. Create Student Account
          2. Update Student Account
          3. Delete Student Account
          4. Show Student Account
          5. Exit
          
          """)

        cho = int(input("Enter the Choice:"))
        
        #  Create Account:
        if cho == 1:
            FirstName = input("Enter First Name:")
            LastName = input("Enter Last Name:")
            gender = input("Enter Your Gender:")
            semester=int(input("Enter Your sem:"))
            Program=input("Enter program:")
            

    
            print("Processing...")
            time.sleep(2)
            studentInst = Student()  # Corrected line
            studentInst.StInfo(FirstName, LastName, gender, semester, Program)
            print("Successfully Uploaded...")

        elif cho==2:
            
            print("Enter Name to update your information:-")
            FirstName = input("Enter First Name:")
            LastName = input("Enter Last Name:")
            if FirstName and LastName == '':
                print("Error..")
            else:
                time.sleep(2)
            
                gender = input("Enter Your Gender:")
                semester = int(input("Enter Your Semester like 1,5 7 etc:"))
                Program = input("Program in which you are studying:")
            
           
            
            print('Processing...')
            print(".......")
            time.sleep(2)
            studentInsts=Student()
            studentInsts.UpdateStInfo(FirstName, LastName, gender, semester, Program)
            print("Updated data successfully")
            
            
