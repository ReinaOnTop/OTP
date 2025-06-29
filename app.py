from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script')
def run_script():
    try:
        # Jalankan main.py
        result = subprocess.check_output(['python', 'main.py'], stderr=subprocess.STDOUT, text=True)
        return jsonify({"output": result})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.output}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
