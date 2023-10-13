from fastapi import APIRouter

from stores.Database import Database

router = APIRouter()
db = Database()


@router.on_event("startup")
async def startup():
    await db.connect()


@router.on_event("shutdown")
async def shutdown():
    await db.disconnect()
