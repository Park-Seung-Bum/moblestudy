
import pymysql


# db연결
def connect_db():
    try:
        connect_db = pymysql.connect(
            user="root",
            password="1234",
            host="127.0.0.1",
            db="mobledb",
            charset="utf8",
        )
        return connect_db
    except pymysql.Error as e:
        print("error : " + str(e))
        return None
def info_len():
    sensor_db = connect_db()                                                                                                                
    cursor = sensor_db.cursor()
    sql = "SELECT * FROM customor"
    cursor.execute(sql)
    len = cursor.fetchall()
    print(len)
    sensor_db.close()
    return len

info_len()