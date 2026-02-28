from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import db

from services.stock_service import StockService
from services.vendor_service import VendorService
from services.purchase_service import PurchaseService

from inventory_app.schemas.stock_schema import StockCreate, StockUpdate, StockResponse
from inventory_app.schemas.vendor_schema import VendorCreate, VendorUpdate
from inventory_app.schemas.purchase_schema import PurchaseCreate, PurchaseUpdate


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, or specify origins like ["http://example.com"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

# ---------------- STOCK ----------------

@app.post("/items")
async def create_item(item: StockCreate):
    return await StockService(db).create_item(item)

@app.get("/items")
async def get_items():
    return await StockService(db).get_all_items()

# @app.get("/items/{item_id}")
# async def get_item(item_id: str):
#     return await StockService(db).get_item(item_id)

# ✅ Add GET endpoint for getting a single item
@app.get("/items/{item_id}", response_model=StockResponse)
async def get_item(item_id: str):
    # Call the service to get the item
    return await StockService(db).get_item(item_id)

@app.put("/items/{item_id}")
async def update_item(item_id: str, item: StockUpdate):
    return await StockService(db).update_item(item_id, item)

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    return await StockService(db).delete_item(item_id)

@app.post("/items/{item_id}/vendors/{vendor_id}")
async def link_vendor(item_id: str, vendor_id: str):
    return await StockService(db).link_vendor(item_id, vendor_id)

# ---------------- VENDOR ----------------

@app.post("/vendors")
async def create_vendor(vendor: VendorCreate):
    return await VendorService(db).create_vendor(vendor)

@app.get("/vendors")
async def get_vendors():
    return await VendorService(db).get_all_vendors()

@app.put("/vendors/{vendor_id}")
async def update_vendor(vendor_id: str, vendor: VendorUpdate):
    return await VendorService(db).update_vendor(vendor_id, vendor)

@app.delete("/vendors/{vendor_id}")
async def delete_vendor(vendor_id: str):
    return await VendorService(db).delete_vendor(vendor_id)

# ---------------- PURCHASE ----------------

@app.post("/purchase-orders")
async def create_order(order: PurchaseCreate):
    return await PurchaseService(db).create_purchase_order(
        vendor_id=order.vendor_id,
        items=[item.dict() for item in order.items]
    )

@app.get("/purchase-orders")
async def get_orders():
    return await PurchaseService(db).get_all_orders()

# @app.put("/purchase-orders/{order_id}")
# async def update_order(order_id: str, order: PurchaseUpdate):
#     return await PurchaseService(db).update_order(order_id, order)

@app.delete("/purchase-orders/{order_id}")
async def delete_order(order_id: str):
    return await PurchaseService(db).delete_order(order_id)
