from dotenv import load_dotenv
import os
import litellm

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
litellm.api_key = OPENAI_API_KEY
