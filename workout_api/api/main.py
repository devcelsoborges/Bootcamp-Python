from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "API em Funcionamento"
