from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

tasks = []

@app.route("/welcome", methods=["GET"])
def welcome():
    return {"message": "hello"}

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data or "title" not in data:
        return {"error": "Title is required"}, 400

    task = {
        "id": str(uuid.uuid4()),
        "title": data["title"]
    }

    tasks.append(task)
    return jsonify(task)

@app.route("/tasks/<string:id>", methods=["DELETE"])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t["id"] != id]
    return {"message": "Task deleted"}

@app.route("/tasks/<string:id>", methods=["PUT"])
def update_task(id):
    data = request.get_json()

    for task in tasks:
        if task["id"] == id:
            task["title"] = data.get("title", task["title"])
            return jsonify(task)

    return {"error": "Task not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)