# BASE_URL = "https://dummyjson.com"
# TIMEOUT = 10
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TIMEOUT = int(os.getenv("TIMEOUT", 10))