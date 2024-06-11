from flask import Blueprint, request, jsonify
from application.tasks.services import get_all_tasks, create_task, complete_task

tasks_blueprint = Blueprint("tasks", __name__, url_prefix="/api")

def init_routes(app):
    app.register_blueprint(tasks_blueprint)

@tasks_blueprint.route("/tasks", methods=["GET"])
def get_tasks_route():
    tasks = get_all_tasks()
    return jsonify([{ "id": task.id, 'title': task.title, 'complete': task.completed } for task in tasks])

@tasks_blueprint.route("/tasks", methods=["POST"])
def create_task_route():
    data = request.get_json()
    response, status = create_task(data)
    return jsonify(response), status

@tasks_blueprint.route("/tasks/<int:task_id>/complete", methods=["POST"])
def complete_task_route(task_id):
    response, status = complete_task(task_id)
    return jsonify(response), status