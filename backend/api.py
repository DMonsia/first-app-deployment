from fastapi import FastAPI


app = FastAPI()


@app.get("/welcom/{username}")
async def welcom(username):
    return f"""<h1> Welcome {username}!</h1>
    This is my first deployment using docker and heroku"""
