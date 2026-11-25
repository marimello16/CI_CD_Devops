from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "online", "mensagem": "API FastAPI rodando com CI/CD!"}