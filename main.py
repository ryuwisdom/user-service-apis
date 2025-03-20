from fastapi import FastAPI
# from api.routers import api_router
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import user
from db.session import engine
from db.base import Base
from core import config

from celery_app import celery_app
# from tasks import example_task



print(f"🚀 FastAPI started! Redis URL: {config.REDIS_URL}")




# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Bonnie FastAPI Project',
    description="API TEST",
    version='1.0.0',
    openapi_url="/openapi.json",   # OpenAPI 스펙 문서 경로
    docs_url="/docs",             # Swagger UI 경로
    redoc_url="/redoc",           # ReDoc 경로
)

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:3000"],  # 프론트엔드 주소
    allow_origins=["*"],  #
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)
# Base.metadata.create_all(bind=engine)
# app.include_router(api_router, prefix='/api')
app.include_router(user.router, prefix='/api', tags=['users'])
app.include_router(user.router)
@app.get('/')
def read_root():
    return {"message": "Hello, Bonnie!"}