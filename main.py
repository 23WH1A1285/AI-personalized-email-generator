from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Enable CORS (Allows frontend to make requests to backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to specific frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Request Model
class EmailRequest(BaseModel):
    prompt: str

@app.post("/generate-email")
async def generate_email(request: EmailRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI email assistant."},
                {"role": "user", "content": request.prompt}
            ]
        )
        email_content = response["choices"][0]["message"]["content"]
        return {"email": email_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Test route
@app.get("/")
def home():
    return {"message": "AI Email Generator API is running!"}
