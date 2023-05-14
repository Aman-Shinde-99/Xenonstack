from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('contact1.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
 
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
    sql = "INSERT INTO contact (name, email, message) VALUES (%s, %s, %s)"
    values = (name, email, message)
    cursor.execute(sql, values)

    # Commit the changes and close the connection
    db.commit()
    db.close()

    return "Form submitted successfully!"


if __name__ == '__main__':
    app.run()
