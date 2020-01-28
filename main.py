from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return "Hi!"

@app.route('/home')
def home():
  return render_template('home.html', aktiva_lapa = 'home')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  #info no datubazes
  return render_template('contact.html', phone = 22140077)

@app.route('/params')
def params():
  return request.args

@app.route('/post_req', methods = ['POST'])
def post_req():
  return request.args


if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5232, threaded = True, debug = True)