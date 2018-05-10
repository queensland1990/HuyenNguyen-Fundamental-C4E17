from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    post=[
    {
        "title": "Thơ con cóc",
        "content": "Ahihi",
        "author": "queensland1990",
        "gender": 1
    },
    {
        "title": "Thơ củ lạc",
        "content": "Lạy chúa trên cao turn down for what",
        "author": "Nhật Minh",
        "gender": 0
    },
    {
        'title': "Em không nghĩ ra",
        'content': "Không nghĩ ra gì",
        'author': "Trường dingtea",
        "gender": 1
    }
    ]
    

    return render_template("index.html",posts=post)

@app.route('/c4e') #đường dẫn
def sayhi():
    return"HI, C4E17"

@app.route('/sayhi/<name>/<age>')
def sayhello(name,age):
    return"Hi {0}, you are {1} yr olds".format(name,age)

@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    return str(a+b)

if __name__ == '__main__':
  app.run(debug=True)
