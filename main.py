from fastapi import FastAPI


todos = []
class Task:
    def __init__(self, title: str, description: str):
        self.id : int = len(todos)
        self.title : str = title
        self.state : int = 0 # 0: todo, 1: done
        self.due_date :str = "2021-12-31"
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
    return {"message": "Todo not found"}

@app.post("/todos")
async def create_todo():
    """Create a new todo"""
    todo = Task("Foo", "Bar")
    todos.append(todo)
    return {"message": "Todo created"}



@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    """Delete a todo"""
    for task in todos:
        if task.id == todo_id:
            todos.remove(task)
            return {"message": "Todo deleted"}
    return {"message": "Todo not found"}