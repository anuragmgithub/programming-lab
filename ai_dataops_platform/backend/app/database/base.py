"""
Base class for all ORM models.

This class acts as the central registry for SQLAlchemy models.
All database tables must inherit from this Base class.

Why this exists:
- Collects model metadata
- Enables table creation via Base.metadata.create_all()
- Required for Alembic migrations
- Ensures single metadata registry across the application

We use SQLAlchemy 2.0 DeclarativeBase for:
- Modern typed ORM
- Better static analysis
- Clean architecture consistency
"""

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
