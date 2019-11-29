import psycopg2
from psycopg2 import Error

            connection=psycopg2.connect(user="proy", password="proy",host="127.0.0.1",port="5432",database="proy")
            cursor=connection.cursor()
            try:
                createTableQuery='''Create TABLE IF NOT EXISTS SENSORBME280
                    (ID SERIAL  PRIMARY KEY,
                    HUMEDAD    REAL    NOT NULL,
                    PRESION        REAL    NOT NULL,
                    TEMPERATURA       REAL    NOT NULL);'''
                cursor.execute(createTableQuery)
                connection.commit()
                print('Table created successfully in PostgresSQL')
            except:
                (Exception,psycop2.DatabaseError) as error:
                print("Error while creating PostgreSQL table", error)print('Table already created')
                
            try:
                
                addTableQuerry="INSERT INTO SENSORBME280 (humedad,presion,temperatura) VALUES (%0.2f,%0.2f,%0.2f);" %(Humedad,Presion,Temperatura)
                print(addTableQuerry)
                cursor.execute(addTableQuerry)
                connection.commit()
            finally:
                
                if (connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")
