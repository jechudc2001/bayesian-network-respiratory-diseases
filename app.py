from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ← AGREGAR ESTA LÍNEA
from pydantic import BaseModel
from pgmpy.inference import VariableElimination
from models import crear_modelo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

class EvidenceInput(BaseModel):
    evidence: dict

model = crear_modelo()
inference = VariableElimination(model)

@app.post("/infer")
def inferencia(input_data: EvidenceInput):
    enfermedades = ['COVID_19', 'Bronquitis', 'Faringitis', 'Neumonia', 'Tuberculosis']
    resultados = {}
    for enfermedad in enfermedades:
        q = inference.query(
            variables=[enfermedad],
            evidence=input_data.evidence,
            show_progress=False
        )
        resultados[enfermedad] = round(q.values[1], 4)


    resultados_ordenados = dict(
        sorted(resultados.items(), key=lambda item: item[1], reverse=True)
    )
    return {"resultados": resultados_ordenados}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)