import asyncio

import fastapi

from celery_app import celery_app
from core.db import queries
from core.db.database import SessionLocal
from core.db.serializer import schemas
from core.utils.other import get_data


async def _async_function_get_price():
    response = await get_data()
    data = response.json().get("data", {}).get("1", {})
    try:
        await queries.write_new_price_query(
            db=SessionLocal(),
            price=schemas.WritePrice(
                price=data.get("quote", {}).get("USD", {}).get("price"),
                date_added=data.get("date_added"),
                last_updated=data.get("last_updated"),
            ),
        )
    except fastapi.exceptions.HTTPException:
        pass


@celery_app.task(acks_late=True)
def get_price():
    asyncio.run(_async_function_get_price())
    return "task is run"
