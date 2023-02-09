from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.endpoint import router

import uvicorn

app = FastAPI()

app.mount('/form', StaticFiles(directory='./static', html=True), name='static')
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host='0.0.0.0',
        port=80
    )
