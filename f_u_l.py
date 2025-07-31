from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

from ee import students_db

app = FastAPI()

# 学生数据模型
class Student(BaseModel):
    student_id: str
    name: str
    gender: str
    class_name: str

class CreateStudent(BaseModel):
    name: str
    gender: str
    class_name: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    class_name: Optional[str] = None


#临时数据库(使用内存列表存储)
students_db = []

students_db.append(Student(student_id='1', name='小一', gender='female', class_name='大学一班'))
students_db.append(Student(student_id='2', name='宇子', gender='male', class_name='大学二班'))

@app.get("/students/", response_model=List[Student])
def get_all_students():
    return students_db

@app.get("/student/{student_id}", response_model=Student)
def get_student(student_id:str):
    for student in students_db:
        if student.student_id == student_id:
            return student
    raise HTTPException(status_code=404, detail='学生不存在')

@app.post("/students", response_model=Student)
def add_student(student: CreateStudent):
    # 生成唯一学号
    new_id = "S" + str(uuid.uuid4().hex)[:3].upper()
    new_student = Student(
        student_id=new_id,
        name = student.name,
        gender=student.gender,
        class_name=student.class_name
    )
    students_db.append(new_student)
    return students_db
@app.delete("/student/{student_id}")
def delete_student(student_id:str):
    for i, student in enumerate(students_db):
        if student.student_id == student_id:
            deleted_student = students_db.pop(i)
            return {"message": f"已删除学生:{deleted_student.name}", "student_id":deleted_student.student_id}

    raise HTTPException(status_code=404,detail="学生不存在")


@app.put("/student/{student_id}", response_model=Student)
def update_student(student_id: str, update_data: UpdateStudent):
    for student in students_db:
        if student.student_id == student_id:
            if update_data.name:
                student.name = update_data.name
            if update_data.gender:
                student.gender = update_data.gender
            if update_data.class_name:
                student.class_name = update_data.class_name
            return student
    raise HTTPException(status_code=404, detail='学生不存在')


















