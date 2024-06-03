"""
Loads in the Huntress API key from an .env file.
"""
import os
import dotenv

def load_api_keys():
    dotenv.load_dotenv()
    return os.getenv('HUNTRESS_API_KEY'), os.getenv('HUNTRESS_API_SECRET')
