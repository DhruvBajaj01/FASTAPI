from fastapi import FastAPI
from fastapi.params import Body
app=FastAPI()
@app.get("/")
def root():
    return{"message":"Welcome to API"}
@app.get("/posts")
def get_posts():
    return {"data":"this is your posts"}
@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return{"message":"succesfully created posts"}
