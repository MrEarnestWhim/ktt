from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from core.db import models
from core.db.serializer import schemas


async def get_last_price_query(db: Session):
    last_price = db.query(models.PriceModel).order_by(models.PriceModel.date_added.desc()).first()

    if not last_price:
        raise HTTPException(status_code=404, detail="Last Price not found")

    return last_price


async def get_prices_query(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PriceModel).order_by(models.PriceModel.create_dt.desc()).offset(skip).limit(limit).all()


async def write_new_price_query(db: Session, price: schemas.WritePrice):
    db_price = models.PriceModel(price=price.price, date_added=price.date_added, last_updated=price.last_updated)

    db.add(db_price)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Price exist")

    db.refresh(db_price)
    return db_price
