import uvicorn
import fastapi
import json
import os
from fastapi.responses import JSONResponse

app: fastapi.FastAPI = fastapi.FastAPI()

@app.get("/")
def pong() -> JSONResponse:
    return JSONResponse({ "message": "Hello Client!" })

@app.get("/get/{filename}")
def read_json(filename: str) -> JSONResponse:
    try:
        with open(f"{filename}.json") as f:
            return JSONResponse(json.load(f))

    except OSError:
        return JSONResponse(
            { "message": "The given file does not exist." },
            404 # Not Found
        )


@app.post("/create/{filename}")
def create_json(filename: str, data: dict) -> JSONResponse:
    try:
        with open(f"{filename}.json", "x") as f:
            json.dump(data, f)

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
def delete_json(filename: str) -> JSONResponse:
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
