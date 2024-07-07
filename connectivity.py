''' This module is designed to connect mysql with python.
    Database: 'automatedIM_DB'
    Table: 'interns' 
'''

# connectivity with MySQL
def get_rows():
    import mysql.connector

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='automatedIM_DB'
    )

    mycursor = mydb.cursor()

    # Fetching rows for auto-send!
    mycursor.execute("select * from interns where status = 'Not Done'") 
    myresult = mycursor.fetchall()

    # Preventing duplicate messages!
    mycursor.execute("update interns set status = 'Done' where status ='Not Done' ")
    mydb.commit()

    return myresult
    