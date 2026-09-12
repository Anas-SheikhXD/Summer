from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # Creates your main Application Object; Everything gets attached to this Functions 

class Task(BaseModel):
    title: str
    done: bool = True


tasks = [] # acting as an normal python list for our database for now

# GET EndPoint , used to retrieve all the tasks
@app.get("/tasks")
 # SHOWS THE WAY on What task to perform after getting a cetain request with GET

# The actual function that runs and returns all the appended tasks inside the tasks list by the diff users using the POST HTTP Method 
def get_tasks(): 
    return tasks
#POST EndPoint , used to create a new task 
@app.post("/tasks")

def create_task(task:dict):
    tasks.append(task)
    return { "message": "Task Added" , "tasks": task}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id < len(tasks):
        return tasks[task_id]
    return {"Error ": "task not found"}





