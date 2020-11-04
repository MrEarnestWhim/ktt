from sqlalchemy import DECIMAL, Column, DateTime, Integer, func

from .database import Base


class PriceModel(Base):
    __tablename__ = "price"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(DECIMAL(precision=15, scale=10, asdecimal=False, decimal_return_scale=None))
    create_dt = Column(DateTime(timezone=True), server_default=func.now())
    date_added = Column(DateTime, index=True)
    last_updated = Column(DateTime, index=True, unique=True)
