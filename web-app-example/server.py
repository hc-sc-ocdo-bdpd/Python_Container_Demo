import os
from flask import Flask

server = Flask(__name__)

@server.route("/")
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    # Use the PORT environment variable (required by Cloud Run) or default to 5000
    port = int(os.environ.get("PORT", 5000))
    server.run(host='0.0.0.0', port=port)
