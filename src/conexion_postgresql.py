import psycopg2

try: 
    Connection=psycopg2.connect(
        host= 'localhost',
        user= 'postgres',
        password= '1123434212g',
        database= 'proyectovivienda'
    )

    print("Conexión exitosa")
    cursor=Connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)
except Exception as ex:
    print(ex)