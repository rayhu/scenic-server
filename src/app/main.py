from typing import Union
from fastapi import FastAPI, HTTPException, Header
import secrets
from dotenv import load_dotenv
import os
from src.config.settings import settings
from typing import Dict, TypedDict


class ServiceSecret(TypedDict):
    secret: str
    valid: bool


# Load environment variables from .env file
load_dotenv()

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

# Retrieve secrets from environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
ADMIN_SECRET_KEY = os.getenv("ADMIN_SECRET_KEY")

service_secrets_db: Dict[str, ServiceSecret] = {
    "openai": {"secret": os.getenv("OPENAI_API_KEY", ""), "valid": True},
    "anthropic": {"secret": os.getenv("ANTHROPIC_API_KEY", ""), "valid": True},
    "google": {"secret": os.getenv("GOOGLE_API_KEY", ""), "valid": True},
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
    # Check if the provided API key matches the secret key
    if x_api_key != SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    # Check if the service name exists in the service secrets database
    if service_name not in service_secrets_db:
        raise HTTPException(status_code=404, detail="Service not found")
    # Return the service secret and invalidation status
    service_info = service_secrets_db[service_name]
    return {"service_secret": service_info["secret"], "valid": service_info["valid"]}


@app.put("/invalidate-service-secret/{service_name}")
async def invalidate_service_secret(service_name: str, x_api_key: str = Header(...)):
    # Check if the provided API key matches the secret key
    if x_api_key != ADMIN_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid AdminAPI Key")

    # Check if the service name exists in the service secrets database
    if service_name not in service_secrets_db:
        raise HTTPException(status_code=404, detail="Service not found")

    # Invalidate the service secret by setting the invalidated flag to True
    service_secrets_db[service_name]["valid"] = False
    return {"message": f"Service secret for {service_name} invalidated successfully"}


# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
