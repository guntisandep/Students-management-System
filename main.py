from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel,Field
from fastapi.responses import RedirectResponse

class students(BaseModel):
    Name :str = Field(min_length=3,max_length=30)
    Age : int = Field(le=60,ge=18)
    Gender: str = Field(max_length=7)
    Marks:int = Field(le=100,ge=0)
    Course:str 
    Image:str
    Status:int


import sqlite3

def get_connection():
     connection = sqlite3.connect(
        "students.db"
    )
     return connection
get_connection()
def create_table():
     connection = get_connection()
     cursor = connection.cursor()
     q = """ CREATE TABLE IF NOT EXISTS STUDENTS(
     ID INTEGER PRIMARY KEY AUTOINCREMENT,
     Name TEXT NOT NULL,
     Age INTEGER,
     Gender TEXT,
     Marks INTEGER,
     Course TEXT,
     Image TEXT,
     Status INTEGER)"""
     cursor.execute(q)
     connection.commit()
     connection.close()

create_table()     
          



templates = Jinja2Templates(
    directory="templates"
)

app = FastAPI()

@app.get("/")
def home(req:Request):
    connection = get_connection()
    cursor = connection.cursor()
    q ="select * from students"
    cursor.execute(q)
    students = cursor.fetchall()
    connection.close()
    print(students)

    connection.close()
    return templates.TemplateResponse(
        request=req,
        name ="home.html",
        context={"stds":students}
    ) 
@app.get("/students/{std_id}")
def single_student(req:Request,std_id:int):
    connection= get_connection()
    cursor = connection.cursor()
    q = "select * from students where id =?"
    cursor.execute(q,(std_id,))
    student = cursor.fetchone()
    print(student)

    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="single-std.html",
        context={
            "std":student
        }
    )   
@app.get("/std/delete/{std_id}")
def delete_student(req:Request,std_id:int):
    connection = get_connection()
    cursor = connection.cursor()
    q = "delete from students where id =?"
    cursor.execute(q,(std_id,))
    connection.commit()
    connection.close()
    return RedirectResponse(url="/",status_code=303) 

@app.get("/stds/add")
def send_form(req:Request):
     return templates.TemplateResponse(
          request=req,
          name="add_student.html",
          context={}
     ) 
@app.post("/stds/add")
def filled_form(
     name = Form(),
     age = Form(),
     gender = Form(),
     marks = Form(),
     course = Form(),
     image = Form(),
     status = Form()
    
): 
 
 std_obj = students(
     Name = name,
     Age=age,
     Gender=gender,
     Marks=marks,
     Course=course,
     Image=image,
     Status=status
 )
 print(std_obj.Name,std_obj.Age,std_obj.Gender,std_obj.Marks,std_obj.Course,std_obj.Image,std_obj.Status)
 values = (std_obj.Name,std_obj.Age,std_obj.Gender,std_obj.Marks,std_obj.Course,std_obj.Image,std_obj.Status)
 connection = get_connection()
 cursor = connection.cursor()
 q = """ INSERT INTO students(Name,Age,Gender,Marks,Course,Image,Status)
 values
 (?,?,?,?,?,?,?)
 """
 cursor.execute(q,values)
 connection.commit()
 connection.close()
 return RedirectResponse(url="/",status_code=303) 

@app.get("/sdts/edit/{std_id}")
def update_student(req:Request,std_id:int):
    connection = get_connection()
    cursor = connection.cursor()
    q = "select* from students where id =?"
    cursor.execute(q,(std_id,))
    student = cursor.fetchone()
    print(student)
    return templates.TemplateResponse(
        request=req,
        name="edit_student.html",
        context={
            "std":student
        }
    )
@app.post("/sdts/edit/{std_id}")
def update_std(
    std_id:int,
    name = Form(),
    age = Form(),
    gender = Form(),
    marks = Form(),
    course = Form(),
    image = Form(),
    status = Form()
        
):
    std_obj = students(
        Name = name,
        Age=age,
        Gender=gender,
        Marks=marks,
        Course=course,
        Image=image,
        Status=status
    )
    
    values = (std_obj.Name,std_obj.Age,std_obj.Gender,std_obj.Marks,std_obj.Course,std_obj.Image,std_obj.Status,std_id)
    connection = get_connection()
    cursor = connection.cursor()

    q =""" UPDATE students SET Name = ?,Age = ?,Gender = ?,Marks=?,Course = ?,Image = ?,Status = ? where id = ?"""
    cursor.execute(q,values) 
    connection.commit()
    connection.close()
    return RedirectResponse(url="/",status_code=303) 