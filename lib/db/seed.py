from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Player, Team

DATABASE_URL = 'sqlite:///game_tracker.db'  # Adjust as needed

def seed_data():
    engine = create_engine(DATABASE_URL)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Create Teams
    team1 = Team.create(session, "Team A")
    team2 = Team.create(session, "Team B")

    # Create Players
    Player.create(session, "Alice", 25, team1)
    Player.create(session, "Bob", 30, team1)
    Player.create(session, "Charlie", 22, team2)

    
    print("Database seeded with initial data.")

    session.close()

if __name__ == "__main__":
    seed_data()