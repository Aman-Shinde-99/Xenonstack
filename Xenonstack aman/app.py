from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']

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
    sql = "INSERT INTO details (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(sql, values)

    # Commit the changes and close the connection
    db.commit()
    db.close()

    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run()
