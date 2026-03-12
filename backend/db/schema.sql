-- Enable UUID generation
CREATE EXTENSION IF NOT EXISTS "pgcrypto"; -- sanity check

-- ENUMS
CREATE TYPE friendship_status AS ENUM ('pending', 'accepted', 'blocked');
CREATE TYPE room_status AS ENUM ('waiting', 'in_progress', 'finished');
CREATE TYPE game_status AS ENUM ('in_progress', 'finished', 'abandoned');

-- USERS
CREATE TABLE users (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username        VARCHAR(32) UNIQUE NOT NULL,
    email           VARCHAR(255) UNIQUE,
    password_hash   VARCHAR(255),
    is_guest        BOOLEAN NOT NULL DEFAULT false,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- USER STATS
CREATE TABLE user_stats (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id         UUID UNIQUE NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    games_played    INT NOT NULL DEFAULT 0,
    games_won       INT NOT NULL DEFAULT 0,
    high_score      INT NOT NULL DEFAULT 0,
    total_score     BIGINT NOT NULL DEFAULT 0,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- FRIENDSHIPS
CREATE TABLE friendships (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    requester_id    UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    addressee_id    UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    status          friendship_status NOT NULL DEFAULT 'pending',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (requester_id, addressee_id)
);

-- ROOMS
CREATE TABLE rooms (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code            VARCHAR(6) UNIQUE NOT NULL,
    host_id         UUID NOT NULL REFERENCES users(id),
    status          room_status NOT NULL DEFAULT 'waiting',
    target_score    INT NOT NULL DEFAULT 10000,
    max_players     INT NOT NULL DEFAULT 4,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- GAMES
CREATE TABLE games (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    room_id         UUID NOT NULL REFERENCES rooms(id),
    status          game_status NOT NULL DEFAULT 'in_progress',
    winner_id       UUID REFERENCES users(id),
    started_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    finished_at     TIMESTAMPTZ
);

-- GAME PLAYERS
CREATE TABLE game_players (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    game_id         UUID NOT NULL REFERENCES games(id) ON DELETE CASCADE,
    user_id         UUID NOT NULL REFERENCES users(id),
    turn_order      INT NOT NULL,
    total_score     INT NOT NULL DEFAULT 0,
    is_on_board     BOOLEAN NOT NULL DEFAULT false,
    UNIQUE (game_id, user_id),
    UNIQUE (game_id, turn_order)
);

-- TURNS
CREATE TABLE turns (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    game_id         UUID NOT NULL REFERENCES games(id) ON DELETE CASCADE,
    user_id         UUID NOT NULL REFERENCES users(id),
    turn_number     INT NOT NULL,
    score_banked    INT,
    is_farkle       BOOLEAN NOT NULL DEFAULT false,
    started_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    ended_at        TIMESTAMPTZ,
    UNIQUE (game_id, turn_number)
);

-- ROLLS
CREATE TABLE rolls (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    turn_id         UUID NOT NULL REFERENCES turns(id) ON DELETE CASCADE,
    roll_number     INT NOT NULL,
    dice_values     INT[] NOT NULL,
    kept_dice       INT[] NOT NULL DEFAULT '{}',
    score_this_roll INT NOT NULL DEFAULT 0,
    rolled_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (turn_id, roll_number)
);
