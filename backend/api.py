from fastapi import FastAPI


app = FastAPI()


@app.get("/welcom")
async def welcom():
    return "<h1> Welcome!</h1></br>This is my first deployment using docker and heroku"
