from flask import Flask, jsonify, request
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySQL database connection details
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'pratham,1234'
DB_NAME = 'globalinsightsdb'

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='pratham,1234',
        db='globalinsightsdb',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/api/data/all', methods=['GET'])
def get_all_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM market_insights")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(data=data)
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify(error=str(e)), 500

@app.route('/api/data/any/<string:query>', methods=['GET'])
def search_data(query):
    try:
        print(f"Received search query: {query}")  # Add debug print statement
        conn = get_db_connection()
        cursor = conn.cursor()
        search_query = f"%{query}%"
        cursor.execute('''SELECT * FROM market_insights WHERE 
                          sector LIKE %s OR 
                          topic LIKE %s OR 
                          title LIKE %s OR 
                          pestle LIKE %s OR 
                          source LIKE %s OR 
                          insight LIKE %s OR 
                          url LIKE %s''', 
                       (search_query, search_query, search_query, search_query, search_query, search_query, search_query))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(data=data)
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify(error=str(e)), 500

@app.route('/api/data/year/<string:year>', methods=['GET'])
def filter_by_year(year):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM market_insights WHERE start_year = %s", (year,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(data=data)
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
