from flask import Flask, request, jsonify

app = Flask(__name__)

import json, os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

tasks = load_tasks()

@app.route("/add", methods=["POST"])
def add_task():
    data = request.get_json()
    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "status": "Pending"        
    }
    tasks.append(task)
    return jsonify({"message": "Task added!", "task": task})

@app.route("/view", methods=["GET"])
def view_tasks():
    return jsonify({"tasks": tasks})

@app.route("/delete/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted!"})
    return jsonify({"message": "Task not found!"})

@app.route("/edit/<int:task_id>", methods=["PUT"])
def edit_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data["title"]
            return jsonify({"message": "Task updated!", "task": task})
    return jsonify({"message": "Task not found!"})

@app.route("/status/<int:task_id>", methods=["PATCH"])
def update_status(task_id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = data["status"]
            return jsonify({"message": "Status updated!", "task": task})
    return jsonify({"message": "Task not found!"})

app.run(debug=True, port=5000)
