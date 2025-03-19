# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# DATABASE_URL = (
#     f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
#     f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
# )
#
# engine = create_engine(DATABASE_URL, pool_pre_ping=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

import os
from dotenv import load_dotenv  # 추가
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# .env 파일 로드
load_dotenv()

DATABASE_URL = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# 디버깅용 출력
print(f"📌 DATABASE_URL: {DATABASE_URL}")

if not DATABASE_URL:
    raise ValueError("🚨 DATABASE_URL 환경 변수가 설정되지 않았습니다!")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)