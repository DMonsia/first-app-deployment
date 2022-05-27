from fastapi import FastAPI

app = FastAPI(title="API", version="0.0.1")


@app.get("/")
async def index():
    return {"message": "Hello world"}
