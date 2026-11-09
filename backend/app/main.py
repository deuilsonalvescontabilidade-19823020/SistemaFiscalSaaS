from fastapi import FastAPI

app = FastAPI(
    title="Deuilson Alves - Sistema Fiscal Contábil",
    description="Sistema SaaS para escritórios de contabilidade",
    version="1.0.0"
)

@app.get("/")
def inicio():
    return {
        "sistema": "Deuilson Alves - Sistema Fiscal Contábil",
        "status": "online"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
