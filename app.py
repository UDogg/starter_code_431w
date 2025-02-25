from flask import Flask, render_template, request, redirect
import sqlite3 as sql

app = Flask(__name__)
host = 'http://127.0.0.1:5000/'

def get_db_connection():
    connection = sql.connect('database.db')
    connection.row_factory = sql.Row
    return connection

# initialize the table for CRUD functinality
def init_db():
    connection = get_db_connection()
    connection.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            pid INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            UNIQUE(firstname, lastname)
        );
    ''')
    cursor = connection.execute("PRAGMA table_info(patients);")
    columns = [row["name"] for row in cursor.fetchall()]
    if "active" not in columns:
        # when they are active or not deleted they have value 1
        # it is abstracted out from the frontend.
        connection.execute('ALTER TABLE patients ADD COLUMN active INTEGER DEFAULT 1;')
    connection.commit()
    connection.close()

init_db()

#Landing page endpoint, it just returns a dropdown menu in index.html
@app.route('/')
def index():
    # Jinja2 templating engine
    return render_template('index.html')

# Business logic, non duplicate single tuple graphical population
@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    error = None
    if request.method == 'POST':
        first_name = request.form['FirstName']
        last_name = request.form['LastName']
        connection = get_db_connection()
        # shows tables below form to show live update
        row = connection.execute('SELECT * FROM patients WHERE firstname = ? AND lastname = ?', (first_name, last_name)).fetchone()
        if row: # row exsits
            if row['active'] == 1:
                error = "Duplicate entry: Patient already exists."
            else: # set a pid for each patient
                connection.execute('UPDATE patients SET active = 1 WHERE pid = ?', (row['pid'],))
                connection.commit()
        else: # no row, append tuple
            connection.execute('INSERT INTO patients (firstname, lastname) VALUES (?, ?);', (first_name, last_name))
            connection.commit()
        connection.close()
    connection = get_db_connection()
    patients = connection.execute('SELECT pid, firstname, lastname FROM patients WHERE active = 1;').fetchall()
    connection.close()
    # Jinja2 templating engine
    return render_template('add.html', error=error, patients=patients)


@app.route('/delete', methods=['GET', 'POST'])
def delete_patient():
    error = None
    cleared = request.args.get('cleared')
    if request.method == 'POST':
        first_name = request.form['FirstName']
        last_name = request.form['LastName']
        connection = get_db_connection()
        # Soft Delete
        cursor = connection.execute('UPDATE patients SET active = 0 WHERE firstname = ? AND lastname = ? AND active = 1;', (first_name, last_name))
        connection.commit()
        if cursor.rowcount == 0:
            # Delete error
            error = "Delete entry: Patient doesn't exist."
        connection.close()
        if error is None:
            return redirect('/')
    connection = get_db_connection()
    patients = connection.execute('SELECT pid, firstname, lastname FROM patients WHERE active = 1;').fetchall()
    connection.close()
    # Jinja2 templating engine
    return render_template('delete.html', error=error, cleared=cleared, patients=patients)

# clear is also soft delete
@app.route('/delete/clear', methods=['POST'])
def clear_table():
    connection = get_db_connection()
    connection.execute('UPDATE patients SET active = 0 WHERE active = 1;')
    connection.commit()
    connection.close()
    return redirect('/delete?cleared=1')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
