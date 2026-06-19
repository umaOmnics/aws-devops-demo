from fastapi import FastAPI
from pydantic import BaseModel

fapp = FastAPI()

@fapp.get("/fastapi")
def home():
    return {"message" : "Hello Uma, from FastAPI "}


# Student module CRUD for learning
class Student(BaseModel):
    id:int
    name:str
    course:str


# Dummy Data
students = [
    {"id": 1, "name": "Uma", "course": "Python-Dev"},
    {"id": 2, "name": "Ravi", "course": "Java-Dev"}
]

@fapp.get("/students")
def getStudents():
    return students


@fapp.get("/students/show/{student_id}")
def studentShow(student_id: int):
    for student in students:
        if student['id'] == student_id:
            return student

    return {"message" : "student not found"}

@fapp.delete("/students/delete/{student_id}")
def deleteStudent(student_id : int):
    for stu in students:
        if stu["id"] == student_id:
            students.pop(student_id)
            return {
                "message" : "Deleted successfully"
            }

    return {"message" : "Student not found"}


@fapp.post("/students/store")
def studentsStore(stu:Student):
    students.append(stu.model_dump())

    return {
        "message" : "Student created",
        "data" : stu
    }


@fapp.post("/students/update/{student_id}")
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