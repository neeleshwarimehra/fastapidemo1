from numbers import Number
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"message":"THIS IS HOME PAGE"}

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
   


class User(BaseModel):
     name: str
     age: int
     address: Address

class Address(BaseModel):
     city: str
     pin: int



@app.post('/create_user')

def create_user(user:User):     
     return {
         "message":"user created",
         "data":user
     }


    
# @app.get("/{user_id}")
# def userdetails(user_id):
#     if Number({user_id}):
#          return {"user_id":f"{user_id}","message":"user available"}
#     else:
#         return {"message":"user not found"}