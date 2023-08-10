from flask import Flask, render_template, jsonify

import random
import time
import threading
from flask import Flask, jsonify

app = Flask(__name__)

sensor_data = {}

def data_generator():
    global sensor_data
    number_of_objects = 10
    object_list = ["Human", "Car", "Tool"]
    state_list = ["Active", "Inactive"]

    while True:
        for i in range(0, number_of_objects):
            sensor_data[i] = {
                "Status": random.choice(state_list),
                "Properties": {
                    "Class": random.choice(object_list),
                    "Location": [random.randint(0, 242354), random.randint(0, 242354)],
                    "DetectionTime": random.randint(0, 23244)
                }
            }
        time.sleep(5)  # Change to 5 seconds

data_thread = threading.Thread(target=data_generator)
data_thread.start()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    global sensor_data
    return jsonify(sensor_data)

if __name__ == '__main__':
    # app.run(host='localhost', port=5000)
    app.run(host='localhost', port=8080)

