from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

#create Engine 
engine = create_engine(
    settings.DATABASE_URL, 
    pool_pre_ping=True,
    pool_size=5,  # how many DB connections stay open
    max_overflow=10, # burst capacity
    echo = False
)

# Session Factory 
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
