# dbConfiguration.py

import mysql.connector

class DatabaseConfiguration:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='079812@#$',
                database='Module'
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            raise  # Reraise the exception to terminate the program

    


dbconf = DatabaseConfiguration()
