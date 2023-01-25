# FastAPI
from fastapi import FastAPI
from .routers import slackRouter
import uvicorn

app = FastAPI()
app. include_router(slackRouter.router)

def start():
    uvicorn.run("slack_bot_.main:app", host="0.0.0.0", port=8000, reload=True)