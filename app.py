#!venv/bin/python
from flask import Flask, jsonify, request, abort

import subprocess, os


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/command', methods=["POST"])
def command_action():
    if not request.json or not 'command' in request.json:
        abort(400)
    command = request.json['command']
    environment = os.environ.copy()

    if 'environment' in request.json:
        environment_params = request.json['environment']
        for variable, value in environment_params.iteritems():
            environment[variable] = value


    result = subprocess.Popen(command, env=environment, shell=True).pid

    result = {"result": result }
    
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")