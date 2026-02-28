from pydantic import BaseModel
from typing import List
from datetime import datetime


class VendorLink(BaseModel):
    vendor_id: str
    approved: bool = True


class StockCreate(BaseModel):
    name: str
    sku: str
    quantity_available: int
    price: float


class StockUpdate(BaseModel):
    name: str | None = None
    sku: str | None = None
    quantity_available: int | None = None
    price: float | None = None


class StockResponse(BaseModel):
    id: str
    name: str
    sku: str
    quantity_available: int
    price: float
    vendor_links: List[VendorLink]


    # Add the delete_order method
    async def delete_order(self, order_id: str):
        result = await self.orders.delete_one({"_id": ObjectId(order_id)})

        if result.deleted_count == 0:
            raise Exception("Order not found")

        return {"message": "Order deleted successfully"}