from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Storm MCP!"

@app.route("/about")
def about():
    return "This is a Flask demo application created with Storm MCP!"

@app.route("/api/status")
def status():
    return jsonify({"status": "running", "message": "Flask app is healthy"})

if __name__ == "__main__":
    app.run(debug=True)
