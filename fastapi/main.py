from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi.database import create_tables, delete_tables
from fastapi.router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Shutdown")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

