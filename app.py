from flask import Flask, request, jsonify
from vod_recovery import manual_vod_recover

app = Flask(__name__)

@app.route('/', methods=["POST"])
def hello_world():
    # Ensure the request has a JSON content type
    if request.is_json:
        # Retrieve JSON data from the request body
        json_data = request.get_json()

        # Access specific values from the JSON data
        name = json_data.get('streamer_name', 'camila')
        number = json_data.get('stream_id', '43549753755')
        timestamp = json_data.get('timestamp', '2024-02-03 00:01:31')

        # Call your function with the extracted data
        result = manual_vod_recover(name, number, timestamp)

        # You can return the result as JSON if needed
        return jsonify(result)
    else:
        # Return an error response if the request body is not JSON
        return jsonify({'error': 'Invalid JSON in request body'}), 400