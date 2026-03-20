from uuid import UUID
from pydantic import BaseModel, ConfigDict
from app.schemas.game import GameStatus

class RollRequest(BaseModel):
    kept_dice: list[int]

class RollResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    dice_values: list[int]
    kept_dice: list[int]
    score_this_roll: int
    is_farkle: bool
    is_hot_dice: bool

class BankResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    score_banked: int
    next_player_id: UUID
    game_status: GameStatus

class RideResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    inherited_score: int
    inherited_dice: list[int]