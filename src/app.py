from flask import Flask
from flask import render_template #이거 있어야 render가능!
from flask import request
from flask import redirect
#from data import Articles
import pymysql
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.debug = True #개발 때 만
#app.debug = False #배포시

db = pymysql.connect(
  host='localhost',
  port = 3306,
  user = 'root',
  password = '1234',
  db = 'busan'
)

@app.route('/')
def index():
    return render_template('Prob03.html')

@app.route('/data', methods=['GET'])
def hello():
    return 'Hello, Flask!'

@app.route('/data/test')
def input():
    return render_template('index.html', data = '진자2 규격') 

@app.route('/data/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/adv', methods=['GET'])
def index_2():
    return render_template('Prob03_1.html')

@app.route('/img', methods=['GET'])
def index_3():
    return render_template('coverviewer.html')

#ARTICLES FROM DATABASE WITH SELECT
@app.route('/articles', methods=['GET'])
def articles(): 
    cursor = db.cursor()
    sql = 'SELECT * FROM topic;' #모든 topic 질의
    cursor.execute(sql)
    topics = cursor.fetchall()
    #print(topics)
    #articles = Articles()
    return render_template('articles.html',articles = topics)

#INSE   RT
@app.route('/add_articles', methods=["GET","POST"])
def add_articles(): 
    if request.method == "POST": #form으로 부터 메소드 전달.
        cursor = db.cursor()
        desc = request.form['Desc'] #원하는거
        title = request.form['Title']
        author = request.form['Author']
        sql = "INSERT INTO topic (title,body,author) VALUES (%s,%s,%s);" #삽입 쿼리
        input_data = [title,desc,author]
        #print(request.form['desc'])
        cursor.execute(sql,input_data)
        db.commit()
        return redirect("/articles") #추가 완료
    else:
        return render_template("add_articles.html") #form으로 부터 메소드 전달.
    
#DELETE
@app.route('/del_articles/<int:id>', methods=["POST"]) #form으로 부터 메소드 전달.
def del_articles(id):
    cursor = db.cursor()
    sql = "DELETE FROM topic WHERE id = %s;" #삭제문 쿼리
    cursor.execute(sql,id)
    db.commit()
    return redirect("/articles") #삭제 후 돌아가기

#EDIT
@app.route('/articles/edit/<int:id>', methods=["GET","POST"])
def edit_article(id):
    cursor = db.cursor()
    sql = "SELECT * FROM topic WHERE id = %s;"
    cursor.execute(sql,id)
    topic = cursor.fetchone()
    if request.method == "POST":
        desc = request.form['Description'] #원하는거
        title = request.form['Title']
        input_data = [title,desc,id]
        sql = "UPDATE topic SET title = %s, body = %s WHERE id = %s"
        cursor.execute(sql,input_data)
        db.commit()
        return redirect("/articles")
    else:
        return render_template("edit_article.html",article = topic) #form으로 부터 메소드 전달.

#ARTICLE FROM DATABASE WITH ID
@app.route('/articles/<int:id>/')
def article(id):
    cursor = db.cursor()
    sql = 'SELECT * FROM topic WHERE id = {}'.format(id) #호출 쿼리
    cursor.execute(sql)
    topic = cursor.fetchone()
    print(topic)
    #articles = Articles()
    #for article in articles:
    #    if article['id'] == int(id):
    #        return render_template('article.html',article = article)
    return render_template('article.html',article = topic)

@app.route('/register', methods=["GET","POST"])
def register(): 
    if request.method == "POST": #form으로 부터 메소드 전달.
        cursor = db.cursor()
        u_name = request.form['U_Name']
        sql = "SELECT id FROM users WHERE username = %s;"
        cursor.execute(sql,u_name)
        profile = cursor.fetchall()
        if len(profile) != 0:
            #중복된 아이디 입니다를 출력
            return redirect("/register")
        pswd = sha256_crypt.hash(request.form['PSWD'])
        if sha256_crypt.verify(request.form['PSWD_chk'],pswd) != True:
            return redirect("/register")
        name = request.form['Name'] #원하는거
        email = request.form['Email']
        sql = "INSERT INTO users (name,email,username,password) VALUES (%s,%s,%s,%s);" #삽입 쿼리
        input_data = [name,email,u_name,pswd]
        #print(request.form['desc'])
        cursor.execute(sql,input_data)
        db.commit()
        return redirect("/data/test") #추가 완료
    else:
        return render_template("register.html") #form으로 부터 메소드 전달.

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST": #form으로 부터 메소드 전달.
        cursor = db.cursor()
        name = request.form['U_Name'] #원하는거
        sql = "SELECT id, password FROM users WHERE username = %s;" #삽입 쿼리
        cursor.execute(sql,name)
        profile = cursor.fetchall()
        pswd = request.form['PSWD']
        
        if len(profile) != 0:
            if sha256_crypt.verify(pswd,profile[0][1]):
                #로그인 성공 출력
                return redirect("/data/test")
            else:
                #비번 틀림
                return redirect("/login")
        else :
            #아이디 틀림
            return redirect("/login")
    else:
        return render_template("login.html")

if __name__ == '__main__':
    app.run()