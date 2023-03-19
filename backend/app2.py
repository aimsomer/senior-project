#comment
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
CORS(app, origins=['http://localhost:3000'])

def get_table_names():
    conn = sqlite3.connect('db2.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    conn.close()
    return [table[0] for table in tables]

def execute_query(query):
    conn = sqlite3.connect('db2.sqlite')
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

def analysis():
    conn = sqlite3.connect('db2.sqlite')
    cursor = conn.cursor()
    cursor.execute(f"SELECT BSSID, CHANNEL, POWER, SPEED FROM {get_table_names()[0]}")
    b = []
    c = []
    p = []
    s = []
    row = cursor.fetchone()
    while row is not None:
        bssid, channel, power, speed = row
        b.append(bssid)
        c.append(channel)
        p.append(power)
        s.append(speed)
        row = cursor.fetchone()
    res = []
    for i in range(1,len(b)):
        if int(p[i]) != -1 and int(s[i]) != -1 :
            res.append({'power': int(p[i]), 'speed': int(s[i]), 'status': checkPowerSpeedStatus(int(p[i]),int(s[i]))})
    return res

def speedAndRssi():
    conn = sqlite3.connect('db2.sqlite')
    cursor = conn.cursor()
    cursor.execute(f"SELECT BSSID, POWER, SPEED FROM {get_table_names()[2]}")
    b = []
    p = []
    s = []
    row = cursor.fetchone()
    while row is not None:
        bssid, power, speed = row
        b.append(bssid)
        p.append(power)
        s.append(speed)
        row = cursor.fetchone()
    res = []
    for i in range(1,len(b)):
        if int(p[i]) != -1 and int(s[i]) != -1 :
            res.append({'power': int(p[i]), 'speed': int(s[i])})
    return res
def speedAndRssi2():
    conn = sqlite3.connect('db2.sqlite')
    cursor = conn.cursor()
    cursor.execute(f"SELECT BSSID, POWER, SPEED FROM {get_table_names()[4]}")
    # print(cursor.fetchall())
    b = []
    p = []
    s = []
    row = cursor.fetchone()
    while row is not None:
        bssid, power, speed = row
        b.append(bssid)
        p.append(power)
        s.append(speed)
        row = cursor.fetchone()
    res = []
    for i in range(1,len(b)):
        if int(p[i]) != -1 and int(s[i]) != -1 :
            res.append({'power': int(p[i]), 'speed': int(s[i])})
    return res
def checkPowerSpeedStatus(power_data, speed_data):
    status = ""
    if power_data < -65 and speed_data < 250:
        status = "Poor"
    elif -65 <= power_data < -45 and 250 <= speed_data <= 550 :
        status = "Average"
    elif power_data >= -45 and speed_data >= 550:
        status = "Good"
    else:
        status = "Unknown"
        
    return status
print(speedAndRssi2())
print(get_table_names())
@app.route('/')
def hello():
    return jsonify(message="Hello"), 201

@app.route('/place1-1-ap')
def ap_place1_1():
    rows = execute_query(f"SELECT * FROM {get_table_names()[0]}")
    return jsonify(data=rows), 200

@app.route('/place1-1-sta')
def sta_place1_1():
    rows = execute_query(f"SELECT * FROM {get_table_names()[1]}")
    return jsonify(data=rows), 200

@app.route('/test')
def test():
    rows = analysis()
    return jsonify(data=rows), 200

@app.route('/plot', methods=["GET"])
def plot():
    rows = speedAndRssi()
    return jsonify(data=rows), 200

@app.route('/plot2', methods=["GET"])
def plot2():
    rows = speedAndRssi2()
    return jsonify(data=rows), 200

if __name__ == "__main__":
    app.run(debug=True)
    