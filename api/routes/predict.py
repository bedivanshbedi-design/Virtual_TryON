from fastapi import APIRouter, UploadFile 
from backend.inference import run_pipeline 

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile):
    result = run_pipeline(file)
    return result

