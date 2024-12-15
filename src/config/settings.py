import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


class Settings:
    # Application settings
    APP_NAME: str = "Scenic Server"
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"

    # API keys and secrets
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY")
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY")


settings = Settings()
