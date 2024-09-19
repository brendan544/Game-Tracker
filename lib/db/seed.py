from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Player, Team

DATABASE_URL = 'sqlite:///game_tracker.db'  # Adjust as needed

def seed_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create some teams
    team_a = Team(name='Team A')
    team_b = Team(name='Team B')

    # Add teams to the session
    session.add(team_a)
    session.add(team_b)
    session.commit()

    # Create players
    players = [
        Player(name='Player 1', age=25, team=team_a),
        Player(name='Player 2', age=28, team=team_a),
        Player(name='Player 3', age=22, team=team_b),
        Player(name='Player 4', age=30, team=team_b),
    ]

    # Add players to the session
    session.add_all(players)
    session.commit()
    session.close()

    print("Database seeded with initial data.")

if __name__ == "__main__":
    
    seed_db()