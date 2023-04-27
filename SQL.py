import mysql.connector
import main

def Connect():
    connection = mysql.connector.connect(user = 'root', database = 'ctc', password = 'Sr@08302007')
    cursor= connection.cursor()
    addData = ("INSERT INTO bank (name) VALUES (%s)")
    val = ('Dollar',)
    cursor.execute(addData, val,)
    print (cursor.lastrowid)
    print(main.test)

    connection.commit()

    cursor.close()

    connection.close()
        
