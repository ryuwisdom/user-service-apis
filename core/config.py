import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("DEBUG", "False").lower() == "true"
print(DEBUG)  # True 또는 False 반환
DB_PORT = int(os.getenv("DB_PORT", 5432))  # 기본값 5432