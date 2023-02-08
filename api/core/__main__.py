from fastapi import FastAPI
from core.endpoint import router

import uvicorn

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host='0.0.0.0',
        port=80
    )
