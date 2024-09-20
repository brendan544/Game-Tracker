import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = 'sqlite:///game_tracker.db'  # SQLite database file

def create_database():
    # Create the database engine
    engine = create_engine(DATABASE_URL)
    # Create all tables in the database
    Base.metadata.create_all(engine)
    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_database()