from flask import Flask, render_template, jsonify, request
from engine import engine

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle', methods=['POST'])
def toggle():
    if engine.is_running:
        engine.stop()
    else:
        engine.start()
    return jsonify(status="Running" if engine.is_running else "Stopped", count=engine.search_count)

@app.route('/status')
def status():
    return jsonify(status="Running" if engine.is_running else "Stopped", count=engine.search_count)

if __name__ == '__main__':
    # Flask app runs on http://127.0.0.1:5000
    print("Dashboard available at http://127.0.0.1:5000")
    app.run(debug=False, port=5000)
