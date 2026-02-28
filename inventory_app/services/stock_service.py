# services/stock_service.py

from bson import ObjectId
from datetime import datetime
from inventory_app.utils.serializer import serialize_doc, serialize_list
from inventory_app.schemas.stock_schema import StockResponse


class StockService:

    def __init__(self, db):
        self.collection = db.stock_items

    async def create_item(self, data):
        item = {
            "name": data.name,
            "sku": data.sku,
            "quantity_available": data.quantity_available,
            "price": data.price,
            "vendor_links": [],
            "created_at": datetime.utcnow()
        }

        result = await self.collection.insert_one(item)
        item["_id"] = str(result.inserted_id)
        return item

    async def link_vendor(self, item_id: str, vendor_id: str):
        await self.collection.update_one(
            {"_id": ObjectId(item_id)},
            {
                "$addToSet": {
                    "vendor_links": {
                        "vendor_id": ObjectId(vendor_id),
                        "approved": True
                    }
                }
            }
        )
        return {"message": "Vendor linked successfully"}

    # ✅ Add the get_item method here to fetch a single item
    async def get_item(self, item_id: str):
        # Convert string to ObjectId for MongoDB query
        item = await self.collection.find_one({"_id": ObjectId(item_id)})
        
        if item is None:
            raise Exception("Item not found")

        # Convert _id to id (Ensure key renaming before passing to Pydantic model)
        item['id'] = str(item.pop('_id'))  # Pop _id and assign it to id

        # Return the item using Pydantic to validate the response
        return StockResponse(**item)
    
    async def get_all_items(self):
        items = await self.collection.find().to_list(100)
        return serialize_list(items)
    
    # ✅ Add this method
    async def update_item(self, item_id: str, data):
        update_data = {k: v for k, v in data.dict(exclude_unset=True).items()}
        if not update_data:
            raise Exception("No fields to update")
        
        await self.collection.update_one(
            {"_id": ObjectId(item_id)},
            {"$set": update_data}
        )

        # Return the updated item
        return await self.get_item(item_id)

    # ✅ Add delete_item method
    async def delete_item(self, item_id: str):
        # Find the item by its ID
        item = await self.collection.find_one({"_id": ObjectId(item_id)})
        
        if item is None:
            raise Exception("Item not found")

        # Perform the delete operation
        await self.collection.delete_one({"_id": ObjectId(item_id)})

        return {"message": "Item deleted successfully"}