from flask import Flask
from flask import render_template #이거 있어야 render가능!

app = Flask(__name__)
app.debug = True #개발 때 만
#app.debug = False #배포시

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

@app.route('/articles', methods=['GET'])
def articles():
    return render_template('articles.html')

if __name__ == '__main__':
    app.run()