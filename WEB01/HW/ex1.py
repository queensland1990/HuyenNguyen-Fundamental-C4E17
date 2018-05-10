from flask import Flask, redirect
app = Flask(__name__)


@app.route('/about-me')
def intro():
    return "Hi, I am Huyen Nguyen. Now, I have just quited my job in a local bank. I will matriculate Wisconsin School of Business this autum. My hobby is to play with dogs, all kinds of dogs"

@app.route('/school')
def school():
    return redirect('http://techkids.vn', code=303)

if __name__ == '__main__':
  app.run(debug=True)
