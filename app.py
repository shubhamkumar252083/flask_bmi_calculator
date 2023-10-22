from flask import Flask, request, jsonify
import logging
from middleware import log_requests_and_responses
from config import *
from bmi_calculator import get_bmi

app = Flask(__name__)

# Configure logging to write to a text file
log_file = "request_response_log.txt"
handler = logging.FileHandler(log_file)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# Register the custom middleware
log_requests_and_responses(app)

@app.route('/')
def hello_world():
    return '<h1>Flask app is working</h1>'


@app.route('/bmi', methods=['POST'])
def create_item():
    age = height = weight = 0
    try:
      data = request.get_json()
    except:
        data = {}
    # print(f'data ==> {data}')
    if not data:
        return jsonify(error_respose_json), 400
    
    age = data.get("age")
    height = data.get("height")
    weight = data.get("weight")

    if not isinstance(age, (int, float)) or age <= 0:
        return jsonify(age_filed_error_respose_json), 400
    
    elif not isinstance(height, (int, float)) or height <= 0:
        return jsonify(height_filed_error_respose_json), 400
    
    elif not isinstance(weight, (int, float)) or weight <= 0:
        return jsonify(weight_filed_error_respose_json), 400
    
    bmi, bmi_text = get_bmi(age, weight, height)
    return_response = {"BMI":bmi, "message":bmi_text}
    return jsonify(return_response), 200


if __name__ == '__main__':
    app.run()
