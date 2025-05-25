import os
import asyncio
from flask import Flask, request, jsonify
from subprocess import PIPE, Popen

app = Flask(__name__)

OPEN_MANUS_PATH = os.path.expanduser("~/Documents/OpenManus/main.py")

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    command = data.get("command", "").strip()

    if not command:
        return jsonify({"output": "No command provided", "success": False})

    try:
        process = Popen(["python", OPEN_MANUS_PATH], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)
        stdout, stderr = process.communicate(input=command)

        if process.returncode == 0:
            return jsonify({"output": stdout.strip(), "success": True})
        else:
            return jsonify({"output": stderr.strip(), "success": False})

    except Exception as e:
        return jsonify({"output": f"Error: {str(e)}", "success": False})

if __name__ == '__main__':
    app.run(debug=True)

