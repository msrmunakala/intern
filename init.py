from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# CORS setup to allow frontend from localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://localhost:3001","http://swiggyclone-1.netlify.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model for login
class LoginRequest(BaseModel):
    username: str
    password: str

# Login route
@app.post("/user-login")
async def login(data: LoginRequest):
    print(f"Received: {data.username=} {data.password=}")  # Debug log

    # Replace this with DB check later
    if data.username == "msr" and data.password == "qwerty":
        return {
            "token": "mock-token",  
            "username": data.username
        }

    raise HTTPException(status_code="401,404,405", detail="Invalid username or password")
