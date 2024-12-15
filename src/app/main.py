from typing import Union
from fastapi import FastAPI, HTTPException, Header
import secrets
from dotenv import load_dotenv
import os
from src.config.settings import settings

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

# Retrieve secrets from environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
service_secrets_db = {
    "openai": os.getenv("OPENAI_SECRET_KEY"),
    "anthropic": os.getenv("ANTHROPIC_SECRET_KEY"),
    "google": os.getenv("GOOGLE_SECRET_KEY"),
}

print("Scenic Server is listening")


def generate_api_key():
    return secrets.token_hex(16)


@app.get("/")
def read_root():
    return {"Hello": settings.APP_NAME}


# @app.post("/issue-secret")
# async def issue_secret(app_name: str):
#     new_api_key = generate_api_key()
#     service_secrets_db[new_api_key] = {"app_name": app_name}
#     return {"api_key": new_api_key}


@app.get("/validate-api-key")
async def validate_api_key(x_api_key: str = Header(...)):
    if x_api_key is not SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return {"message": "API key is valid"}


@app.get("/get-service-secret/{service_name}")
async def get_service_secret(service_name: str, x_api_key: str = Header(...)):
    if x_api_key != SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    if service_name not in service_secrets_db:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"service_secret": service_secrets_db[service_name]}


# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
