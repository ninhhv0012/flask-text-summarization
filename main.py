from config import DATABASE_URI
from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS




app = Flask(__name__)
CORS(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI


def connect_to_db():
    try:
        conn = psycopg2.connect(DATABASE_URI)
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None
@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    conn = connect_to_db()
    if conn is None:
        return "Database connection error", 500

    cursor = conn.cursor()

    try:
        sql = "SELECT * FROM your_table WHERE id = %s"
        cursor.execute(sql, (id,))
        data = cursor.fetchone()  # Fetch one row for ID-based lookup
        if data:
            return jsonify(data), 200
        else:
            return "Data not found", 404
    except Exception as e:
        print("Error getting data:", e)
        return "Error getting data", 500
    finally:
        cursor.close()
        conn.close()

@app.route('/data', methods=['GET'])
def get_all_data():
    conn = connect_to_db()
    if conn is None:
        return "Database connection error", 500

    cursor = conn.cursor()

    try:
        sql = "SELECT * FROM summarization order by created_at desc"
        cursor.execute(sql)
        data = cursor.fetchall()  # Fetch one row for ID-based lookup
        if data:
            return jsonify(data), 200
        else:
            return "Data not found", 404
    except Exception as e:
        print("Error getting data:", e)
        return "Error getting data", 500
    finally:
        cursor.close()
        conn.close()
@app.route('/data', methods=['POST'])
def create_data():
    data = request.get_json()  # Get data from the request body (usually JSON)

    conn = connect_to_db()
    if conn is None:
        return "Database connection error", 500

    cursor = conn.cursor()

    try:
        # Construct your INSERT statement using data from the request
        sql = "INSERT INTO summarization (text, summarization) VALUES (%s, %s)"
        cursor.execute(sql, (data['text'], data['summary']))
        conn.commit()
        return  jsonify(data), 201
    except Exception as e:
        conn.rollback()  # Rollback on error
        print("Error creating data:", e)
        return "Error creating data", 500
    finally:
        cursor.close()
        conn.close()  # Close connection
if __name__ == '__main__':
    app.run(debug=True, port=5000)
