
import mysql.connector

def update_record(id,  nama, merek ):
    try:
        mysb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="toko_makeup"
        )

        mycursor = mysb.cursor()

        sql = "UPDATE produk SET id = %s, nama = %s, merek = %s WHERE id = %s"
        val = (id, nama, merek, id)
        print("Executing SQL:", sql % val)  
        mycursor.execute(sql, val)

        mysb.commit()
    
        print(mycursor.rowcount, "record(s) affected")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mycursor.close()
        mysb.close()


