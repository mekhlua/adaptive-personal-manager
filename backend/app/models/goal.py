from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.core.database import Base


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    category = Column(String)
    start_date = Column(Date)
    target_date = Column(Date)
    priority = Column(String, default="medium")
    status = Column(String, default="active")
    progress = Column(Integer, default=0)
