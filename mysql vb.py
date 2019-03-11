def connect(naamdb):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database=naamdb)
    return mydb



#starten
if __name__ == "__main__":
    import mysql.connector
    
    db = connect("data")
    mycursor = db.cursor()

    #query = "SELECT * FROM LP where auteur = %s"
    #anaam = ("Polet, Sybren",)
    query = "SELECT * FROM test"
    #mycursor.execute(query,anaam)
    #mycursor.execute(query)
    #myresult = mycursor.fetchall()



    #insert of update
    sql = "INSERT INTO test (id,data) VALUES (%s, %s)"
    val = (362, "fisfhaf")
    mycursor.execute(sql, val)

    db.commit()

    print(mycursor.rowcount, "record inserted.")

    query = "SELECT * FROM test"
    #mycursor.execute(query,anaam)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for x in myresult: print(x)
