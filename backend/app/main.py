from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('PG_CONN_STR')

engine = create_engine(DATABASE_URL)