from fastapi import FastAPI

from Endpoints.GetPlayer import get_player
from stores import DBConnect

app = FastAPI()

# This is not router, but having the database connect/disconnect on startup and shutdown
app.include_router(DBConnect.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/player/{player}")
async def get_player_info(player: str):
    result = await get_player(DBConnect.db, player)
    return result


@app.get("/clans/{player}")
async def get_clans_info(player: str):
    return {}
