from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI()

# 学生数据模型
class Student(BaseModel):
    student_id: str
    name: str
    gender: str
    class_name: str

# 创建学生模型（用于添加学生）
class CreateStudent(BaseModel):
    name: str
    gender: str
    class_name: str

# 更新学生模型
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    class_name: Optional[str] = None

# 临时数据库 (使用内存列表存储)
students_db = []

# 添加示例数据
students_db.append(Student(student_id="S001", name="张三", gender="男", class_name="高一(1)班"))
students_db.append(Student(student_id="S002", name="李四", gender="女", class_name="高一(2)班"))

# 获取所有学生信息
@app.get("/students", response_model=List[Student])
async def get_all_students():
    return students_db

# 获取单个学生信息
@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: str):
    for student in students_db:
        if student.student_id == student_id:
            return student
    raise HTTPException(status_code=404, detail="学生不存在")

# 添加学生
@app.post("/students", response_model=Student)
async def add_student(student: CreateStudent):
    # 生成唯一学号
    new_id = "S" + str(uuid.uuid4().hex)[:3].upper()
    new_student = Student(
        student_id=new_id,
        name=student.name,
        gender=student.gender,
        class_name=student.class_name
    )
    students_db.append(new_student)
    return new_student

# 删除学生
@app.delete("/students/{student_id}")
async def delete_student(student_id: str):
    for i, student in enumerate(students_db):
        if student.student_id == student_id:
            deleted_student = students_db.pop(i)
            return {"message": f"已删除学生: {deleted_student.name}", "student_id": student_id}
    raise HTTPException(status_code=404, detail="学生不存在")

# 更新学生信息
@app.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: str, update_data: UpdateStudent):
    for student in students_db:
        if student.student_id == student_id:
            if update_data.name:
                student.name = update_data.name
            if update_data.gender:
                student.gender = update_data.gender
            if update_data.class_name:
                student.class_name = update_data.class_name
            return student
    raise HTTPException(status_code=404, detail="学生不存在")