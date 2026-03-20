from uuid import UUID
from pydantic import BaseModel, ConfigDict
from enum import Enum
from datetime import datetime


class RoomStatus(str, Enum):
    waiting = "waiting"
    in_progress = "in_progress"
    finished = "finished"


class RoomCreate(BaseModel):
    target_score: int = 10000
    max_players: int = 4
    riding_enabled: bool = False   # ← riding config set at lobby creation


class RoomResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    code: str
    host_id: UUID
    status: RoomStatus
    target_score: int
    max_players: int
    riding_enabled: bool
    created_at: datetime