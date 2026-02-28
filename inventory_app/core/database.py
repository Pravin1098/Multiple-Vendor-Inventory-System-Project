# core/database.py

from motor.motor_asyncio import AsyncIOMotorClient

# MONGO_URL = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.7.0"
MONGO_URL = "mongodb://mongo:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.7.0"

client = AsyncIOMotorClient(MONGO_URL)
db = client.inventory_db