from fastapi import APIRouter, UploadFile 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.inference import run_pipeline 

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile):
    result = run_pipeline(file)
    return result

