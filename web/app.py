from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    # Serve the static index.html
    return send_from_directory("static", "index.html")

@app.route("/api/chat/send", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    return jsonify({"reply": f"You said: {user_msg}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
