# Import create_engine function
from sqlalchemy import create_engine

# # Connecting to MySQL server at localhost using PyMySQL DBAPI
# engine = create_engine("mysql+pymysql://root:pass@localhost/mydb")
#
# # Connecting to MySQL server at 23.92.23.113 using mysql-python DBAPI
# engine = create_engine("mysql+mysqldb://root:pass@23.92.23.113/mydb")
#
# # Connecting to PostgreSQL server at localhost using psycopg2 DBAPI
# engine = create_engine("postgresql+psycopg2://root:pass@localhost/mydb")
#
# # Connecting to Oracle server at localhost using cx-Oracle DBAPI
# engine = create_engine("oracle+cx_oracle://root:pass@localhost/mydb")
#
# # Connecting to MSSQL server at localhost using PyODBC DBAPI
# engine = create_engine("oracle+pyodbc://root:pass@localhost/mydb")

if __name__ == '__main__':
    connStr = "mysql+pymysql://root:root@127.0.0.1:3306/test"
    engine = create_engine(connStr)
    conn = engine.connect()
    df = conn.execute("select * from colors").fetchall()
    print(df)
    print(type(df))
