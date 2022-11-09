"""import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         port= 3306,
                                         database='tuStockOnlineDb',
                                         user='root',
                                         password='root')

  # mySql_query = "describe productos"
  # mySql_query = "select * from productos"
    mySql_query = "select * from productos where Name like '%av%'"
  #  mySql_query = "select count(*) from productos"

    cursor = connection.cursor()
    cursor.execute(mySql_query)
   
    rows=cursor.fetchall()
    for row in rows:
    	print(row)    
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed") """
