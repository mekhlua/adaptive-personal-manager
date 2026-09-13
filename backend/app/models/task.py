from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    goal_id = Column(Integer, ForeignKey("goals.id"), nullable=True)
    title = Column(String, nullable=False)
    description = Column(String)
    category = Column(String)
    priority = Column(String, default="medium")
    deadline = Column(DateTime)
    estimated_duration = Column(Integer)  # minutes
    actual_duration = Column(Integer)
    status = Column(String, default="planned")
    postponement_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime, nullable=True)
