from fastapi import FastAPI


todos = []
class Task:
    def __init__(self, title: str, description: str):
        self.id = len(todos)
        self.title = title
        self.state = 0 # 0: todo, 1: done
        self.due_date = "2021-12-31"
        self.description = description
    
    def to_dict(self):
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
    return {"message": "Hello World"}

@app.get("/gregor")
async def gregor():
    return {"message": "Gregor le maxi bg de la mort qui tue"}

#Todo example
@app.get("/todos")
async def get_todos():
    data_to_dict = [todo.to_dict() for todo in todos]
    return data_to_dict

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for task in todos:
        if task.id == todo_id:
            return task.to_dict()
    return {"message": "Todo not found"}

@app.post("/todos")
async def create_todo():
    todo = Task("Foo", "Bar")
    todos.append(todo)
    return {"message": "Todo created"}

# @app.put("/todos/{todo_id}")
# async def update_todo(todo_id: int):
#     return {"title": "Foo"}

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    return {"title": "Foo"}



if __name__ == "__main__":
    print("Hello World")
    # app = FastAPI()
    # uvicorn.run(app, host="