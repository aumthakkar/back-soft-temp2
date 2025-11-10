
from flask import Flask, jsonify
import socket
import time


app = Flask(__name__)


@app.route('/api/v1/info')
# ‘/’ URL is bound with hello_world() function.
def info():
    return jsonify({
        "hostname" : socket.gethostname(),
        "time" : time.ctime(),
        "message" : "You are doing great Pranav! Way to go!! <3",
        "env" : "${{values.app_env}}",
        "app_name" : "${{values.app_name}}"
    })

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({
        "status" : "up"
    })

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host="0.0.0.0")