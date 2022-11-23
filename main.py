from fastapi import FastAPI

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
    return [{"title": "Foo"}, {"title": "Bar"}]

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    return {"title": "Foo"}

@app.post("/todos")
async def create_todo():
    return {"title": "Foo"}

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int):
    return {"title": "Foo"}

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    return {"title": "Foo"}



if __name__ == "__main__":
    print("Hello World")
    # app = FastAPI()
    # uvicorn.run(app, host="