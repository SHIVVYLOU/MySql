import os
import datetime
import pymysql

#get user from Cloud9 workspace
#(modify this variable if running on another envir0nment)
username = os.getenv('C9_USER')

#CONNECT TO THE DATABASE
connection =pymysql.connect(host='localhost',
                            user= username,
                            password= '',
                            db='Chinook')
try:
    #run a query
    with connection.cursor() as cursor:
        cursor.execute("""create table if not exists Friends(name char(20)age int, DOB datetime),""")
        # note that the above code will still display a warning (not error) if the 
        #table already exists
        
finally:
    #close the connection, regardless of whether the above was successful
    connection.close
    ()
