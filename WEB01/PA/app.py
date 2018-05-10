from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    post=[
    {
    'title': "Thơ con cóc",
    'content': "Lạy chúa trên cao, turdown 4 what",
    'author': "Minh",
    "gender": 1
    },
    {
    'title':"Thơ con ếch",
    "content":"I love you",
    "author":"boyfriend",
    "gender": 0
    }
]
    return render_template("index.html", posts=post)

# @app.route('/friend')
# def sayhi():
#     return "Hi Andy"
#
# @app.route('/sayhi/<name>/<age>')
# def sayhello(name, age):
#     return "Hi {0}, you are {1} years old".format(name,age)
#
# @app.route('/sum/<a>/<b>')
# def sum(a,b):
#     return str(int(a)+int(b))
#
# @app.route('/sum1/<int:a>/<int:b>')
# def calc(a,b):
#     return str(a+b)

if __name__ == '__main__':
  app.run(debug=True)
