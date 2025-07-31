from typing import Union
import json
from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    gender: int
    class_name: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/students")
def read_all_students():
    return [{"name": "xx", "id": 1, "gender":0, "class_name":"1"}, {"name": "xy", "id": 2, "gender":0, "class_name":"1"}]

@app.get("/student/{student_id}")
def read_all_students(student_id:int):
    return {"name": "student_name", "id": student_id, "gender":0, "class_name":"1"}

@app.put("/student/{student_id}")
def update_student(student_id: int, item: Student):
    return {"name": item.name, "item_id": student_id}

@app.post("/student/add")
def add_student(name: str, age: int):
    return {"name": name, "age": age, "id": 3, "gender":0, "class_name":"1"}

@app.post("/student/delete/{student_id}")
def delete_student(student_id: int):
    return {"name": "name", "age": 5, "id": student_id, "gender":0, "class_name":"1"}
