from sqlalchemy import create_engine
from app.core.config import DATABASE_URL

print(DATABASE_URL)

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print("Connected successfully!")