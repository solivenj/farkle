from uuid import UUID

from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import Enum
from datetime import datetime

from app.schemas.player import PlayerResponse

class GameStatus(str, Enum):
    in_progress = "in_progress"
    finished = "finished"
    abandoned = "abandoned"

class GameCreate(BaseModel):
    room_id: UUID

class GameResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    status: GameStatus
    started_at: datetime 

class GameState(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    status: GameStatus
    winner_id: Optional[UUID] = None
    started_at: datetime
    finished_at: Optional[datetime] = None
    target_score: int
    turn_number: int
    current_player_id: UUID
    dice_values: list[int]
    kept_dice: list[int]
    score_this_roll: int
    riding_enabled: bool
    inherited_score: int
    inherited_dice: list[int]
    players: list[PlayerResponse]