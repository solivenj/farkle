from typing import Optional

from sqlalchemy import DateTime, Integer, BigInteger, String, ForeignKey, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID, ARRAY, ENUM

import uuid
from datetime import datetime

from app.database import Base

# ENUMS
friendship_status = ENUM("pending", "accepted", "blocked", name="friendship_status")
room_status = ENUM("waiting", "in_progress", "finished", name="room_status")
game_status = ENUM("in_progress", "finished", "abandoned", name="game_status")

# Users table
class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4,primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    password_hash: Mapped[str]
    is_guest: Mapped[bool] = mapped_column(server_default="false")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

class UserStat(Base):
    __tablename__ = "user_stats"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4,primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    games_played: Mapped[int] = mapped_column(Integer, server_default="0")
    games_won: Mapped[int] = mapped_column(Integer, server_default="0")
    high_score: Mapped[int] = mapped_column(Integer, server_default="0")
    total_score: Mapped[int] = mapped_column(BigInteger, server_default="0")
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

class Friendship(Base):
    __tablename__ = "friendships"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4,primary_key=True)
    requester_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    addressee_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    status: Mapped[str] = mapped_column(friendship_status)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4,primary_key=True)
    code: Mapped[str] = mapped_column(String(6), unique=True)
    host_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    status: Mapped[str] = mapped_column(room_status)
    target_score: Mapped[int] = mapped_column(Integer, server_default="10000")
    max_players: Mapped[int] = mapped_column(Integer, server_default="4")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

class Game(Base):
    __tablename__ = "games"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4,primary_key=True)
    room_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("rooms.id"))
    status: Mapped[str] = mapped_column(game_status)
    winner_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("users.id"), nullable=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    finished_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

class GamePlayer(Base):
    __tablename__ = "game_players"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4,primary_key=True)
    game_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("games.id"))
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    turn_order: Mapped[int] = mapped_column(Integer)
    total_score: Mapped[int] = mapped_column(Integer, server_default="0")
    is_on_board: Mapped[bool] = mapped_column(server_default="false")

class Turn(Base):
    __tablename__ = "turns"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4,primary_key=True)
    game_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("games.id"))
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    turn_number: Mapped[int] = mapped_column(Integer)
    score_banked: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_farkle: Mapped[bool] = mapped_column(server_default="false")
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    ended_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

class Roll(Base):
    __tablename__ = "rolls"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4,primary_key=True)
    turn_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("turns.id"))
    roll_number: Mapped[int] = mapped_column(Integer)
    dice_values: Mapped[list[int]] = mapped_column(ARRAY(Integer))
    kept_dice: Mapped[list[int]] = mapped_column(ARRAY(Integer))
    score_this_roll: Mapped[int] = mapped_column(Integer)
    rolled_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))