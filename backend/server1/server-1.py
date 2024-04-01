from flask import Flask
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Update the URL to use the IP address of flask_app2 service
FLASK_APP2_IP = "172.28.0.2"  # Update this with the actual IP address

@app.route('/')
def index():
    url = f"http://{FLASK_APP2_IP}:5001"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text  
    else:
        return 'Failed to fetch response from Flask App 2'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
