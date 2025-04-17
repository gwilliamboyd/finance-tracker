import os
from sqlmodel import Session, create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('PG_CONN_STR')

engine = create_engine(DATABASE_URL)

# create session
def get_session():
    with Session(engine) as session:
        yield session