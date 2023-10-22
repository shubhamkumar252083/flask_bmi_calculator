from flask import Flask, request, jsonify
import logging
from middleware import log_requests_and_responses

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
    data = request.get_json()
    # if isinstance(value, int):
    print(f'data ==> {data}')
    return jsonify(data), 201


if __name__ == '__main__':
    app.run()
