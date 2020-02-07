from flask import Flask, render_template, request
from file_proc import read_file

app = Flask(__name__)


@app.route('/')
def index():
  return "<a href='/home'> Hi! </a>"

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = 22334455)

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/params')
def params():
  return request.args

@app.route('/post', methods = ['POST'])
def post():
  return request.get_json()

@app.route('/read_file')
def read_from_file():
  content = read_file()
  return content





if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 5222, threaded = True, debug = True)

