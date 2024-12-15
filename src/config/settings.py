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
    OPENAI_SECRET_KEY: str = os.getenv("OPENAI_SECRET_KEY")
    ANTHROPIC_SECRET_KEY: str = os.getenv("ANTHROPIC_SECRET_KEY")
    GOOGLE_SECRET_KEY: str = os.getenv("GOOGLE_SECRET_KEY")


settings = Settings()
