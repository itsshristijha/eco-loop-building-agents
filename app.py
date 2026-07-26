from fastapi import FastAPI
from controller import run_controller

app = FastAPI(title="Eco Loop Building Agents")

@app.get("/")
def home():
    return {"message": "Eco Loop Building Agents"}

@app.get("/simulate")
def simulate():
    return run_controller()