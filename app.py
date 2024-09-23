from flask import Flask

app = Flask(__name__)

@app.route("/api/python/message", methods=['GET'])  # Use 'methods' instead of 'method'
def get_message():
    return "Hello from Python API!"

if __name__ == "__main__":
    app.run(debug=True)
