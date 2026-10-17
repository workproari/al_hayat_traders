from fastapi import FastAPI

app = FastAPI(
    title="Al Hayat Traders ERP",
    description="Accounting, Inventory, Sales & customer management system. ",
    version="0.1.0",
)

@app.get("/")
def home():
    return{
        "application": "Al Hayat Traders ERP",
        "status": "running",
        "message": "Welcome to Al Hayat Traders",
    }

@app.get("/health")
def health_check():
    return{
        "status": "healthy",
    }

