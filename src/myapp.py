from todo.routes import todo_router
from config import config
from fastapi.security import OAuth2PasswordBearer


from fastapi import FastAPI

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

app.include_router(
    todo_router,
    prefix="/items",
    responses={404: {"description": "Not found"}},
)


@app.on_event("startup")
async def app_startup():
    """
    Do tasks related to app initialization.
    """
    config.load_config()


@app.on_event("shutdown")
async def app_shutdown():
    """
    Do tasks related to app termination.
    """
    # This does finish the DB driver connection.
    config.close_db_client()
