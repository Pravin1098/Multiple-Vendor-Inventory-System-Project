from pydantic import BaseModel, EmailStr


class VendorCreate(BaseModel):
    name: str
    email: EmailStr


class VendorUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = None


class VendorResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    is_active: bool