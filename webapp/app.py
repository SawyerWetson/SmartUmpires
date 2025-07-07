from flask import Flask, render_template, jsonify, request
import subprocess
import sys
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frontend.html')

@app.route('/run-strikezone', methods=['POST'])
def run_strikezone():
    try:
        # Adjust the path if setup.py is not in the same directory
        script_path = os.path.join(os.path.dirname(__file__), 'setup.py')
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({'message': 'StrikeZone system started successfully!'})
        else:
            return jsonify({'message': f'Error running setup.py: {result.stderr}'}), 500
    except Exception as e:
        return jsonify({'message': f'Exception: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
