from fasapi import FastAPI
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api.routes.predict import router

app = FastAPI()
app.include_router(router)

