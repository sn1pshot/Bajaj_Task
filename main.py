from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/bfhl")
def get_operation_code():
    # Hardcoded JSON response
    response = {
        "operation_code": 1
    }
    return JSONResponse(content=response, status_code=200)
