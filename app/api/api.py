from fastapi import APIRouter

api_router = APIRouter()

@api_router.get('/health')
async def health_check():
    return {"message":"API is working"}

@api_router.get('/hi')
async def say_hi():
    return {"hello":"I am saying Hi"}
