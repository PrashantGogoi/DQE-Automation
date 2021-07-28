import pyodbc
import pandas as pd

# def connectToDb(connStr):
#     connObj = pyodbc.connect(connStr)
#     return connObj

if __name__ == '__main__':
    # conn = pyodbc.connect('Driver={MySQL};'
    #                       'Server=localhost;'
    #                       'Database=test;'
    #                       'Trusted_Connection=yes;')

    # Connect to MySQL
    connStr = 'DRIVER={MySQL ODBC 8.0 Unicode Driver};User=root;Password=root;Server=127.0.0.1;Database=test;Port=3306;String Types=Unicode'
    conn = pyodbc.connect(connStr)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test.colors')
    for row in cursor:
        print(row)

    # Connect to SQL Server
    # import pyodbc
    #
    # # Some other example server values are
    # # server = 'localhost\sqlexpress' # for a named instance
    # # server = 'myserver,port' # to specify an alternate port
    # server = 'tcp:myserver.database.windows.net'
    # database = 'mydb'
    # username = 'myusername'
    # password = 'mypassword'
    # cnxn = pyodbc.connect(
    #     'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    # cursor = cnxn.cursor()

    # Connect to Oracle
    # import pyodbc
    # cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=myhost;Service Name=myservicename;User=myuserid;Password=mypassword')

    #Connect to HIVE

