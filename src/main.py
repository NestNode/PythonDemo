"""
This is the main module for the Flask application.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """
    This function returns a simple HTTP response.
    """
    return "Hello World! This is a simple HTTP response."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=24006)
