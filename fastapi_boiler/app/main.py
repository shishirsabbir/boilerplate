# imports
from fastapi import FastAPI
from app.core.config import settings
from app.auth.router import router as auth_router
from app.users.router import router as user_router

# define app
app = FastAPI(title=settings.app_name)


# mouting routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(user_router, prefix="/users", tags=["Users"])


# test route
@app.get("/", tags=["Default"])
async def test():
    return {"message": "Hello World!"}
