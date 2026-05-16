from fastapi import FastAPI
from enum import IntEnum
from typing import List, Optional
from pydantic import BasemModel,Field


api = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM  = 2
    HIGH =1 

class TodoBase(BaseModel):
    todo_name : str = Field(...,min_length=3, max_length=512)
    todo_description: str = Field(...,description = 'descrption of the todo')
    priority: Priority =Field(...,default = Priority.LOW,descriptiomn = 'priority of the todo')


class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    todo_name : Optional[str] = Field(...,min_length=3, max_length=512)
    todo_description: Optional[str]   = Field(...,description = 'descrption of the todo')
    priority: Optional[Priority]=Field(...,default = Priority.LOW,descriptiomn = 'priority of the todo')
     

class todo(TodoBase):
    pass



all_todos = [
    {'todo_id':1 , 'todo_name':'Sports','todo_description':'Go to the gym'},
    {'todo_id':2 , 'todo_name':'Study','todo_description':'Do tutorials'},
    {'todo_id':3 , 'todo_name':'Rest','todo_description':'Take a nap'},
    {'todo_id':4 , 'todo_name':'Socialise','todo_description':'Hangout'},
    {'todo_id':5 , 'todo_name':'Meditate','todo_description':'Do Yoga'},

]





 


@api.get('/')
def index():
    return {'message':'Hello World'}


@api.get('/todos/{todo_id}')
def get_todo(todo_id):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'result' : todo}
             



@api.get('/todos')
def get_todo(first_n:int = None):
    if first_n:
        return all_todos[:first_n]
    return all_todos


@api.post('/todos')
def create_todo(todo: dict):
    new_todo_id = max(item['todo_id'] for item in all_todos) + 1

    new_todo = {
        "todo_id": new_todo_id,
        "todo_name": todo["todo_name"],
        "todo_description": todo["todo_description"]
    }

    all_todos.append(new_todo)
    return new_todo






@api.get('/')
def index():
    return {"message": "Welcome to the Books API"}


@api.get('/books')
def get_books():
    
    return all_books


@api.put('todos/{todo_id}')
def update_todo(todo_id: int,updated_todo:dict):
    for todo in all_todos:
        if todo[todo_id] == todo_id:
            todo['todo_name'] = updated_todo['todo_name']
            todo['todo_description'] = updated_todo['todo_description']
            return todo
    return {'message':'Todo not found'}



@api.delete('todo/{todo_id}')
def delete_todo(todo_id:int, todo_list:dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            all_todos.remove(todo)
            return {'message':'Todo deleted successfully'}
    return {'message':'Todo not found'} 