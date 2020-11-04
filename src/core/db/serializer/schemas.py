from pydantic import BaseModel
from pydantic.validators import Decimal, datetime


class PriceBase(BaseModel):
    price: Decimal


class GetPrice(PriceBase):
    create_dt: datetime
    date_added: datetime
    last_updated: datetime

    class Config:
        orm_mode = True


class WritePrice(PriceBase):
    date_added: datetime
    last_updated: datetime

    class Config:
        orm_mode = True
