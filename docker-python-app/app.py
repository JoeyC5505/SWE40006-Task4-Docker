from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = socket.gethostname()
    return f"""
    <h1>Hello World!</h1>
    <p>Python Flask application deployed using Docker.</p>
    <p>Container hostname: {hostname}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)