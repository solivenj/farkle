from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.turns import RollResponse, RollRequest, BankResponse, RideResponse

router = APIRouter(prefix="/games", tags=["turns"])

@router.post("/{game_id}/roll", response_model=RollResponse)
async def roll_dice(
    game_id: UUID,
    body: RollRequest,
    db: AsyncSession = Depends(get_db),
):
    raise NotImplementedError

@router.post("/{game_id}/bank", response_model=BankResponse)
async def bank_score(
    game_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    raise NotImplementedError


@router.post("/{game_id}/ride", response_model=RideResponse)
async def ride(
    game_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    raise NotImplementedError


@router.post("/{game_id}/decline-ride", status_code=200)
async def decline_ride(
    game_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    raise NotImplementedError