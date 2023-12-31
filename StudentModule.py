from dbConfiguration import dbconf
import mysql.connector

class Student:
    
    def StInfo(self, FirstName, LastName, gender,RollNo,semester,Program):
        query="""
            insert into Student(FirstName, LastName, gender,RollNo semester, Program)
            values (%s,%s,%s,%s,%s,%s)
        """
        data = (FirstName,LastName, gender,RollNo, semester, Program)
        dbconf.cursor.execute(query, data)
        dbconf.connection.commit()
    
    def UpdateStInfo(self,gender,RollNo,semester, Program, FirstName,LastName):
        
        query="""
            update student set gender=%s,RollNo=%s, semester=%s, Program=%s  where FirstName=%s and LastName=%s
          """ 
        data=(gender,RollNo,semester, Program, FirstName,LastName)
        
        try:
            dbconf.cursor.execute(query, data)
            dbconf.connection.commit()
            print("Update successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            dbconf.cursor.execute(query,data)
            dbconf.connection.commit()
        
        

st=Student()
        
        
    
        
        
        
        
