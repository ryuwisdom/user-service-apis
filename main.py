from fastapi import FastAPI
# from api.routers import api_router
from api.endpoints import user
from db.session import engine
from db.base import Base

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
# Base.metadata.create_all(bind=engine)
# app.include_router(api_router, prefix='/api')
app.include_router(user.router, prefix='/api', tags=['users'])
@app.get('/')
def read_root():
    return {"message": "Hello, Bonnie!"}