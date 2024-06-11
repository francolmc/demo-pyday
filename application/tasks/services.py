from application.extensions import db
from application.tasks.models import Task

def get_all_tasks():
    tasks = Task.query.all()
    return tasks

def create_task(data):
    if not data or not 'title' in data or not 'description' in data:
        return {
            "error": "Invalid input"
        }, 400
    
    new_task = Task(title=data['title'], description=data['description'])
    db.session.add(new_task)
    db.session.commit()
    
    return {
        "message": "Task created successfully",
        "task": {
            "id": new_task.id,
            "title": new_task.title,
            "description": new_task.description,
            "completed": new_task.completed
        }
    }, 201

def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.complete()
        db.session.commit()
        return {
            "message": "Task completed successfully",
            "task": {
                "id": task.id,
                "completed": task.completed
            }
        }, 200
    return {
        "error": "Task not found"
    }, 404