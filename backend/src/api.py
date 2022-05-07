from fastapi import FastAPI

## create app
app = FastAPI(title="API", version="0.0.1")


### test the main page
@app.get("/", tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome to API"}
