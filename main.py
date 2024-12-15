import os
from dotenv import load_dotenv, dotenv_values
from src.app.main import app

def check_env_files():
    # Load the .env.sample file
    sample_env = dotenv_values(".env.sample")
    
    # Check if .env file exists
    if not os.path.exists(".env"):
        raise FileNotFoundError(".env file is missing. Please create it based on .env.sample.")
    
    # Load the .env file
    actual_env = dotenv_values(".env")
    
    # Compare keys
    missing_keys = [key for key in sample_env if key not in actual_env]
    if missing_keys:
        raise ValueError(f"The following keys are missing in .env: {', '.join(missing_keys)}")

# Check the .env file before running the app
check_env_files()

if __name__ == "__main__":
    app.run()

