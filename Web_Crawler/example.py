import psycopg2
import random


conn = psycopg2.connect(database="tinyedu", user="postgres",
                        password="ritsuka00", host="127.0.0.1", port="5432")
cur = conn.cursor()

print("Opened database successfully")


def generate_random_string(len_sep):
    random_string = ''
    random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, len_sep):
        random_string += str(random_str_seq[random.randint(0,
                             len(random_str_seq) - 1)])
    return random_string


def create_table():
    first_name = ['Nguyen', 'Le', 'Hoang', 'Tran',
                  'Dinh', 'Ha', 'Pham', 'Phan', 'Ho', 'Vu']
    last_name = ['Nam', 'Quan', 'Hoang', 'Hieu',
                 'Nguyet', 'Anh', 'Son', 'Duc', 'Yen', 'Quynh']
    acctype = ['Student', 'Teacher', 'Admin']

    cur = conn.cursor()
    cur.execute("DELETE FROM users")
    for i in range(10):
        username = generate_random_string(4)
        password = generate_random_string(6)
        sql_query = "INSERT INTO users VALUES ( %s, %s, %s, %s,%s)"
        sql_insert = (first_name[random.randint(
            0, 9)], last_name[random.randint(0, 9)], username, password, acctype[random.randint(0, 2)])
        cur.execute(sql_query, sql_insert)
    conn.commit()
    print("Operation done successfully")


def Insert_student():
    std_id = input("Enter student ID:")
    first_name = input("First Name:")
    last_name = input("Last Name:")
    gender = input("Gender:")
    clazz_id = input("Class ID:")
    sql_insert = (std_id, first_name, last_name, gender, clazz_id)
    sql_query = "INSERT INTO student (student_id,first_name,last_name,gender,address,clazz_id) VALUES (%s, %s, %s, %s,'Nghe An',%s) "
    cur.execute(sql_query, sql_insert)
    conn.commit()
    print("Successful")


def check(records, column, table_name):
    sql = "SELECT " + column + " FROM " + table_name
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        if row[0] == records:
            return 1
    return 0


def update_student():

    while True:
        stu_id = str(input("Enter student ID:"))
        a = check(stu_id, 'student_id', 'student')
        if a == 1:
            break
        else:
            print("Student ID not found")

    update = input("Update in column: ")
    new = input("New value:")
    sql_query = "UPDATE student SET " + update + \
        " = %s WHERE student_id = %s"
    sql_insert = (new, stu_id)
    cur.execute(sql_query, sql_insert)
    conn.commit()
    print("Successful")


def delete():
    while True:
        username = str(input("Enter username:"))
        a = check(username, 'username', 'users')
        if a == 1:
            break
        else:
            print("username not found")

    sql_query = "DELETE FROM users WHERE username = %s"
    sql_insert = (username,)
    cur.execute(sql_query, sql_insert)
    conn.commit()


def display(table_name):
    cur.execute("SELECT * FROM " + table_name)
    rows = cur.fetchall()
    for row in rows:
        print(row)


# root.mainloop()
if __name__ == '__main__':
    create_table()
    # Insert_student()
    # update_student()
    # display('student')
    delete()
    cur.close()
    conn.close()
