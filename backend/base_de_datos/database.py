from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde un archivo .env



cliente = MongoClient(
            os.getenv("MONGO_URI"), 
            serverSelectionTimeoutMS=5000)  # Tiempo de espera de 5 segundos

db = cliente["appdb"]  

chats_collection = db["chats"]






