import random
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Fast API Demo", description="simple app to be used with github actions")

quotes = [
    "The only way to do great work is to love what you do.",
    "Life is what happens when you're busy making other plans.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Simplicity is the ultimate sophistication.",
    "It does not matter how slowly you go as long as you do not stop."
]

todos = []

class Todo(BaseModel):
    id: int = None
    task: str
    completed: bool = False

@app.get("/quote")
async def get_random_quote():
    return {"quote": random.choice(quotes)}

@app.get("/todos", response_model=List[Todo])
async def get_todos():
    return todos

@app.post("/todos", response_model=Todo)
async def create_todo(todo: Todo):
    todo.id = len(todos) + 1
    todos.append(todo)
    return todos[-1]

@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")
