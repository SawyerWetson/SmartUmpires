from flask import Flask, render_template, jsonify
import subprocess
import sys
import os

app = Flask(__name__)

@app.route("/")
def home():
    
    return render_template('frontend.html')

@app.route('/run-strikezone', methods=['POST'])
def run_strikezone():
    try:
        script_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'setup.py')
        )
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        output = result.stdout + "\n" + result.stderr
        if result.returncode == 0:
            return jsonify({'message': 'StrikeZone system started successfully!\n' + output})
        else:
            return jsonify({'message': f'Error running setup.py:\n{output}'}), 500
    except Exception as e:
        return jsonify({'message': f'Exception: {e}'}), 500

if __name__ == "__main__":
    app.run(debug=True)
