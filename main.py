# from __future__ import annotations

from fastapi import FastAPI

import json

todos : list = []
class Task:
    def __init__(self, id: int,  title: str, state :int, due_date : str, description: str):
        self.id : int = len(todos) if id == -1 else id
        self.title : str = title
        self.state : int = state # 0: todo, 1: done
        self.due_date :str = "2021-12-31" if due_date == "" else due_date
        self.description :str = description
    
    def to_dict(self):
        """Converts the object to a dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "state": self.state,
            "due_date": self.due_date,
            "description": self.description
        }
    @staticmethod
    def from_dict(input_dict : dict):
        """Converts a dictionary to an object"""
        return Task(input_dict["id"], input_dict["title"], input_dict["state"], input_dict["due_date"], input_dict["description"])


  
app = FastAPI()


@app.get("/")
async def root():
    """This is the root of the API"""
    return {"message": "Hello World"}

@app.get("/gregor")
async def gregor():
    """This is an example of a second endpoint"""
    return {"message": "Gregor le maxi bg de la mort qui tue"}

#Todo example
@app.get("/todos")
async def get_todos():
    """Display all the todos"""
    data_to_dict = [todo.to_dict() for todo in todos]
    return data_to_dict

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    """Display a specific todo"""
    for task in todos:
        if task.id == todo_id:
            return task.to_dict()
    return 404, {"message": "Todo not found"}

@app.post("/todos")
async def create_todo(id: int,  title: str, state :int, due_date : str, description: str):
    """Create a new todo"""
    
    todos.append(Task(id, title, state, due_date, description))
    return {"message": "Todo created"}



@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    """Delete a todo"""
    for task in todos:
        if task.id == todo_id:
            todos.remove(task)
            return {"message": "Todo deleted"}
    return 404, {"message": "Todo not found"}