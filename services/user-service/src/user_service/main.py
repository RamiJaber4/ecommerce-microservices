from fastapi import FastAPI

from user_service.users.registration.router import router as registration_router

app = FastAPI(title="User Service")

app.include_router(registration_router)