from fastapi import FastAPI,Form,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from fastapi.responses import HTMLResponse
from models import TaskModel,Base
from database import engine,LocalSession

app=FastAPI()

Base.metadata.create_all(bind=engine)
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates=Jinja2Templates(directory="templates")


@app.get("/",response_class=HTMLResponse)
def home(req:Request):
    with LocalSession() as db:
        tasks = db.query(TaskModel).all()
        return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={"tasks":tasks}
    )

@app.post("/add-task",response_class=HTMLResponse)
def add_task(task:Annotated[str,Form()],req:Request):
    with LocalSession() as db:
        new_task=TaskModel(task=task)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        tasks=db.query(TaskModel).all()
        return templates.TemplateResponse(
            request=req,
            name="home.html",
            context={"tasks":tasks}
        )

@app.post("/delete-task/{task_id}")
def delete_task(task_id: int, req: Request):
    with LocalSession() as db:
        task = db.query(TaskModel).filter(TaskModel.id == task_id).first()

        db.delete(task)
        db.commit()

        tasks = db.query(TaskModel).all()

        return templates.TemplateResponse(
            request=req,
            name="home.html",
            context={"tasks": tasks}
        )