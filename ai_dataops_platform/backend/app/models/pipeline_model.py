"""
Pipeline ORM model.

Represents a pipeline definition in the system.
Each pipeline can later have tasks, runs, logs, etc.

__tablename__

Defines the actual table name in MySQL.
Without this, SQLAlchemy won't know what to create.

mapped_column()
This replaces old Column().
It:
Defines column properties
Supports typing
Cleaner syntax
    
"""

from sqlalchemy import String, Text 
from sqlalchemy import mapped, mapped_column

from app.database.base import Base

class Pipeline(Base):
    __tablename__ = "pipelines"

    id: mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    description: mapped[str] = mapped_column(Text, nullable=True)
    status: mapped[str] = mapped_column(String(50), nullable=False, default="created")


