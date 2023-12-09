import pymysql
con = pymysql.connect(host='localhost',
                      user='root',
                      password="20btad036",
                      db='pdbc',
                    )

def insert(id,name,cgpa):
   cur = con.cursor()
   sql = "insert into std values(%s,%s,%s)"
   std = (id,name,cgpa)
   cur.execute(sql,std)
   con.commit()

def update(id,name,cgpa):
   cur = con.cursor()
   sql = "update std set name=%s,gpa=%s where id=%s"
   std = (name,cgpa,id)
   cur.execute(sql,std)
   con.commit()

def select():
    cur = con.cursor()
    sql = "select * from std"
    cur.execute(sql)
    result = cur.fetchall()
    # return result
    for i in result:
      print(i[0],i[1],i[2])

# def delete(id):
#    cur = con.cursor()
#    sql = f"delete form std where id = {id}"
#    # std = tuple(id)
#    cur.execute(sql)
#    con.commit()


# insert(5,"jawa palani",5.5)

# update(5,"java palani",6.5)

# delete(5)

select()

