from fastapi import FastAPI

app = FastAPI()

from registro_foco import registro_foco
from diagnostico_produtividade import diagnostico_produtividade

app.include_router(registro_foco)
app.include_router(diagnostico_produtividade)

# para rodar o código => uvicorn main:app --reload