from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello from Flask App 2 running on port 5001!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Bind to 0.0.0.0 for external access
