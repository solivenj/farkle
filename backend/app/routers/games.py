from uuid import UUID
from backend.app.models import Game
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone

from app.dependencies import get_db
from app.schemas.game import GameCreate, GameResponse, GameState

router = APIRouter(prefix="/games", tags=["games"])


@router.post("", response_model=GameResponse, status_code=201)
async def create_game(
    body: GameCreate,
    db: AsyncSession = Depends(get_db),
):
    room_id = body.room_id

    # create the game
    game = Game()
    db.add(game)


    await db.commit()
    await db.refresh(game)
  
    return game      

@router.get("/{game_id}", response_model=GameState) # GameState
async def get_game( 
    game_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    raise NotImplementedError

@router.post("/{game_id}/start", response_model=GameResponse)
async def start_game(
    game_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    raise NotImplementedError

@router.post("/{game_id}/leave", status_code=200)
async def leave_game(
    game_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    raise NotImplementedError