from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_random_quote():
    response = client.get("/quote")
    assert response.status_code == 200
    assert "quote" in response.json()

def test_create_todo():
    todo_data = {"task": "Test todo"}
    response = client.post("/todos/", json=todo_data)
    assert response.status_code == 200
    assert response.json()["task"] == "Test todo"
    assert "id" in response.json()
    assert response.json()["completed"] is False


def test_get_todos():
    # First create a todo
    client.post("/todos", json={"task": "Test get todos"})

    # Then fetch all todos
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_todo_by_id():
    # First create a todo and get its ID
    create_response = client.post("/todos/", json={"task": "Test get by ID"})
    todo_id = create_response.json()["id"]

    # Then fetch that specific todo
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id
    assert response.json()["task"] == "Test get by ID"


def test_get_nonexistent_todo():
    response = client.get("/todos/9999")
    assert response.status_code == 404
