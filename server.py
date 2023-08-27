from flask import Flask, jsonify
import pyodbc
import time

app = Flask(__name__)

# Replace these with your actual SQL Server connection details
server = 'sql1'
database = 'TestDB'
username = 'SA'
password = 'P@ssw0rd'
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Function to execute SQL queries
def execute_sql_query(query):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

@app.route('/api/data', methods=['GET'])
def get_data():
    start_time = time.time()  # Capture the start time

    query = 'SELECT * FROM Inventory'
    data = execute_sql_query(query)
    
    # Convert the data to a list of dictionaries
    data_list = []
    for row in data:
        data_dict = {
            'column1': row.column1,
            'column2': row.column2,
            # Add more columns here
        }
        data_list.append(data_dict)

    end_time = time.time()  # Capture the end time
    response_time = end_time - start_time  # Calculate response time
    
    return jsonify({
        'data': data_list,
        'response_time': response_time
    })

if __name__ == '__main__':
    app.run(debug=True)
