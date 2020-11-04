import os
from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session

from core.db import models, queries
from core.db.database import engine
from core.db.serializer import schemas
from core.db.utils import get_db
from core.utils.other import get_data

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
models.Base.metadata.create_all(bind=engine)


@app.get("/get_prices", response_model=List[schemas.GetPrice])
async def get_prices(request: Request, db: Session = Depends(get_db)):
    return await queries.get_prices_query(
        db=db, skip=request.query_params.get("skip") or 0, limit=request.query_params.get("limit") or 100
    )


@app.get("/get_last_price", response_model=schemas.GetPrice)
async def get_last_price(db: Session = Depends(get_db)):
    return await queries.get_last_price_query(db=db)


@app.get("/write_new_price", response_model=schemas.GetPrice)
async def write_new_price(db: Session = Depends(get_db)):
    response = await get_data()
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail=response.json().get("status", {}).get("error_message")
        )

    data = response.json().get("data", {}).get("1", {})
    return await queries.write_new_price_query(
        db=db,
        price=schemas.WritePrice(
            price=data.get("quote", {}).get("USD", {}).get("price"),
            date_added=data.get("date_added"),
            last_updated=data.get("last_updated"),
        ),
    )
