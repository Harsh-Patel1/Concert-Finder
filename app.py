from flask import Flask, render_template, redirect
app = Flask(__name__)

'''
from flask import Flask, render_template, redirect, url_for, request
from flaskext.mysql import MySQL


app = Flask(
  __name__,
  template_folder='templates',  # html file folder
  static_folder='static'  # directory for static files
)

@app.route('/color_redirect', methods=['POST'])
def color_redirect():
  colors = request.form["teamcolor"]
  if colors == "Dark Navy":
    return redirect(url_for('blue'))
  else:
    return redirect(url_for('orange'))
'''
app = Flask(
  __name__,
  template_folder='templates',  # html file folder
  static_folder='static'  # directory for static files
)

@app.route('/')  # default page
def base_page():
  return render_template('index.html', ) 

@app.route('/recordings')
def recordings():
  return render_template('recordings.html', )

@app.route('/search')
def search():
  return render_template('search.html', )

if __name__ == "__main__":  # Makes sure this is the main process
  app.run(  # Starts the site
    host='0.0.0.0',  # Establishes the host, required for repl to detect the site
    port=81
    ##port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
  )

