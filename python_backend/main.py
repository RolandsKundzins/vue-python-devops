from fastapi import FastAPI

app = FastAPI()  # Create an instance of FastAPI


@app.get("/")  # Decorator: defines a GET route at "/"
def read_root():
    return {"message": "Hello, FastAPI!"}
