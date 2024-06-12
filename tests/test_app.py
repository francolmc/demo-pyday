import pytest
from application import create_app
from application.extensions import db
from application.tasks.models import Task

@pytest.fixture
def client():
    app = create_app(testing=True)
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
        with app.app_context():
            db.drop_all()

def test_get_tasks(client):
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert response.get_json() == []

def test_create_task(client):
    response = client.post("/api/tasks", json={
        "title": "Test Task",
        "description": "This is a test task"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["task"]["title"] == "Test Task"
    assert data["task"]["description"] == "This is a test task"
    assert not data["task"]["completed"]

def test_complete_task(client):
    client.post("/api/tasks", json={
        "title": "Test Task",
        "description": "This is a test task"
    })
    response = client.post("/api/tasks/1/complete")
    assert response.status_code == 200
    data = response.get_json()
    assert data["task"]["completed"]