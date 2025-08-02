from fastapi import FastAPI

app = FastAPI(title="HR SaaS Backend")

@app.get("/")
async def root():
    return {"message": "HR SaaS API is running"}