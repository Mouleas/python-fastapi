from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

env = os.getenv("ENV", "local")
env_file = f".env.{env}"

load_dotenv(env_file)

DATABASE_URL = os.getenv("DATABASE_URL")
print(f"Using database URL from {env_file} : {DATABASE_URL}")
if not DATABASE_URL:
    raise ValueError(f"DATABASE_URL not found in {env_file}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
