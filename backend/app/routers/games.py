from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from pydantic import BaseModel

from app.database import get_db

router = APIRouter()

# @router.post("")
# async def health_check(db: AsyncSession = Depends(get_db)):