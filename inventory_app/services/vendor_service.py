from bson import ObjectId
from datetime import datetime


class VendorService:

    def __init__(self, db):
        self.collection = db.vendors

    async def create_vendor(self, data):
        vendor = {
            "name": data.name,
            "email": data.email,
            "is_active": True,
            "created_at": datetime.utcnow()
        }

        result = await self.collection.insert_one(vendor)
        vendor["_id"] = str(result.inserted_id)
        return vendor

    async def get_all_vendors(self):
        vendors = []
        async for vendor in self.collection.find():
            vendor["_id"] = str(vendor["_id"])
            vendors.append(vendor)
        return vendors

    async def update_vendor(self, vendor_id: str, data):
        update_data = {k: v for k, v in data.dict().items() if v is not None}

        await self.collection.update_one(
            {"_id": ObjectId(vendor_id)},
            {"$set": update_data}
        )

        return {"message": "Vendor updated successfully"}

    async def delete_vendor(self, vendor_id: str):
        await self.collection.delete_one({"_id": ObjectId(vendor_id)})
        return {"message": "Vendor deleted successfully"}