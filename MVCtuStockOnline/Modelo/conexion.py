import mysql.connector 

try:
    conexion = mysql.connector.connect(
                                host = 'localhost',  
                                port = 3306,               
                                user = 'root',            
                                password = 'root',   
                                database = 'tuStockOnlineDB'             
                                )
    if conexion.is_connected():
                 print("LA CONEXIÓN FUE EXITOSA")
        

except:
     print("NO SE PUDO CONECTAR A LA BASE DE DATOS")

finally:
    if conexion.is_connected():
       conexion.close()
    print("LA CONEXIÓN FUE CERRADA")
    



 
  