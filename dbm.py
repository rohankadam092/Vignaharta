import pymysql as p

def connect():
    return p.connect(host="localhost",user="root",password="1234",database="pandal")


def view():
    con=connect()
    cur=con.cursor()
    sql="select * from famous_ganpati_pandal"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def viewcity(city):
    con=connect()
    cur=con.cursor()
    sql="select * from famous_ganpati_pandal where city = %s"
    cur.execute(sql,city)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data