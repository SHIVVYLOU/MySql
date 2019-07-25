import os
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
        sql = 'SELECT * FROM Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #close the connection, regardless of whether the above was successful
    connection.close
    ()
