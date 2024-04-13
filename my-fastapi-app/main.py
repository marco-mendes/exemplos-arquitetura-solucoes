from fastapi import FastAPI

app = FastAPI()

@app.get("/endpoint_assincrono")
async def endpoint_assincrono():
    return {"mensagem": "Este é um endpoint assíncrono"}

@app.get("/endpoint_sincrono")
def endpoint_sincrono():
    return {"mensagem": "Este é um endpoint síncrono"}