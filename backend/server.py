from flask import Flask, request
import os, mysql.connector
import sys

app = Flask(__name__)

mydb = mysql.connector.connect(
  host = os.environ["MYSQL_HOST"],
  user = os.environ["MYSQL_USER"],
  password = os.environ["MYSQL_ROOT_PASSWORD"],
  database = os.environ["MYSQL_DATABASE"]
)

@app.route('/')
def index():
    return "ok"

@app.route('/login', methods=['POST'])
def login():    
    if request.method == 'POST':
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM user WHERE login='admin';")
        myresult = mycursor.fetchall()
        admin = {"login": myresult[0][0], "password": myresult[0][1]}
        payload = request.get_json()
        if payload['username'] != admin['login'] or payload['password'] != admin['password']:
            return "Forbidden", 403
        else:
            return "Ok", 200

@app.route('/health')
def health():
    return "ok"