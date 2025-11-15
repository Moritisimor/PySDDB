import uvicorn
import fastapi
import json
import os
from fastapi.responses import JSONResponse

app: fastapi.FastAPI = fastapi.FastAPI()

@app.get("/")
def pong() -> JSONResponse:
    return JSONResponse(
        content={ "message": "Hello Client!" },
        status_code=200 # Ok
    )

@app.get("/get/{filename}")
def read_json(filename: str) -> JSONResponse:
    try:
        with open(f"{filename}.json") as f:
            return JSONResponse(
                content=json.load(f),
                status_code=200 # Ok
            )

    except OSError:
        return JSONResponse(
            content={ "message": "The given file does not exist." },
            status_code=404 # Not Found
        )


@app.post("/create/{filename}")
def create_json(filename: str, data: dict) -> JSONResponse:
    try:
        with open(f"{filename}.json", "x") as f:
            json.dump(data, f)

        return JSONResponse(
            content={ "message": "Successfully created file." },
            status_code=201 # Created
        )
    except OSError:
        return JSONResponse(
            content={ "message": "Could not create file as it already exists." },
            status_code=409 # Conflict
        )

@app.delete("/drop/{filename}")
def delete_json(filename: str) -> JSONResponse:
    try:
        os.remove(f"{filename}.json")
        return JSONResponse(
            content={ "message": "Successfully deleted file!" },
            status_code=200 # Ok
        )
    except OSError:
        return JSONResponse(
            content={ "message": "The given file does not exist." },
            status_code=404 # Not Found
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
