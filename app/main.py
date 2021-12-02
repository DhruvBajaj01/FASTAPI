from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app=FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published : bool = True
    

while True:
    
    try:
        conn=psycopg2.connect(host="localhost", database="Fastapi", user="postgres", password="Db23012001*", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection is Succesfull")
        break
    except Exception as error :
        print("Connection to Database failed")
        print("Error :",error)
        time.sleep(2)


my_posts = [{"title": "title of post 1", "content":"content of post 1", "id":1},
{"title": "favorite foods","content":"pizza,burger,pasta","id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"]== id:
            return i

@app.get("/")
def root():
    return{"message":"Welcome to API"}



@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts=cursor.fetchall()

    return {"data": posts}



@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts(title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id : int,response : Response):
    cursor.execute("""SELECT * from posts where id = %s""", (str(id)))
    post = cursor.fetchone()
    
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id : {id} was not found")
        
    return {"post_details": post} 

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id :int):
    index = find_index_post(id)
    if index== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id :{id} doesnot exist.")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, post: Post):
    index = find_index_post(id)
    
    if index== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id :{id} doesnot exist.")
   
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data":post_dict}
