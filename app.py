from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(
  __name__,
  template_folder='templates',  # html file folder
  static_folder='static'  # directory for static files (CSS, JavaScript, videos, etc..)
)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#importing SQL models


# Routes and Flask configuration
@app.route('/')  # default page
def base_page():
  return render_template('index.html', ) 

@app.route('/recordings')
def recordings():
  return render_template('recordings.html', )

@app.route('/search')
def search():
  return render_template('search.html', )

@app.route('/search_redirect', )
def search_redirect():
  #years = User.query.all()
  #return 'Hello, these are the users: {}'.format(users)
  '''
  year = request.form["year"]
  if year == "2021":
    return alert("2020221")
    #return redirect(url_for('blue'))
  else:
    return alert("NOT 2021")
    #return redirect(url_for('orange'))'''

if __name__ == "__main__":  # Makes sure this is the main process
  app.run(  # Starts the site
    host='0.0.0.0',  # Establishes the host, required for repl to detect the site
    port=81
  )

