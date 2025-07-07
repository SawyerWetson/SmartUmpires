import os

app.route('/run-strikezone', methods=['POST'])
def run_strikezone():
    try:
        # Go up two levels: from ui/webapp/ to SmartUmpires/
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
