from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%d %B %Y, %I:%M:%S %p")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Deployment Dashboard</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f7fb;
                margin: 0;
                padding: 0;
            }}

            header {{
                background: #0b5ed7;
                color: white;
                padding: 25px;
                text-align: center;
            }}

            .container {{
                width: 85%;
                margin: 30px auto;
            }}

            .card {{
                background: white;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}

            .status {{
                color: green;
                font-weight: bold;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}

            th {{
                background: #eeeeee;
            }}

            footer {{
                text-align: center;
                padding: 20px;
                color: #666;
            }}
        </style>
    </head>

    <body>

        <header>
            <h1>Docker Deployment Dashboard</h1>
            <p>SWE40006 Software Deployment and Evolution</p>
        </header>

        <div class="container">

            <div class="card">
                <h2>Application Status</h2>
                <p>Status:
                    <span class="status">Running Successfully</span>
                </p>
                <p>Application Type: Python Flask Web Application</p>
                <p>Deployment Platform: Docker</p>
            </div>

            <div class="card">
                <h2>Container Information</h2>
                <table>
                    <tr>
                        <th>Property</th>
                        <th>Value</th>
                    </tr>
                    <tr>
                        <td>Container Hostname</td>
                        <td>{hostname}</td>
                    </tr>
                    <tr>
                        <td>Container Port</td>
                        <td>80</td>
                    </tr>
                    <tr>
                        <td>Current Server Time</td>
                        <td>{current_time}</td>
                    </tr>
                </table>
            </div>

            <div class="card">
                <h2>Deployment Progress</h2>
                <ul>
                    <li>Docker image built successfully</li>
                    <li>Python runtime included</li>
                    <li>Flask dependency installed</li>
                    <li>Container deployed successfully</li>
                    <li>Web application accessible from host</li>
                </ul>
            </div>

        </div>

        <footer>
            SWE40006 - Docker Deployment Activity 4.3
        </footer>

    </body>
    </html>
    """


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "Docker Deployment Dashboard"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)