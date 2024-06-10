from flask import Flask, render_template, redirect, request, session, url_for
import os, requests

app = Flask(__name__, static_url_path='', static_folder='static')
app.secret_key = 'your_secret_key'
app.config['TEMPLATES_AUTO_RELOAD'] = True


API_URL = os.environ["API_URL"]
@app.route('/')
def index():
    if 'logged_in' in session:
        return render_template('index.html', api_url=API_URL)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # POST/form data
        payload = {
            'username': request.form['username'],
            'password': request.form['password']
        }

        r = requests.post("%s/login" % API_URL, json=payload)

        if (r.status_code == 200):
            session['logged_in'] = True
            return redirect('/')
        else:
            error = 'Invalid Credentials. Please try again.'
        
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/health')
def health():
    return "ok"