from uuid import UUID
from pydantic import BaseModel, ConfigDict


class PlayerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    username: str
    total_score: int
    turn_order: int
    is_on_board: bool