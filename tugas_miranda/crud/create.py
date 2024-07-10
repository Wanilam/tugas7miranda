import mysql.connector

def create_record(id, nama, merek):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="toko_makeup"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO produk (id, nama, merek) VALUES ( %s, %s, %s)"
    val = (id, nama, merek)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mysb.close()