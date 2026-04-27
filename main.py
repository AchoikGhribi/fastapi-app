from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Render!"}

@app.get("/health")
def health():
    return {"status": "ok"}

if name == "main":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)