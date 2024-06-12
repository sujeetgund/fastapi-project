from fastapi import FastAPI
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str
    


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get a single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo not found"}

# Create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created successfully", "todos": todos}

# Update a todo

# Delete a todo