from fastapi import FastAPI

app = FastAPI()

# healthcheck
@app.get("/")
def hello_world():
    return {"message": "OK"}


@app.get("/api")
def hello_world():
    return {"message": "Needs to be implemented"}