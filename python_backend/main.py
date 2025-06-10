from fastapi import FastAPI

app = FastAPI()  # Create an instance of FastAPI


@app.get("/message")
def read_root():
    return {"message": "Hello, I am a message from Python backend!"}
