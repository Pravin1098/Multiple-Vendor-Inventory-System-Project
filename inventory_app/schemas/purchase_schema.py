from pydantic import BaseModel
from typing import List


class PurchaseItem(BaseModel):
    item_id: str
    quantity: int
    unit_price: float


class PurchaseCreate(BaseModel):
    vendor_id: str
    items: List[PurchaseItem]


from pydantic import BaseModel
from typing import List, Optional

class PurchaseUpdate(BaseModel):
    vendor_id: Optional[str]
    items: Optional[List[PurchaseItem]]
    status: Optional[str] = "UPDATED"  # default status for updates

# Other schemas (PurchaseItem, PurchaseCreate, PurchaseResponse) remain the same


class PurchaseResponse(BaseModel):
    id: str
    vendor_id: str
    items: List[PurchaseItem]
    status: str