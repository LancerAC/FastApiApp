from contextlib import asynccontextmanager

from fastapiLearn import FastAPI

from fastapiLearn.database import create_tables, delete_tables
from fastapiLearn.router import router as tasks_router


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

