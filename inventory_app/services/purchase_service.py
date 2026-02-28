from bson import ObjectId
from datetime import datetime
from inventory_app.utils.serializer import serialize_doc, serialize_list


class PurchaseService:

    def __init__(self, db):
        self.orders = db.purchase_orders
        self.items = db.stock_items

    async def create_purchase_order(self, vendor_id: str, items: list):

        for item in items:
            stock_item = await self.items.find_one({
                "_id": ObjectId(item["item_id"]),
                "vendor_links": {
                    "$elemMatch": {
                        "vendor_id": ObjectId(vendor_id),
                        "approved": True
                    }
                }
            })

            if not stock_item:
                raise Exception("Vendor not approved for this item")

        order_doc = {
            "vendor_id": ObjectId(vendor_id),
            "items": [
                {
                    "item_id": ObjectId(i["item_id"]),
                    "quantity": i["quantity"],
                    "unit_price": i["unit_price"]
                }
                for i in items
            ],
            "status": "CREATED",
            "created_at": datetime.utcnow()
        }

        result = await self.orders.insert_one(order_doc)

        order = await self.orders.find_one({"_id": result.inserted_id})

        return serialize_doc(order)

    async def get_all_orders(self):
        orders = await self.orders.find().to_list(100)
        return serialize_list(orders)
    
    # Add the delete_order method
    async def delete_order(self, order_id: str):
        result = await self.orders.delete_one({"_id": ObjectId(order_id)})

        if result.deleted_count == 0:
            raise Exception("Order not found")

        return {"message": "Order deleted successfully"}