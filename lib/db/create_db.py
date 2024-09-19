from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///game_tracker.db"  

def create_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)  

if __name__ == '__main__':
    create_database()
    print("Database created and tables set up.")