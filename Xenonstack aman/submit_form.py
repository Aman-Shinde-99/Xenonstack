from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/submit_form.py', methods=['POST'])
def submit_form():
    # Get the form data 
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']
    aadhaar = request.form['aadhaar']
    pan = request.form['pan']

    # Connect to the MySQL database
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aman@1234',
        database='xenonstack'
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Insert the form data into the database
    sql = "INSERT INTO account_opening_form (name, email, phone, address, aadhaar, pan) VALUES (%s, %s, %s, %s, %s, %s)"
    values = ()
#Aman_Shinde, shindeaman30@gmail.com, 8888497338, yavatmal, 6148482484151, 54845564652