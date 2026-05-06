    from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    task = {
        "id": len(tasks) + 1,
        "title": data.get("title")
    }
    tasks.append(task)
    return jsonify(task)

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t["id"] != id]
    return jsonify({"message": "Deleted"})
    
if __name__ == "__main__":
    app.run(debug=True)