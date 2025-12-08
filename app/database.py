from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("MONGO_DB")

if not MONGO_URI:
    raise ValueError("No está definida la variable MONGO_URI en .env")

if not DB_NAME:
    raise ValueError("No está definida la variable MONGO_DB en .env")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]


