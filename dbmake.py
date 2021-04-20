import pymysql
import hashlib as hl
import os

def make_information():
    query = "INSERT INTO users (name, email, username, password) VALUES ('"
    info_list = []

    print('enter name:',end = '')   
    name = str(input())
    query += name
    info_list.append({'name' : name})
    query += "', '"

    print('enter email:',end = '')
    email = str(input())
    query += email
    info_list.append({'email' : email})
    query += "', '"

    print('enter username:',end = '')
    username = str(input())
    query += username
    info_list.append({'username' : username})
    query += "', '"

    print('enter password:',end = '')
    password = str(hl.sha1(bytes(str(input()),'utf-8')))[-19:-1]
    query += password
    info_list.append({'password' : password})
    query += "');"

    return query

def _compare(inp, db_cursor, attribute):
    query = 'SELECT ' + attribute + ' FROM' + ' users'
    db_cursor.execute(query)
    info = db_cursor.fetchall()
    for data in info:
        if data[0] == inp:
            return True
    
    return False

def check_information(db):
    cursor = db.cursor()
    print('enter name:',end = '')
    name = str(input())
    chk = _compare(name, cursor ,'name')
    if chk is False:
        print('Name ', end = '')
        return False
    #info_list = []
    #info_list.append({'name' : name})

    print('enter email:',end = '')
    email = str(input())
    chk = _compare(email, cursor ,'email')
    if chk is False:
        print('Email ', end = '')
        return False
    #info_list.append({'email' : email})

    print('enter username:',end = '')
    username = str(input())
    chk = _compare(username, cursor ,'username')
    if chk is False:
        print('Username ', end = '')
        return False
    #info_list.append({'username' : username})
    '''
    print('enter password:',end = '')
    password = str(hl.sha1(bytes(str(input()),'utf-8')))[-19:-1]
    print(password)
    chk = _compare(password, cursor ,'password')
    if chk is False:
        print('Password ', end = '')
        return False
    '''
    print('Inserted Information is Exist on Database')
    return True

def access(host, port, user, password,db_name):
    db = pymysql.connect(
        host=host,
        port=port,
        user=user,
        passwd=password,
        db = db_name
        )
    return db, db.cursor()

def user_interface():
    print("############################")
    print("#1. insert                 #")
    print("#2. search                 #")
    print("#q or Q. EXIT              #")
    print("############################")
    


def main():
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = '1234'
    db = 'busan'
    database, cursor = access(host,port,user,passwd,db)
    command = 'temp'
    escape = ['q','Q','EXIT','exit']
    while(command not in escape):
        user_interface()
        command = str(input())
        if command in escape:
            print('bye bye')
            break

        if command == 'insert' or command == '1':
            cursor.execute(make_information())
            database.commit()
            continue
    
        elif command == 'search' or command == '2':
            chk = check_information(database)
            if chk is False:
                print('Not Exist in database or Wrong Information')
            continue

        else:
            print('wrong execution')
            continue
        


    #query = "INSERT INTO `users` (`name`, `email`, `username`, `password`) VALUES ('HS', 'adrain@nga.com', 'adrain', '12345');"
    #database.commit()
    #cursor.execute(query)
    #query = 'SELECT name FROM users'
    #cursor.execute(query)
    #topic = cursor.fetchall()
    #print(topic[0][0])
    #query = 'SELECT * FROM topic'
    #query = 'CREATE TABLE `topic` (`id` int(11) NOT NULL AUTO_INCREMENT,`title` varchar(100) NOT NULL,`body` text NOT NULL,`author` varchar(30) NOT NULL,`create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY (id)) ENGINE=innoDB DEFAULT CHARSET=utf8;'
    #query = "INSERT INTO topic (title, body, author) VALUES ('BUSAN', 'GALMEGI', 'HH');"
    #cursor.execute(query)
    #database.commit()
    #query = 'SELECT * FROM topic'
    #cursor.execute(query)
    #topic = cursor.fetchall()
    #print(topic)
    #cursor.commit()
    #cursor.close()
    #topic = cursor.fetchall()
    #print(topic)

if __name__ == '__main__':
    main()