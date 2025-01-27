from fastapi import FastAPI
from routers import controller


app = FastAPI(title="GUS Regon API")

app.include_router(controller.router)