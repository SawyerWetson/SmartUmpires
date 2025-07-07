from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-strikezone', methods=['POST'])
def run_strikezone():
    try:
        subprocess.Popen(['python', 'setup.py'])  # Adjust path if needed
        return jsonify({'status': 'success', 'message': 'StrikeZone started!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
