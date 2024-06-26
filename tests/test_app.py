import pytest

@pytest.mark.usefixtures("test_database")
class TestAPI:
    def test_get_tasks(self, test_client):
        response = test_client.get("/api/tasks")
        assert response.status_code == 200
        assert response.get_json() == []

    def test_create_task(self, test_client):
        response = test_client.post("/api/tasks", json={
            "title": "Test Task",
            "description": "This is a test task"
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data["task"]["title"] == "Test Task"
        assert data["task"]["description"] == "This is a test task"
        assert not data["task"]["completed"]

    def test_complete_task(self, test_client):
        test_client.post("/api/tasks", json={
            "title": "Test Task",
            "description": "This is a test task"
        })
        response = test_client.post("/api/tasks/1/complete")
        assert response.status_code == 200
        data = response.get_json()
        assert data["task"]["completed"]

    def test_complete_taks_not_exist(self, test_client):
        response = test_client.post("/api/tasks/9999/complete")
        assert response.status_code == 404
        data = response.get_json()
        assert data["error"] == "Task not found"