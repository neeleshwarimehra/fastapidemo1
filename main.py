from numbers import Number
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException

app = FastAPI()

@app.get('/')
def index():
    return {"message":"THIS IS HOME PAGE"}

todo_list = []

# http://127.0.0.1:8000/
class Todo(BaseModel):
    id: int
    title: str
    description: str
    priority: int
    complete: bool

# http://127.0.0.1:8000/todos/

@app.post('/todos/')
def create_todo_item(todo: Todo):
    todo_list.append(todo)
    return todo

# http://127.0.0.1:8000/todos/
@app.get('/todos/')
def get_todo_list():
    return {"todos": todo_list}




# http://127.0.0.1:8000/todos/

@app.get('/todos/{todo_id}')
def get_todo_item(todo_id:int):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo

    raise HTTPException(status_code=404, detail="Todo Item not found")

# http://127.0.0.1:8000/todos/1
@app.put("/todos/{todo_id}")
def update_todo_item(todo_id:int,updated_todo_item:Todo):
    for index , todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index] = updated_todo_item
            print("Updated todo item:", updated_todo_item)
            return  {"message":"item updated", "data":updated_todo_item}

        raise HTTPException(status_code=404, detail="todo item not found")



@app.delete("/todos/{todo_id}")
def delete_todo_item(todo_id:int):
    for index , todo in enumerate(todo_list):
        if todo.id == todo_id:
            deleted_todo = todo_list.pop(index)
            return {"message":"item deleted", "data":deleted_todo}

    raise HTTPException(status_code=404, detail="todo item not found")










# {
#   "message": "item updated",
#   "data": {
#     "id": 1,
#     "title": "study DJANGO API",
#     "description": "RAG demo",
#     "priority": 1,
#     "complete": false
#   }
# }

# TESTING Basic API

# @app.get('/name={name}')
# def hello_world(name: str = "World"):
#     return {"message": f"Hello {name}!"}


# @app.get('/home')
# def home():
#     return {"message":"THIS IS HOME"}


# @app.get('/users')
# def users():
#     return {
#         "users":["Rohit","Mohit","Ram","Krishna","Radha"]
#     }

# @app.get("/{user_id}")
# def userdetails(user_id):
#          return {"user_id":f"{user_id}","message":"user available"}
   
# class User(BaseModel):
#      name: str
#      age: int
#      address: Address

# class Address(BaseModel):
#      city: str
#      pin: int



# @app.post('/create_user')

# def create_user(user:User):     
#      return {
#          "message":"user created",
#          "data":user
#      }


    
# @app.get("/{user_id}")
# def userdetails(user_id):
#     if Number({user_id}):
#          return {"user_id":f"{user_id}","message":"user available"}
#     else:
#         return {"message":"user not found"}




# {
#   "todos": [
#     {
#       "id": 1,
#       "title": "study RAG",
#       "description": "RAG demo",
#       "priority": 1,
#       "complete": false
#     },
#     {
#       "id": 3,
#       "title": "study RAG",
#       "description": "RAG demo",
#       "priority": 1,
#       "complete": false
#     },
#     {
#       "id": 4,
#       "title": "study RAG",
#       "description": "RAG demo",
#       "priority": 1,
#       "complete": false
#     }
#   ]
# }