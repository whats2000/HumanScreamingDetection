# Import necessary modules
import torch
from flask import Flask, render_template, jsonify

from ModelEval import process_file
from RecordSound import record_sound

app = Flask(__name__)

model = torch.load('Models/model_2023-10-10--17-02-06.pt')

# Define a route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to start recording
@app.route('/start_record', methods=['POST'])
def start_record():
    record_sound(44100, 10)

    return 'Recording Completed'

# Route to evaluate the recorded voice
@app.route('/evaluate_voice', methods=['POST'])
def evaluate_voice():
    evaluation_result = process_file('SoundRecord/recorded.wav', model)

    # Convert NumPy boolean to Python boolean
    evaluation_result = bool(evaluation_result)

    # Return the evaluation result as JSON
    return jsonify({'result': evaluation_result})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
