import asyncio
import uvicorn
import fastapi
import json
import os
from fastapi.responses import JSONResponse

app: fastapi.FastAPI = fastapi.FastAPI()
lock: asyncio.Lock = asyncio.Lock()

@app.get("/")
async def pong() -> JSONResponse:
    return JSONResponse({ "message": "Hello Client!" })

@app.get("/get/{filename}")
async def read_json(filename: str) -> JSONResponse:
    async with lock:
        try:
            with open(f"{filename}.json") as f:
                return JSONResponse(json.load(f))

        except OSError:
            return JSONResponse(
                { "message": "The given file does not exist." },
                404 # Not Found
            )


@app.post("/create/{filename}")
async def create_json(filename: str, data: dict) -> JSONResponse:
    async with lock:
        try:
            with open(f"{filename}.json.tmp", "w") as f:
                json.dump(data, f)
                os.replace(f"{filename}.json.tmp", f"{filename}.json")

            return JSONResponse(
                { "message": "Successfully created file." },
                201 # Created
            )
        
        except OSError:
            return JSONResponse(
                { "message": "Could not create file as it already exists." },
                409 # Conflict
            )

@app.delete("/drop/{filename}")
async def delete_json(filename: str) -> JSONResponse:
    async with lock:
        try:
            os.remove(f"{filename}.json")
            return JSONResponse({ "message": "Successfully deleted file!" })
        except OSError:
            return JSONResponse(
                { "message": "The given file does not exist." },
                404 # Not Found
            )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
