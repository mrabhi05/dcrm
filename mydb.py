import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'abhi05',
)


cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE dcrm")

print("All Done!!")