# Farkle — CLAUDE.md

## Project
Multiplayer Farkle dice game. React + TypeScript + Vite frontend. FastAPI + PostgreSQL backend. WebSockets for real-time multiplayer. JWT auth.

## Rules
- Never write the Farkle rules engine or scoring logic. That is written by the developer with TDD.
- Generate boilerplate, scaffolding, and styling freely.
- Always validate server-side. Never trust the client.
- Conventional Commits format on all commits.

## Stack
- Frontend: React 18, TypeScript, Tailwind CSS, Vite
- Backend: FastAPI, SQLAlchemy 2.0, Alembic, asyncpg
- DB: PostgreSQL
- Auth: JWT (HttpOnly cookies), bcrypt