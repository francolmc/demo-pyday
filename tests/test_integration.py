import pytest

@pytest.mark.usefixtures("test_database")
class TestIntegration:
    def test_create_and_complete_task(self, test_client):
        response = test_client.post("/api/tasks", json={
            "title": "Test Task",
            "description": "This is a test task"
        })
        assert response.status_code == 201
        response = test_client.post("/api/tasks/1/complete")
        assert response.status_code == 200
        data = response.get_json()
        assert data["task"]["completed"]