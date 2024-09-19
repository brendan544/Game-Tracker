import argparse
from sqlalchemy.orm import sessionmaker
from models import Base, Player, Team, Game
from sqlalchemy import create_engine

DATABASE_URL = 'sqlite:///game_tracker.db'  # Adjust as needed

def create_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

def add_player(name, age, team_name):
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    team = session.query(Team).filter_by(name=team_name).first()
    if not team:
        print(f"Team '{team_name}' does not exist.")
        return

    player = Player(name=name, age=age, team=team)
    session.add(player)
    session.commit()
    session.close()
    print(f"Added player: {player}")

def main():
    parser = argparse.ArgumentParser(description="Game Tracker CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Create DB command
    subparsers.add_parser('create-db', help='Create the database')

    # Add player command
    add_player_parser = subparsers.add_parser('add-player', help='Add a new player')
    add_player_parser.add_argument('name', type=str, help='Name of the player')
    add_player_parser.add_argument('age', type=int, help='Age of the player')
    add_player_parser.add_argument('team', type=str, help='Team name')

    args = parser.parse_args()

    if args.command == 'create-db':
        create_db()
        print("Database created.")
    elif args.command == 'add-player':
        add_player(args.name, args.age, args.team)

if __name__ == "__main__":
    
    main()

