from uvicorn import run
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from image2ascii.routes import router

app = FastAPI()
app.include_router(router, prefix="/say")


@app.get("/", include_in_schema=False)
async def home():
    return RedirectResponse(url="/docs/")


if __name__ == '__main__':
    reload: bool = True
    run("runner:app",
        host="0.0.0.0",
        port=80,
        reload=reload)
