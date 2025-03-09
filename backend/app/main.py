from fastapi import FastAPI

app = FastAPI(redoc_url="/redoc")


@app.get("/")
def read_root():
    return {"message": "Hello World"}
