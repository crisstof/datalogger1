from flask import Flask, jsonify, request
import sqlite3
import random
import threading
import time

app = Flask(__name__, static_folder="static")


# Simuler des capteurs
def simulate_sensors():
    while True:
        temp = round(random.uniform(18.0, 25.0), 1)
        conn = sqlite3.connect("db.sqlite")
        c = conn.cursor()
        c.execute("INSERT INTO sensor_data (sensor_id, value) VALUES (?, ?)", (1, temp))
        conn.commit()
        conn.close()
        time.sleep(5)


@app.route("/api/sensor/<int:sensor_id>", methods=["GET"])
def get_sensor(sensor_id):
    conn = sqlite3.connect("db.sqlite")
    c = conn.cursor()
    c.execute("SELECT * FROM sensor_data WHERE sensor_id=?", (sensor_id,))
    data = c.fetchall()
    conn.close()
    return jsonify(data)


@app.route("/")
def index():
    return app.send_static_file("index.html")


lights = {"salon": False}


# ajouter une commande allumer une lampe simulée
@app.route("/api/light/<room>", methods=["POST"])
def toggle_light(room):
    state = request.json.get("state")
    lights[room] = state
    return jsonify({"status": "ok", "room": room, "state": state})


@app.route("/api/lights", methods=["GET"])
def get_lights():
    return jsonify(lights)


threading.Thread(target=simulate_sensors).start()

if __name__ == "__main__":
    app.run(debug=True)
