from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <h1>Hello from Jenkins! 🚀</h1>
    <p>This is a Real Web Server Deployed by CI/CD.</p>
    <p>Version: 2.0 (Dockerized)</p>
    """

if __name__ == "__main__":
    # anyone can acees in 0.0.0.0
    app.run(host='0.0.0.0', port=5000)