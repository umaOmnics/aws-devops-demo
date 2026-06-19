# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Hello Azure DevOps"
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/fastapi")
def home():
    return {"message" : "Hello Aws-Uma, from FastAPI "}


# Student module CRUD for learning
class Student(BaseModel):
    id:int
    name:str
    course:str


# Dummy Data
students = [
    {"id": 1, "name": "Uma", "course": "Python-developer"},
    {"id": 2, "name": "Ravi", "course": "Java"}
]

@app.get("/students")
def getStudents():
    return students


@app.get("/students/show/{student_id}")
def studentShow(student_id: int):
    for student in students:
        if student['id'] == student_id:
            return student

    return {"message" : "student not found"}

@app.delete("/students/delete/{student_id}")
def deleteStudent(student_id : int):
    for stu in students:
        if stu["id"] == student_id:
            students.pop(student_id)
            return {
                "message" : "Deleted successfully"
            }

    return {"message" : "Student not found"}


@app.post("/students/store")
def studentsStore(stu:Student):
    students.append(stu.model_dump())

    return {
        "message" : "Student created",
        "data" : stu
    }


@app.post("/students/update/{student_id}")
def updateStudents(student_id : int, stu: Student):
    for st_data in students:
        if st_data["id"] == student_id:
            st_data["name"] = stu.name
            st_data['course'] = stu.course

            return {
                "message" : "Updated successfully",
                "data" : st_data
            }

    return {"message" : "Student not found"}
# End of student module CRUD for learning