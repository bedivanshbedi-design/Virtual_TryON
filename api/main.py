from fasapi import FastAPI
from api.routes.predict import router

app = FastAPI()
app.include_router(router)

