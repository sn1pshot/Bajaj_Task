from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Union, Optional
from fastapi.responses import JSONResponse



app = FastAPI()

@app.get("/bfhl")
def get_operation_code():
    
    response = {
        "operation_code": 1
    }
    return JSONResponse(content=response, status_code=200)

class DataRequest(BaseModel):
    data: List[str]


class DataResponse(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    numbers: List[str]
    alphabets: List[str]
    highest_lowercase_alphabet: Optional[str]

@app.post("/bfhl", response_model=DataResponse)
def process_data(request: DataRequest):
    
    user_id = "john_doe_17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"

    
    numbers = [item for item in request.data if item.isdigit()]
    alphabets = [item for item in request.data if item.isalpha()]
    
    
    lowercase_alphabets = [char for char in alphabets if char.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None
    
    
    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }

    return response
