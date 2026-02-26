from fastapi import FastAPI

app = FastAPI(title="AI DataOps Platform")

@app.get("/")
async def root():
    return {"message": "AI DataOps Backend Running 🚀"}